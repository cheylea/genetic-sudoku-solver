# Unit Tests for Sudoku Genetic Algorithm

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
import unittest
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from src.algorithm import *
from tests.test_cases import *


# Unit Tests
class TestSudoku(unittest.TestCase):

    # Test correctly structured, solvable grids.
    print("Testing correct values...")

    def test_sudoku_one(self):
        generations = 500
        solution = geneticAlgorithm(generations, initial_a)
        self.assertEqual(0, solution[0])

    def test_sudoku_two(self):
        generations = 500
        solution = geneticAlgorithm(generations, initial_b)
        self.assertEqual(0, solution[0])

    def test_sudoku_three(self):
        generations = 500
        solution = geneticAlgorithm(generations, initial_c)
        self.assertEqual(0, solution[0])

    # Test incorrectly structured grids.
    print("Testing incorrect values...")

    def test_sudoku_four(self):
        generations = 500
        solution = geneticAlgorithm(generations, initial_d)
        self.assertEqual("Please enter a minimum of four unique letters.",
                         solution)

    def test_sudoku_five(self):
        generations = 500
        solution = geneticAlgorithm(generations, initial_e)
        self.assertEqual("Please enter a maximum of four unique letters.",
                         solution)

    def test_sudoku_six(self):
        generations = 500
        solution = geneticAlgorithm(generations, initial_f)
        self.assertEqual("No possible solution", solution)

    # Test getFixed function
    print("Testing fixed values function...")

    def test_fixed(self):
        solution = getFixed(fixed)
        self.assertEqual(fixed_ans, solution)

    # Test fitness_value function
    print("Testing fitness value function...")

    def test_fitness_one(self):
        solution = fitness_value(fitness_one)
        self.assertEqual(fitness_one_ans, solution)

    def test_fitness_two(self):
        solution = fitness_value(fitness_two)
        self.assertEqual(fitness_two_ans, solution)

    def test_fitness_three(self):
        solution = fitness_value(fitness_three)
        self.assertEqual(fitness_three_ans, solution)

    # Test generateSolution

    # Test generatePopulation

    # Test mutateSolution

    # Test crossSolution

    # Test removeDuplicateSolutions
    print("Testing removing duplicate solutions...")

    def test_fixed(self):
        solution = removeDuplicateSolutions(duplicate_list)
        self.assertEqual(duplicate_list_ans, solution)


if __name__ == '__main__':
    print("Beginning unit tests...")
    unittest.main()
    print("Complete.")
