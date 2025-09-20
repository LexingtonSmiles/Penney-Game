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
For the purposes of Checkpoint 1 (hi professor), DataGeneration.md includes an explanation of our permutations, tests, and results for data generation and storage.
run_tests.py is currently placed inside src/ 
- run to simulate tests

## Contents
code/: Contains source code that is needed to make the project work.

data/: Contains generated files of each deck and seed.

DataGeneration.md: Explains an explanation of several methods and permutations tested for the first checkpoint of this project: data generation and storage.

data/run_tests.py: Generates tables and saves them inside the same folder (the code folder).

data/all_test_results.md: Contains all the tables generated from our testing.
