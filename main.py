from src.datageneration import make_files
from src.scoring import analyze, combos
from src.heatmap import heatmap

seed = 0

make_files(tot_n = 9, max_decks= 2)

analyze(data_folder= "C:/Users/kmand/DATA 440/Penney-Game/data", df_folder = "C:/Users/kmand/DATA 440/Penney-Game/outputs", df_name = 'scoring_analysis', combos = combos)

heatmap(path = "C:/Users/kmand/DATA 440/Penney-Game/outputs")