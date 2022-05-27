# Genetic Algorithm Code

import random
import copy


# grid_to_solve = [['d', ' ', ' ', ' '],
#                  [' ', 'r', ' ', ' '],
#                  [' ', ' ', 'o', ' '],
#                  [' ', ' ', ' ', 'w']]

def getFixed(grid):
    fixed_coords = copy.deepcopy(grid)

    for i in range(0, 4):
        for j in range(0, 4):
            if grid[i][j] == ' ':
                fixed_coords[i][j] = 0
            else:
                fixed_coords[i][j] = 1
    return(fixed_coords)


def fitness_value(grid):
    row_violated = 0
    col_violated = 0
    sub_matrix_violated = 0

    # Check Rows
    for i in range(0, len(grid)):
        group = []
        for j in range(0, len(grid[i])):
            group.append(grid[i][j])
        count = group.count(' ')
        group = list(set(group))
        if count != 0:
            group.remove(' ')
        if len(group) < 4:
            row_violated += 4 - len(group) - count

    # Check Columns
    for i in range(0, len(grid[i])):
        group = []
        for j in range(0, len(grid)):
            group.append(grid[j][i])
        count = group.count(' ')
        group = list(set(group))
        if count != 0:
            group.remove(' ')
        if len(group) < 4:
            col_violated += 4 - len(group) - count

    # Check Sub-Grid
    sub_matrix_one = ([grid[0][0], grid[0][1], grid[1][0], grid[1][1]])
    count = sub_matrix_one.count(' ')
    sub_matrix_one = list(set(sub_matrix_one))
    if count != 0:
        sub_matrix_one.remove(' ')
    sub_matrix_violated += 4 - len(sub_matrix_one) - count

    sub_matrix_two = ([grid[2][0], grid[3][0], grid[2][1], grid[3][1]])
    count = sub_matrix_two.count(' ')
    sub_matrix_two = list(set(sub_matrix_two))
    if count != 0:
        sub_matrix_two.remove(' ')
    sub_matrix_violated += 4 - len(sub_matrix_two) - count

    sub_matrix_three = [grid[0][2], grid[0][3], grid[1][2], grid[1][3]]
    count = sub_matrix_three.count(' ')
    sub_matrix_three = list(set(sub_matrix_three))
    if count != 0:
        sub_matrix_three.remove(' ')
    sub_matrix_violated += 4 - len(sub_matrix_three) - count

    sub_matrix_four = ([grid[2][2], grid[3][2], grid[2][3], grid[3][3]])
    count = sub_matrix_four.count(' ')
    sub_matrix_four = list(set(sub_matrix_four))
    if count != 0:
        sub_matrix_four.remove(' ')
    sub_matrix_violated += 4 - len(sub_matrix_four) - count

    # Result Total Score
    return(row_violated + col_violated + sub_matrix_violated)


def generateSolution(grid):
    to_solve = copy.deepcopy(grid)
    letters_fixed = [[i for i in sub if i != ' '] for sub in to_solve]
    letters_fixed = [i for sub in letters_fixed for i in sub]
    u_letters = list(set(letters_fixed))
    letters_total = u_letters + u_letters + u_letters + u_letters
    for i in letters_fixed:
        for j in letters_total:
            if j == i:
                letters_total.remove(j)
                break
    letters_left = letters_total
    random.shuffle(letters_left)

    for i in range(0, 4):
        for j in range(0, 4):
            if to_solve[i][j] == ' ':
                to_solve[i][j] = letters_left[0]
                letters_left.remove(letters_left[0])

    return(to_solve)


def generatePopulation(grid, generations):
    new_grid = copy.deepcopy(grid)
    solutions = []
    start = 0
    while start <= generations:
        new_grid = grid
        solution = generateSolution(new_grid)
        score = fitness_value(solution)
        solutions.append((score, solution))
        start += 1
    return(solutions)


