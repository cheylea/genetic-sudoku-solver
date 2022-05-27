# Accuracy Tests for Sudoku Genetic Algorithm

# Update PYTHON Path (Source below)
""" Title: Relative imports in Python 3
Author: E-rich
Date: 10th Nov. 2021
Code version: 1.0
Availability:
https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
"""

# Import test cases, functions and test cases
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from src.algorithm import *
from tests.test_cases import *

generations = 10
tests = 0
accuracy_set = []

print("Beginning accuracy tests, this may take a few minutes...")

tests = 0
print("(1) Running test input one of three...")
while tests < generations:
    print("Running algorithm test " +
          str(tests+1) +
          " of " +
          str(generations) +
          "...")
    result = geneticAlgorithm(1000, initial_a)
    result = result[0]
    accuracy = (result / 32) * 100
    accuracy_set.append(accuracy)
    tests += 1

tests = 0
print("(2) Running test input two of three...")
while tests < generations:
    print("Running algorithm test " +
          str(tests+1) +
          " of " +
          str(generations) +
          "...")
    result = geneticAlgorithm(1000, initial_b)
    result = result[0]
    accuracy = (result / 32) * 100
    accuracy_set.append(accuracy)
    tests += 1

tests = 0
print("(3) Running test input three of three...")
while tests < generations:
    print("Running algorithm test " +
          str(tests+1) +
          " of " +
          str(generations) +
          "...")
    result = geneticAlgorithm(1000, initial_c)
    result = result[0]
    accuracy = (result / 32) * 100
    accuracy_set.append(accuracy)
    tests += 1

print("Calculating result...")
print("Algorithm Accuracy: " +
      str(100 - sum(accuracy_set)/len(accuracy_set)) +
      "%")
