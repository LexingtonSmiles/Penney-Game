import pandas as pd
import numpy as np
import random
import os
from wrappers import measure_rw

PATH_DATA = "C:/Users/kmand/DATA 440/Penney-Game/data/permutation3"

seed = 0

def generate_decks(num: int, seed: int):
    """
    make an numpy array of 52 0s and 1s to show black and red cards in a deck
    """
    random.seed(seed)
    arr = []
    for i in range(num):
        arr.append(np.array([False] * 26 + [True] * 26))
    flat = [item for sublist in arr for item in sublist]
    random.shuffle(flat)
    rows = len(arr)
    cols = len(arr[0])
    shuffled_arr = [flat[i * cols:(i + 1) * cols] for i in range(rows)]
    return shuffled_arr

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