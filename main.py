from src.datageneration import make_files
from src.scoring import analyze, combos
from src.heatmap import heatmap

DATA_FOLDER = "C:/Users/kmand/DATA 440/Penney-Game/data"
DF_FOLDER = "C:/Users/kmand/DATA 440/Penney-Game/outputs"
HEATMAP_FOLDER = "C:/Users/kmand/DATA 440/Penney-Game/figures"

make_files(tot_n = 9, max_decks= 2)

analyze(data_folder= DATA_FOLDER, df_folder = DF_FOLDER, df_name = 'scoring_analysis', combos = combos)

heatmap(df_folder = DF_FOLDER, heatmap_folder = HEATMAP_FOLDER)