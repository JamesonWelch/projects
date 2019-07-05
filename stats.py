import math
from os.path import dirname, join


current_dir = dirname(__file__)
file_path = join(current_dir, "sample_dataset.txt")


dataset = []
with open(file_path) as f:
    for line in f:
        line = int(line)
        dataset.append(line)


def total():
    return len(dataset)


def summation():
    s = 0
    for i in dataset:
        s += i
    return s


def sample_mean():
    s = summation()
    return s / (len(dataset))


def sample_variance():
    mean = sample_mean()
    return sum(pow(x - mean, 2) for x in dataset) / len(dataset)


def sample_std_deviation():
    mean = sample_mean()
    var = sum(pow(x - mean, 2) for x in dataset) / len(dataset)
    return math.sqrt(var)


def sorting(data):
    sorted_data = []

    while data:
        minimum = data[0]
        for x in data:
            if x < minimum:
                minimum = x
        sorted_data.append(minimum)
    return sorted_data


def median():
    n_sort = sorting(dataset)
    n = len(dataset)
    if n % 2 == 0:
        median1 = n_sort[n // 2]
        median2 = n_sort[n // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = n_sort[n // 2]
    return median


def minimum():
    min_d = dataset[0]
    for i in range(1, len(dataset)):
        if min_d > dataset[i]:
            min_d = dataset[i]
    return min_d, i


def maximum():
    max_d = dataset[0]
    for i in range(1, len(dataset)):
        if max_d < dataset[i]:
            max_d = dataset[i]
    return max_d

