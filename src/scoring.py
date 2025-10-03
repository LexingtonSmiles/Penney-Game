import pandas as pd
import numpy as np
import os

PATH_DATA = "/Users/lexnguyen/Library/CloudStorage/OneDrive-William&Mary/Fall 2025/DATA_440/Penney-Game-Cloned/data1"
PATH_OUTPUT = "/Users/lexnguyen/Library/CloudStorage/OneDrive-William&Mary/Fall 2025/DATA_440/Penney-Game-Cloned/outputs"
def load_first_raw_file(path: str) -> tuple[np.ndarray, str]:
    """
    Load the first file in a folder whose name contains 'raw' using np.load.
    
    Parameters:
        path (str): Folder path to search for files.
        
    Returns:
        tuple[np.ndarray, str]: Loaded NumPy array and the filename.
                                Returns (None, None) if no file found.
    """
    # List all files in the folder
    all_files = os.listdir(path)

    # Filter only files with "raw" in the name
    raw_files = [f for f in all_files if "raw" in f and os.path.isfile(os.path.join(path, f))]

    if not raw_files:
        print("No raw files found in the folder.")
        return None, None

    # Sort for consistency and pick the first one
    raw_files.sort()
    first_file_name = raw_files[0]
    full_path = os.path.join(path, first_file_name)
    print(f"Loading file: {full_path}")

    # Load the file
    array = np.load(full_path)
    
    return array, first_file_name
    
def count_raw_files(path: str) -> int:
    """
    Count the number of files in the given folder whose filename contains 'raw'.

    Parameters:
        path (str): Folder path to search.

    Returns:
        int: Number of files with 'raw' in the filename.
    """
    count = 0
    for fname in os.listdir(path):
        full_path = os.path.join(path, fname)
        if os.path.isfile(full_path) and "raw" in fname:
            count += 1

    return count

def count_raw_files(path: str) -> int:
    """
    Count the number of files in the given folder whose filename contains 'raw'.

    Parameters:
        path (str): Folder path to search.

    Returns:
        int: Number of files with 'raw' in the filename.
    """
    count = 0
    for fname in os.listdir(path):
        full_path = os.path.join(path, fname)
        if os.path.isfile(full_path) and "raw" in fname:
            count += 1

    return count

# once read, change name
def rename_raw_to_cooked(path: str, filename: str) -> str:
    """
    Rename a single file starting with 'raw-deck' to 'cooked-deck'.

    Parameters:
        path (str): folder path
        filename (str): name of the file to rename

    Raises:
        FileNotFoundError: If the file does not exist
        ValueError: If the filename does not start with 'raw-deck'

    Returns:
        str: The new filename
    """
    old_path = os.path.join(path, filename)

    # Check if file exists
    if not os.path.isfile(old_path):
        raise FileNotFoundError(f"File not found: {old_path}")

    # Check if filename starts with 'raw-deck'
    if not filename.startswith("raw-deck"):
        raise ValueError(f"Filename does not start with 'raw-deck': {filename}")

    # Build new filename and path
    new_name = filename.replace("raw-deck", "cooked-deck", 1)
    new_path = os.path.join(path, new_name)

    # Rename the file
    os.rename(old_path, new_path)
    print(f"Renamed: {filename} -> {new_name}")

    return new_name

def check_or_create_wins_df(folder: str, filename: str, combos: list[dict]) -> pd.DataFrame:
    """
    Check if a CSV file exists in the folder. 
    If yes, load it as a DataFrame. 
    If not, create a blank DataFrame with rows from combos and scoring columns.
    
    Parameters:
        folder (str): Directory where the file might exist.
        filename (str): Name of the CSV file (e.g. 'scoring.csv').
        combos (list): List of dictionaries with player_a and player_b combos.
        
    Returns:
        pd.DataFrame: Loaded or newly created DataFrame.
    """
    filepath = os.path.join(folder, filename)
    
    if os.path.isfile(filepath):
        print(f"Found existing file: {filepath}. Loading DataFrame.")
        df = pd.read_csv(filepath)
    else:
        print(f"No existing file found. Creating blank DataFrame with {len(combos)} rows.")
        
        # Build DataFrame from combos
        df = pd.DataFrame(combos)
        df.rename(columns={"player_a": "p1", "player_b": "p2"}, inplace=True)

        # Add scoring columns initialized to None
        df["p1_wins_cards"] = None
        df["p1_wins_tricks"] = None
        df["p2_wins_cards"] = None
        df["p2_wins_tricks"] = None
        df["draws_cards"] = None
        df["draws_tricks"] = None
    
    return df

