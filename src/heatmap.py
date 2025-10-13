import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the data
df = pd.read_csv("scoring_analysis.csv")

# Step 2: Compute total tricks and win/draw rates
df["total_tricks"] = df["p1_wins_tricks"] + df["p2_wins_tricks"] + df["draws_tricks"]
df["p1_trick_win_rate"] = df["p1_wins_tricks"] / df["total_tricks"]
df["draw_trick_rate"] = df["draws_tricks"] / df["total_tricks"]

# Step 3: Create a pivot table with formatted annotations
# Format: "P1% (Draw%)"
df["annotation"] = df.apply(lambda row: f'{row["p1_trick_win_rate"]*100:.1f}% ({row["draw_trick_rate"]*100:.1f}%)', axis=1)

# Get unique p1 and p2 combinations for axes
p1_values = sorted(df["p1"].unique())
p2_values = sorted(df["p2"].unique())

# Create a matrix of annotations
annotation_matrix = pd.DataFrame(index=p1_values, columns=p2_values)

# Fill in the matrix with our formatted annotations
for _, row in df.iterrows():
    annotation_matrix.loc[row["p1"], row["p2"]] = row["annotation"]

# Also create a matrix of numerical values for coloring (just the win rate)
value_matrix = df.pivot(index="p1", columns="p2", values="p1_trick_win_rate")

# Step 4: Plotting the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(value_matrix, annot=annotation_matrix, fmt='', cmap="YlGnBu", cbar_kws={'label': 'P1 Trick Win Rate'})
plt.title("Heatmap of Penney's Game Results")
plt.xlabel("Player 2")
plt.ylabel("Player 1")
plt.tight_layout()
plt.show()
