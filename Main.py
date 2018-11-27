import matplotlib.pyplot as plt
import numpy as np
import math
import random


def get_error(individual, points):
    m = individual[1][0]
    b = individual[1][1]
    error = 0
    for index, x_el in enumerate(points[0]):
        y = x_el * m + b
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
    individuals = [[-1, [random.uniform(-10.0, 10.0), random.uniform(-10.0, 10.0)]] for i in range(10)]

    points = np.array([[5,26,42,9], [32,5,16,11]])

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
    for _ in range(1000):
        if to_break:
            break
        print("Starting a round with " + str(len(individuals)) + " individuals")
        # Fill up individuals list with MUTANTS!!!!
        list_to_append = []
        ind_count = 0
        for ind in individuals:
            #print("Individuals processed: " + str(ind_count))
            ind_count += 1
            # deep copy the individual
            new_ind = []
            new_ind.append(ind[0])
            new_ind.append([])
            for el in ind[1]:
                new_ind[1].append(el)

            # mutate the new individual!
            if random.uniform(0, 1) < 0.5:
                if random.uniform(0, 1) < 0.5:
                    new_ind[1][0] += 0.01
                else:
                    new_ind[1][0] -= 0.01
            if random.uniform(0, 1) < 0.25:
                if random.uniform(0, 1) < 0.5:
                    new_ind[1][0] += 0.1
                else:
                    new_ind[1][0] -= 0.1
            if random.uniform(0, 1) < 0.125:
                if random.uniform(0, 1) < 0.5:
                    new_ind[1][0] += 1.0
                else:
                    new_ind[1][0] -= 1.0
            if random.uniform(0, 1) < 0.0625:
                if random.uniform(0, 1) < 0.5:
                    new_ind[1][0] += 10.0
                else:
                    new_ind[1][0] -= 10.0

            if random.uniform(0, 1) < 0.5:
                if random.uniform(0, 1) < 0.5:
                    new_ind[1][1] += 0.01
                else:
                    new_ind[1][1] -= 0.01
            if random.uniform(0, 1) < 0.25:
                if random.uniform(0, 1) < 0.5:
                    new_ind[1][1] += 0.1
                else:
                    new_ind[1][1] -= 0.1
            if random.uniform(0, 1) < 0.125:
                if random.uniform(0, 1) < 0.5:
                    new_ind[1][1] += 1.0
                else:
                    new_ind[1][1] -= 1.0
            if random.uniform(0, 1) < 0.0625:
                if random.uniform(0, 1) < 0.5:
                    new_ind[1][1] += 10.0
                else:
                    new_ind[1][1] -= 10.0
            list_to_append.append(new_ind)
        print("Finished creating mutants")
        for ind in list_to_append:
            individuals.append(ind)
        print()

        # Remove all individuals whose error is greater than average
        get_errors(individuals, points)
        last_avg = avg_error
        while len(individuals) > 100:
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

    print(get_average_error(individuals))
    ind = individuals[0][1]
    y = ind[0] * x + ind[1]
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(points[0], points[1], 'ro')
    plt.show()

main()