import pandas as pd
import numpy as np
import random
import os

PATH_DATA = "C:/Users/kmand/DATA 440/Penney-Game/data/permutation3"

seed = 0

def generate_decks(seed: int):
    """
    make an numpy array of 52 0s and 1s to show black and red cards in a deck
    """
    random.seed(seed)
    arr = np.array([True] * 26 + [False] * 26)
    np.random.shuffle(arr)
    return arr

def num_of_decks_per_file(tot_n:int, max_decks:int):
    full_files = tot_n // max_decks
    leftover = tot_n % max_decks
    return full_files, leftover

def filepath_raw(seed: int, num_of_decks: int):
    """
    generate file name for each individual deck
    """
    filename = (f'raw-deck_seed{seed}_num_of_decks{num_of_decks}.npy')
    raw_filepath = os.path.join(PATH_DATA, filename)
        
    return raw_filepath

def savefile(decks: np.array, filepath: str):
    """
    save n decks to a .npy file with a specific file destination
    """
        
    directory = os.path.dirname(filepath)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    np.save(filepath, decks)
    return


@timer 
@file_storage_tracker
def make_files(tot_n:int, max_decks:int = 10000, seed:int = seed):
    """
    use generate function to make the decks for each file then use save function to 
    save each file with the filename function
    """
    #use num of files to determine how many decks go in each file
    full_files, leftover = num_of_decks_per_file(tot_n = tot_n, max_decks = max_decks)

    

    for i in range(full_files):
        #make a placeholder for all decks about to go into the file
        full_storage = []
         
        #generate decks for the full files
        if full_files != 0:
            for i in range(max_decks):
                full_storage.append(generate_decks(seed))
            
            #make filepath/name
            filepath = filepath_raw(seed, max_decks)

            #use save file raw to save the file with all the decks in it  
            savefile(full_storage, filepath)

            #update the seed number
            seed = seed + 1

    if leftover != 0:
        #make new placeholder for decks about to go into leftover file
        leftover_storage = []
            
        #generate decks for the not full files
        for i in range(leftover):
            leftover_storage.append(generate_decks(seed))

        #make filepath/name
        filepath = filepath_raw(seed, leftover)

        #use save file raw to save the file with all the decks in it
        savefile(leftover_storage, filepath)

        #update the seed number
        seed = seed + 1
    return