def score_deck(deck: np.ndarray, combos: list) -> pd.DataFrame:
    """
    Scores a single deck for both trick and card scoring.
    
    Parameters:
        deck (np.ndarray): the deck to score
        combos (list): a list of all the combinations of players' choices
                       each combo is a dict: {"player_a": tuple, "player_b": tuple}
    
    Returns:
        pd.DataFrame: deck number, player combos, and scores
    """
    
    rows = []
    
    for i, combo in enumerate(combos):
        p1 = combo["player_a"]
        p2 = combo["player_b"]
        
        p1_tricks = 0
        p1_cards = 0
        p2_tricks = 0
        p2_cards = 0
        
        first_card_pos = 0
        third_card_pos = 3
        cards_to_win = 3
        
        # Loop through deck until there aren't enough cards left for a 3-card comparison
        while third_card_pos <= len(deck):
            current_cards = tuple(deck[first_card_pos:third_card_pos])
            
            if current_cards == p1:
                p1_tricks += 1
                p1_cards += cards_to_win
                first_card_pos += 3
                third_card_pos += 3
                cards_to_win = 3
            elif current_cards == p2:
                p2_tricks += 1
                p2_cards += cards_to_win
                first_card_pos += 3
                third_card_pos += 3
                cards_to_win = 3
            else:
                cards_to_win += 1
                first_card_pos += 1
                third_card_pos += 1
        
        rows.append({
            "Decks": deck.tolist(), 
            "p1": p1,
            "p2": p2,
            "p1_tricks": p1_tricks,
            "p1_cards": p1_cards,
            "p2_tricks": p2_tricks,
            "p2_cards": p2_cards
        })
    
    df = pd.DataFrame(rows)
    return df

def save_dataframe_to_csv(df: pd.DataFrame, folder: str, filename: str) -> None:
    """
    Save a pandas DataFrame to a CSV file.

    Parameters:
        df (pd.DataFrame): The DataFrame to save.
        folder (str): Directory where the file will be saved.
        filename (str): The name of the file (e.g. 'output.csv').
    """
    # Make sure the folder exists
    os.makedirs(folder, exist_ok=True)

    # Build full path
    filepath = os.path.join(folder, filename)

    # Save DataFrame
    df.to_csv(filepath, index=False)
    print(f"DataFrame saved to {filepath}")

