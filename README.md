# Penney's Game Project

This repository stores the first project of DATA 440 in Fall 2025: Penney's Game
- **Penney’s Game** is a paradoxical coin-tossing game where two players choose different sequences of coin flips (e.g., `HTH` vs `TTH`). Despite appearing fair, one sequence always has a probabilistic advantage over the other.
- **Humble–Nishiyama Randomness Game** is a variation of Penney’s Game which features a deck of playing cards that substitutes the heads and tails of a coin with 26 red cards and 26 black cards.

## Purpose
This code simulates the Humble-Nishiyma Randomness Game, a variation on Penney's Game. Read the details [here](https://mathwo.github.io/assets/files/penney_game/humble-nishiyama_randomness_game-a_new_variation_on_penneys_coin_game.pdf).



The aim of this project is to:
- Generate and store randomized decks of outcomes.
- Provide tools for running simulations with reproducible randomness.
- Explore empirical probabilities and confirm theoretical predictions.

## Quick Start Guide
DataGeneration.md includes an explanation of our permutations, tests, and results for data generation and storage.
Scoring.md includes an explanation of our scoring logic and the other methods we tried before arriving at our final scoring file.
To generate and score 500,000 decks run main.py

## Contents
src/: Contains source code that is used generate the decks as well as score them.

data/: Contains generated files of each deck and seed.

DataGeneration.md: Explains an explanation of several methods and permutations tested for the first checkpoint of this project: data generation and storage.

main.py: Generates 500,000 decks and scores them.

outputs/scoring_analysis.csv: Contains scores for the number of times P1 and P2 won tricks or cards and the number of draws there were in tricks and cards.