def mutateSolution(fixed, solution):
    new_solution = copy.deepcopy(solution)
    x = random.random()
    if x < 0.35:
        for i in range(0, 4):
            for j in range(0, 4):
                if fixed[i][j] == 1:
                    continue
                else:
                    x = random.randrange(0, 4)
                    y = random.randrange(0, 4)
                    if fixed[x][y] == 1:
                        continue
                    else:
                        new_solution[i][j] = new_solution[x][y]
    return(new_solution)


def crossSolution(solution_one, solution_two):
    x = random.random()
    result = [solution_one, solution_two]
    if x < 0.35:
        new_solution_one = copy.deepcopy(solution_one)
        new_solution_two = copy.deepcopy(solution_two)
        new_solution_one_alt = copy.deepcopy(solution_one)
        new_solution_two_alt = copy.deepcopy(solution_two)
        attempts = 0
        while attempts < 10:
            x = random.randrange(0, 4)
            y = random.randrange(0, 4)
            sub_grid_one = []
            sub_grid_two = []
            for i in range(0, x + 1):
                for j in range(0, y + 1):
                    sub_grid_one.append(new_solution_one[i][j])
                    sub_grid_two.append(new_solution_two[i][j])
            sub_grid_one.sort()
            sub_grid_two.sort()
            if sub_grid_one == sub_grid_two:
                new_solution_one_alt[i][j] = new_solution_two[i][j]
                new_solution_two_alt[i][j] = new_solution_one[i][j]
                result = [new_solution_one_alt, new_solution_two_alt]
            attempts += 1
        return(result)
    else:
        return(result)


def removeDuplicateSolutions(list):
    no_duplicates = []
    for item in list:
        if item not in no_duplicates:
            no_duplicates.append(item)
    return(no_duplicates)


def geneticAlgorithm(max_limit, grid_to_solve):
    word = [[i for i in sub if i != ' '] for sub in grid_to_solve]
    word = [i for sub in word for i in sub]
    word = list(set(word))
    # Check Correct Letters Given
    word = list(set(word))
    if len(word) < 4:
        return("Please enter a minimum of four unique letters.")
    elif len(word) > 4:
        return("Please enter a maximum of four unique letters.")
    else:
        pass

    # Check if initial positions have a possible solution
    if fitness_value(grid_to_solve) > 0:
        return("No possible solution")
    else:
        # Generate First Set of Random Solutions
        population = generatePopulation(grid_to_solve, 1000)
        population.sort()
        limit = 0

        while limit < max_limit:
            # Check for correct solutions
            # print("Run:" + str(limit))
            if population[0][0] == 0:
                return(population[0])

            else:
                # Mutate Solutions
                fixed = getFixed(grid_to_solve)
                mutated_population = []
                for solution in population:
                    mutated = mutateSolution(fixed, solution[1])
                    score = fitness_value(mutated)
                    mutated_population.append((score, mutated))
                # Select only higher scoring solutions going forward
                population = population + mutated_population
                population.sort()
                slice = round(len(population) * 0.05)
                select_population = population[:slice]
                # Crossover the best solutions to gain new children
                i = 0
                j = 1
                crossover_population = []
                slice_two = round(len(select_population) * 0.20)
                while j < len(select_population[:slice_two]):
                    children = crossSolution(select_population[i][1],
                                             select_population[j][1])
                    solution_one = (fitness_value(children[0]), children[0])
                    solution_two = (fitness_value(children[1]), children[1])
                    crossover_population.append(solution_one)
                    crossover_population.append(solution_two)
                    i += 2
                    j += 2

                # Generate fresh random solutions
                population = select_population + crossover_population
                population.sort()
                range = 1000 - len(population)
                generate_population = generatePopulation(grid_to_solve, range)
                population = population + generate_population
                population.sort()
                limit += 1

        # If solution cannot be found
        if limit == max_limit:
            return(population[0])

# print(geneticAlgorithm(1000,grid_to_solve))
