import pandas as pd
import numpy as np
import random
import os
from wrappers import measure_rw

PATH_DATA = "C:/Users/kmand/DATA 440/Penney-Game/data/permutation5"

seed = 0

def generate_decks(n: int, seed: int):
    """
    Creates n by 52 array of n amount of shuffled decks each containing 26 Trues and 26 Falses
    """
    rng = np.random.default_rng(seed)
    
    # base deck
    deck = np.array([True] * 26 + [False] * 26)
    
    # generates n random permutations of indices [0..51]
    idx = np.array([rng.permutation(52) for _ in range(n)])
    
    # applies permutations to deck
    arr = deck[idx]
    
    return arr

def num_of_decks_per_file(tot_n:int, max_decks:int):
    #calculate number of files that will be filled to their max deck size
    full_files = tot_n // max_decks
    #calculate the number of decks to go in the final file that will not be full
    leftover = tot_n % max_decks
    return full_files, leftover

def filepath_raw(seed: int, num_of_decks: int):
    """
    generate file name for each individual deck
    """
    #create filename based on the random seed and number of decks in the file
    filename = (f'raw-deck_seed{seed}_num_of_decks{num_of_decks}.npy')
    #join the filepath previously listed with the new name
    raw_filepath = os.path.join(PATH_DATA, filename)
        
    return raw_filepath

def savefile(decks: np.array, filepath: str):
    """
    save n decks to a .npy file with a specific file destination
    """
    #get the directory from the full filepath
    directory = os.path.dirname(filepath)
    #if the directory part is not empty and it doesn't exist then create it
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    #save the numpy array to the specified .npy file
    np.save(filepath, decks)
    return

@measure_rw
def make_files3(tot_n:int, max_decks:int = 10000, seed:int = seed):
    """
    use generate function to make the decks for each file then use save function to 
    save each file with the filename function
    """
    #use num of files to determine how many decks go in each file
    full_files, leftover = num_of_decks_per_file(tot_n = tot_n, max_decks = max_decks)

    filepaths = [] 

    for i in range(full_files):
        #make a placeholder for all decks about to go into the file
        full_storage = []
         
        #generate decks for the full files
        if full_files != 0:
            full_storage.append(generate_decks(max_decks, seed))
            
            #make filepath/name
            filepath = filepath_raw(seed, max_decks)

            #use save file raw to save the file with all the decks in it  
            savefile(full_storage, filepath)

            filepaths.append(filepath)

            #update the seed number
            seed = seed + 1

    if leftover != 0:
        #make new placeholder for decks about to go into leftover file
        leftover_storage = []
            
        #generate decks for the not full files
        leftover_storage.append(generate_decks(leftover, seed))

        #make filepath/name
        filepath = filepath_raw(seed, leftover)

        #use save file raw to save the file with all the decks in it
        savefile(leftover_storage, filepath)

        filepaths.append(filepath)

        #update the seed number
        seed = seed + 1

    file_sizes = [os.path.getsize(path) for path in filepaths if os.path.exists(path)]

    return filepaths, file_sizes