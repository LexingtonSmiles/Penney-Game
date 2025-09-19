import numpy as np
import pandas as pd
import os


def __generate_decks(tot_decks:int, max_decks:int = 10000):
    """
    Generates tot_decks of decks with n decks in each file, with a n maxxing out at max_decks
    """
   
    #calculates how many deck files are needed
    y = __calc_decks(tot_decks = tot_decks, max_decks = max_decks)
    #how many files with max_decks are needed
    num_decks_maxxed = y[0]
    #for when there are less decks than the max decks per file 
    num_decks_rem = y[1]

    #create that many maxxed files then finish with one file with remaining decks
    
    for i in range(num_decks_maxxed):
        #finds next seed
        seed =find_next_seed()
        #creates array of shuffled decks
        array = __shuffle_decks(n = max_decks, seed = seed)
        #saves array
        __save_deck_file(array, seed, n = max_decks)

    #create last file
    if num_decks_rem != 0:
        n = num_decks_rem
        #finds next seed 
        seed= find_next_seed()
        array =  __shuffle_decks(n = n, seed = seed)
        __save_deck_file(array, seed, n= n)
    print('all done!')

    
        #need to generate multiple arrays with diff seeds each array with max_decks
        #loop and check for what seeds are used already... use filenames to see?...
        #or can just put the above in a loop for that amount of times

def __calc_decks(tot_decks:int, max_decks:int):
    """
    Calculates the number of files and the amount of decks needed in each file
    """
    num_decks_maxxed = tot_decks//max_decks

    num_decks_rem = tot_decks%max_decks

    return num_decks_maxxed, num_decks_rem

def __shuffle_decks(n: int, seed: int):
    """
    Creates n by 52 array of n amount of shuffled decks each containing 26 Trues and 26 Falses
    """
    rng = np.random.default_rng(seed)
    
    # Base deck
    deck = np.array([0] * 26 + [1] * 26)
    
    # Generate n random permutations of indices [0..51]
    idx = np.array([rng.permutation(52) for _ in range(n)])
    
    # Apply permutations to deck
    arr = deck[idx]
    
    return arr

PATH_DATA = "C:/Users/kmand/DATA 440/Penney-Game/data"

def savefile(decks: np.array, filepath: str):
    """
    save n decks to a .npy file with a specific file destination
    """
        
    directory = os.path.dirname(filepath)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    np.save(filepath, decks)
    return

def __filename_raw(seed: int, n: int):
    """
    Creates filename for generated deck files 
    """
    filename = (f'raw-deck_seed{seed}_n_{n}')
    #raw_filename = os.path.join(PATH_DATA, filename)
    return filename

def __load_data(file_path:str):
    loaded_deck = np.load(file_path)
    print(loaded_deck)

def find_next_seed() -> int | None:
    """
    Scans all files in a directory and finds the highest seed number
    in filenames formatted like '*-deck_seed{seed}_n_{n}'.
    
    Works for both 'raw-deck' and 'cooked-deck'.
    """
    seeds = []
    

    for fname in os.listdir(PATH_DATA):
        if "-deck_seed" in fname and "_n_" in fname:
            try:
                # Example: "cooked-deck_seed123_n_52"
                parts = fname.split('_')        # ['cooked-deck', 'seed123', 'n', '52']
                seed_str = parts[1][4:]         # remove 'seed' -> '123'
                seeds.append(int(seed_str))
            except (IndexError, ValueError):
                continue
    return int(max(seeds)+1) if seeds else 1