def count_wins(df: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame with results from a single deck, compute win/loss/draw counts 
    for both game modes (tricks and cards).
    
    Input format:
    Decks | p1 | p2 | p1_tricks | p1_cards | p2_tricks | p2_cards
    
    Output format:
    p1 | p2 | p1_wins_tricks | p2_wins_tricks | draws_tricks |
              p1_wins_cards | p2_wins_cards | draws_cards
    """
    
    results = []

    for _, row in df.iterrows():
        p1, p2 = row["p1"], row["p2"]

        # Initialize counters for one row
        p1_wins_tricks = p2_wins_tricks = draws_tricks = 0
        p1_wins_cards  = p2_wins_cards  = draws_cards  = 0

        # Tricks comparison
        if row["p1_tricks"] > row["p2_tricks"]:
            p1_wins_tricks = 1
        elif row["p1_tricks"] < row["p2_tricks"]:
            p2_wins_tricks = 1
        else:
            draws_tricks = 1

        # Cards comparison
        if row["p1_cards"] > row["p2_cards"]:
            p1_wins_cards = 1
        elif row["p1_cards"] < row["p2_cards"]:
            p2_wins_cards = 1
        else:
            draws_cards = 1

        results.append({
            "p1": p1,
            "p2": p2,
            "p1_wins_tricks": p1_wins_tricks,
            "p2_wins_tricks": p2_wins_tricks,
            "draws_tricks": draws_tricks,
            "p1_wins_cards": p1_wins_cards,
            "p2_wins_cards": p2_wins_cards,
            "draws_cards": draws_cards,
        })

    return pd.DataFrame(results)

def update_results(results_df: pd.DataFrame, scores_df: pd.DataFrame) -> pd.DataFrame:
    """
    Update the cumulative results DataFrame with the new scores from scores_df.
    
    Both DataFrames must have p1, p2 columns.
    """
    # Merge on p1 and p2
    merged = results_df.merge(
        scores_df,
        on=["p1", "p2"],
        how="left",
        suffixes=("", "_new")
    )

    # Columns to update
    score_columns = [
        "p1_wins_tricks", "p2_wins_tricks", "draws_tricks",
        "p1_wins_cards", "p2_wins_cards", "draws_cards"
    ]

    for col in score_columns:
        new_col = col + "_new"
        if new_col in merged:
            # Explicitly convert to numeric to avoid future warning
            merged[col] = pd.to_numeric(merged[col], errors="coerce").fillna(0)
            merged[new_col] = pd.to_numeric(merged[new_col], errors="coerce").fillna(0)

            # Add new values to cumulative totals
            merged[col] = merged[col] + merged[new_col]

            # Remove temporary new column
            merged = merged.drop(columns=new_col)

    return merged

def analyze(data_folder: str, df_folder: str, df_name: str, combos: list):
    """
    Load raw deck files, score each deck using combos, and save/update a DataFrame.
    
    Parameters:
        data_folder (str): folder containing raw deck files
        df_folder (str): folder to store/load main DataFrame
        df_name (str): CSV filename for main DataFrame
        combos (list): list of player combinations
    """
    
    # Count number of raw files
    raw_num = count_raw_files(data_folder)
    
    # Load or create main DataFrame
    df = check_or_create_wins_df(df_folder, df_name, combos)
    
    for file_idx in range(raw_num):
        # Load first raw file
        decks, filename = load_first_raw_file(data_folder)
        if decks is None:
            continue  # skip if no file found
        
        # Ensure decks is 2D (num_decks x deck_length)
        if decks.ndim == 3 and decks.shape[0] == 1:
            decks = decks[0]
        elif decks.ndim == 1:
            decks = decks[np.newaxis, :]  # make it 2D with 1 row
        
        num_decks = decks.shape[0]
        
        for deck_idx in range(num_decks):
            # Get a single deck
            single_deck = decks[deck_idx]
            
            # Score deck
            df_scores = score_deck(single_deck, combos)

            #count scores for wins and draws
            df_wins = count_wins(df_scores)
            
            # Append to main DataFrame
            df = update_results(df,df_wins)
            
        
        # Rename raw file to mark as processed
        rename_raw_to_cooked(data_folder, filename)
    
    # Save updated DataFrame
    save_dataframe_to_csv(df, df_folder, df_name)
    

#list of dictionaries with the 56 relevant players' choices combos
combos = [
    {"player_a": (False, False, False), "player_b": (False, False, True)},
    {"player_a": (False, False, False), "player_b": (False, True, False)},
    {"player_a": (False, False, False), "player_b": (False, True, True)},
    {"player_a": (False, False, False), "player_b": (True, False, False)},
    {"player_a": (False, False, False), "player_b": (True, False, True)},
    {"player_a": (False, False, False), "player_b": (True, True, False)},
    {"player_a": (False, False, False), "player_b": (True, True, True)},
    {"player_a": (False, False, True), "player_b": (False, False, False)},
    {"player_a": (False, False, True), "player_b": (False, True, False)},
    {"player_a": (False, False, True), "player_b": (False, True, True)},
    {"player_a": (False, False, True), "player_b": (True, False, False)},
    {"player_a": (False, False, True), "player_b": (True, False, True)},
    {"player_a": (False, False, True), "player_b": (True, True, False)},
    {"player_a": (False, False, True), "player_b": (True, True, True)},
    {"player_a": (False, True, False), "player_b": (False, False, False)},
    {"player_a": (False, True, False), "player_b": (False, False, True)},
    {"player_a": (False, True, False), "player_b": (False, True, True)},
    {"player_a": (False, True, False), "player_b": (True, False, False)},
    {"player_a": (False, True, False), "player_b": (True, False, True)},
    {"player_a": (False, True, False), "player_b": (True, True, False)},
    {"player_a": (False, True, False), "player_b": (True, True, True)},
    {"player_a": (False, True, True), "player_b": (False, False, False)},
    {"player_a": (False, True, True), "player_b": (False, False, True)},
    {"player_a": (False, True, True), "player_b": (False, True, False)},
    {"player_a": (False, True, True), "player_b": (True, False, False)},
    {"player_a": (False, True, True), "player_b": (True, False, True)},
    {"player_a": (False, True, True), "player_b": (True, True, False)},
    {"player_a": (False, True, True), "player_b": (True, True, True)},
    {"player_a": (True, False, False), "player_b": (False, False, False)},
    {"player_a": (True, False, False), "player_b": (False, False, True)},
    {"player_a": (True, False, False), "player_b": (False, True, False)},
    {"player_a": (True, False, False), "player_b": (False, True, True)},
    {"player_a": (True, False, False), "player_b": (True, False, True)},
    {"player_a": (True, False, False), "player_b": (True, True, False)},
    {"player_a": (True, False, False), "player_b": (True, True, True)},
    {"player_a": (True, False, True), "player_b": (False, False, False)},
    {"player_a": (True, False, True), "player_b": (False, False, True)},
    {"player_a": (True, False, True), "player_b": (False, True, False)},
    {"player_a": (True, False, True), "player_b": (False, True, True)},
    {"player_a": (True, False, True), "player_b": (True, False, False)},
    {"player_a": (True, False, True), "player_b": (True, True, False)},
    {"player_a": (True, False, True), "player_b": (True, True, True)},
    {"player_a": (True, True, False), "player_b": (False, False, False)},
    {"player_a": (True, True, False), "player_b": (False, False, True)},
    {"player_a": (True, True, False), "player_b": (False, True, False)},
    {"player_a": (True, True, False), "player_b": (False, True, True)},
    {"player_a": (True, True, False), "player_b": (True, False, False)},
    {"player_a": (True, True, False), "player_b": (True, False, True)},
    {"player_a": (True, True, False), "player_b": (True, True, True)},
    {"player_a": (True, True, True), "player_b": (False, False, False)},
    {"player_a": (True, True, True), "player_b": (False, False, True)},
    {"player_a": (True, True, True), "player_b": (False, True, False)},
    {"player_a": (True, True, True), "player_b": (False, True, True)},
    {"player_a": (True, True, True), "player_b": (True, False, False)},
    {"player_a": (True, True, True), "player_b": (True, False, True)},
    {"player_a": (True, True, True), "player_b": (True, True, False)},
]

