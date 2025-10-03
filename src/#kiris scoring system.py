import pandas as pd
#kiris scoring system


#generate all the combinations of true and false when three are picked

#compare two combinations to see which win
#combinations cannot be the same for both players


#count the number of tricks won

#count the number of cards won

#NEED AN IDEX COLUMN

#initial ideas:
#- make a df with the combinations already stored then iterate by row to calculate the number of tricks and cards for each player
#- do i need to write the code to look into each file in the data folder then calculate?


def score(df) -> pd.DataFrame:
    for i in range(len(df)): #... will be the total number of rows
        first = 0
        third = 3
        deck = df.at[i, 'decks']
        cards_to_win = 3
        #now use a for loop to calculate the tricks and cards
        for k in range(len(deck)):#... will be 52 for the num of zeros and ones
            if deck[first:third] == df.loc[i, 'P1']:
                df.at[i, 'P1_tricks'] += 1
                df.at[i, 'P1_cards'] += cards_to_win
                first += 3
                third += 3
                cards_to_win = 3
            elif deck[first:third] == df.loc[i, 'P2']:
                df.at[i, 'P2_tricks'] += 1
                df.at[i, 'P2_cards'] += cards_to_win
                first += 3
                third += 3
                cards_to_win = 3
            else:
                cards_to_win += 1
                first += 1
                third += 1
    return
