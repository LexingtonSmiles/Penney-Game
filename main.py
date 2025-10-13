from src.datageneration import make_files
from src.scoring import analyze, combos

seed = 0

make_files(tot_n = 9, max_decks= 2, seed = seed)

analyze(data_folder= "C:/Users/kmand/DATA 440/Penney-Game/testdata", df_folder = "C:/Users/kmand/DATA 440/Penney-Game/testdata", df_name = 'scoring_analysis', combos = combos)