import statistics
import numpy as np

def mean_median(array_input):
    if not array_input:
        return None

    # Menghitung mean
    mean = np.mean(array_input)

    # Menghitung median
    median = statistics.median(array_input)

    return (mean, median)


if __name__ == '__main__':
    print(mean_median([1, 2, 3, 4])) # (2.5, 2.5)
    print(mean_median([1, 2, 3, 4, 5])) # (3.0, 3)
    print(mean_median([7, 8, 9, 13, 15])) # (10.4, 9)
    print(mean_median([10, 20, 30, 40, 50])) # (30.0, 30)
    print(mean_median([15, 20, 30, 60, 120])) # (49.0, 30)