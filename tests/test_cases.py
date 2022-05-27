# Input Tests (Correct Structure)
initial_a = [['d', ' ', ' ', ' '],
             [' ', 'r', ' ', ' '],
             [' ', ' ', 'o', ' '],
             [' ', ' ', ' ', 'w']]


initial_b = [[' ', ' ', ' ', ' '],
             [' ', 't', ' ', ' '],
             [' ', 'e', 'k', ' '],
             ['r', ' ', ' ', ' ']]

initial_c = [[' ', ' ', ' ', 'h'],
             [' ', ' ', ' ', 'o'],
             [' ', ' ', ' ', 'p'],
             [' ', ' ', ' ', 'e']]

# Input Tests (Incorrect Structure)

# Not enough unique letters
initial_d = [['d', ' ', ' ', ' '],
             [' ', 'r', ' ', ' '],
             [' ', ' ', 'r', ' '],
             [' ', ' ', ' ', 'w']]

# Too many unique letters
initial_e = [[' ', ' ', ' ', '8'],
             [' ', 't', ' ', 'm'],
             [' ', 'e', 'k', ' '],
             ['r', ' ', ' ', ' ']]

# Impossible to find solution
initial_f = [[' ', ' ', ' ', 'h'],
             [' ', ' ', 'o', 'o'],
             [' ', ' ', ' ', 'p'],
             [' ', ' ', ' ', 'e']]


# Test individual function components

# getFixed
fixed = [['d', ' ', ' ', ' '],
         [' ', 'r', ' ', ' '],
         [' ', ' ', 'o', ' '],
         [' ', ' ', ' ', 'w']]

fixed_ans = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

# fitness_value
fitness_one = [['d', 'o', 'o', 'r'],    # 10
               ['o', 'r', 'w', 'w'],
               ['w', 'd', 'o', 'd'],
               ['r', 'd', 'r', 'w']]

fitness_two = [['d', 'w', 'd', 'd'],    # 14
               ['d', 'r', 'w', 'o'],
               ['r', 'r', 'o', 'r'],
               ['o', 'o', 'w', 'w']]

fitness_three = [['d', 'o', 'w', 'r'],  # 0
                 ['w', 'r', 'd', 'o'],
                 ['r', 'w', 'o', 'd'],
                 ['o', 'd', 'r', 'w']]

fitness_one_ans = 10
fitness_two_ans = 14
fitness_three_ans = 0

# generateSolution
# generatePopulation
generate = [['d', ' ', ' ', ' '],
            [' ', 'r', ' ', ' '],
            [' ', ' ', 'o', ' '],
            [' ', ' ', ' ', 'w']]


# mutateSolution
# crossSolution
solution_one = [['d', 'o', 'o', 'r'],
                ['o', 'r', 'w', 'w'],
                ['w', 'd', 'o', 'd'],
                ['r', 'd', 'r', 'w']]

solution_two = [['d', 'w', 'd', 'd'],
                ['d', 'r', 'w', 'o'],
                ['r', 'r', 'o', 'r'],
                ['o', 'o', 'w', 'w']]


# removeDuplicateSolutions
duplicate_list = [[['d', 'w', 'd', 'd'],
                   ['d', 'r', 'w', 'o'],
                   ['r', 'r', 'o', 'r'],
                   ['o', 'o', 'w', 'w']],
                  [['d', 'w', 'd', 'd'],
                   ['d', 'r', 'w', 'o'],
                   ['r', 'r', 'o', 'r'],
                   ['o', 'o', 'w', 'w']]]

duplicate_list_ans = [[['d', 'w', 'd', 'd'],
                       ['d', 'r', 'w', 'o'],
                       ['r', 'r', 'o', 'r'],
                       ['o', 'o', 'w', 'w']]]
