from src.datageneration import make_files
from src.scoring import analyze, combos

seed = 0

make_files(tot_n = 500000, max_decks= 50000, seed = seed)

analyze(data_folder= "C:/Users/kmand/DATA 440/Penney-Game/data", df_folder = "C:/Users/kmand/DATA 440/Penney-Game/outputs", df_name = 'scoring_analysis', combos = combos)