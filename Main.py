import matplotlib.pyplot as plt
import numpy as np
import math
import random

NUMBER_COMPONENTS = 2


def get_error(individual, points):
    components = individual[1]
    error = 0
    for index, x_el in enumerate(points[0]):
        # y = x_el * m + b
        y = 0
        for comp_index, comp in enumerate(components):
            y += comp * (x_el ** (len(components) - 1 - comp_index))
        error += (y - points[1][index]) ** 2
    error = math.sqrt(error)
    individual[0] = error


def get_errors(individuals, points):
    for individual in individuals:
        get_error(individual, points)


def get_average_error(individuals):
    total = 0
    for ind in individuals:
        total += ind[0]
    total /= float(len(individuals))
    return total


def main():
    individuals = [[-1, [random.uniform(-10.0, 10.0) for _ in range(NUMBER_COMPONENTS)]] for _ in range(1000)]

    points = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 7, 13, 21, 31, 43, 57, 73, 91, 111]])

    x = np.arange(min(points[0]) - 1, max(points[0]) + 1, 0.2)

    get_errors(individuals, points)
    avg_error = get_average_error(individuals)
    print(avg_error)

    # Remove all individuals whose errors are greater than the average
    to_remove = []
    for ind in individuals:
        if ind[0] > avg_error:
            to_remove.append(ind)
    for ind in to_remove:
        individuals.remove(ind)
    to_break = False
    while avg_error > 0.1 * len(points[0]):  # for _ in range(1000): # Modify for specific situations
        if to_break:
            break
        print("Starting a round with " + str(len(individuals)) + " individuals")
        print("Avg error: " + str(avg_error))
        print("'Best' error: " + str(individuals[0][0]))
        # Fill up individuals list with MUTANTS!!!!
        list_to_append = []
        ind_count = 0
        for ind in individuals:
            ind_count += 1
            # deep copy the individual
            new_ind = []
            new_ind.append(ind[0])
            new_ind.append([])
            for el in ind[1]:
                new_ind[1].append(el)

            # mutate the new individual!
            for comp_index, comp in enumerate(new_ind[1]):
                if random.uniform(0, 1) < 0.5:
                    if random.uniform(0, 1) < 0.5:
                        new_ind[1][comp_index] += 0.01
                    else:
                        new_ind[1][comp_index] -= 0.01
                if random.uniform(0, 1) < 0.25:
                    if random.uniform(0, 1) < 0.5:
                        new_ind[1][comp_index] += 0.1
                    else:
                        new_ind[1][comp_index] -= 0.1
                if random.uniform(0, 1) < 0.125:
                    if random.uniform(0, 1) < 0.5:
                        new_ind[1][comp_index] += 0.2
                    else:
                        new_ind[1][comp_index] -= 0.2
                if random.uniform(0, 1) < 0.0625:
                    if random.uniform(0, 1) < 0.5:
                        new_ind[1][comp_index] += 0.3
                    else:
                        new_ind[1][comp_index] -= 0.3
            list_to_append.append(new_ind)
        print("Finished creating mutants")
        for ind in list_to_append:
            individuals.append(ind)
        print()

        # Remove all individuals whose error is greater than average
        get_errors(individuals, points)
        last_avg = 0
        while len(individuals) > 1000:
            last_avg = avg_error
            get_errors(individuals, points)
            avg_error = get_average_error(individuals)
            to_remove = []
            for ind in individuals:
                if ind[0] > avg_error:
                    to_remove.append(ind)
            if abs(avg_error - last_avg) < 0.001:
                to_break = True
                break
            if len(to_remove) == len(individuals) or len(to_remove) == 0:
                print(avg_error)
                break
            for ind in to_remove:
                individuals.remove(ind)
        if to_break:
            break

    print("Average error: " + str(get_average_error(individuals)))
    ind = individuals[0][1]
    print("Error of best: " + str(individuals[0][0]))
    print(ind)
    y = x - x
    for comp_index, comp in enumerate(ind):
        y += comp * (x ** (len(ind) - 1 - comp_index))
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(points[0], points[1], 'ro')
    plt.show()


main()
