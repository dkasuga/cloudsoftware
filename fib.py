#-*- using utf-8 -*-
import time
import argparse
import statistics
import math
from matplotlib import pyplot as plt

import numpy as np

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def plot(record, file_name="img.png", sec_scale="mill"):
    fig = plt.figure()
    if sec_scale == "mill":
        scale = 1000.0
    else:
        scale = 1.0

    n = record["n"]
    mean = record["mean"] * scale
    median = record["median"] * scale
    std = record["std"] * scale
    plt.plot(n, mean)
    plt.fill_between(n, (mean-std), (mean+std), alpha=0.4, color="g")
    print(mean-std)
    print(mean+std)

    plt.legend()
    plt.xlabel("n of fibonacci")
    plt.ylabel("time [ms]")
    plt.ylim(0.0, 0.1)
    fig.savefig(file_name)



def compute_statistics(timelist):
    mean = statistics.mean(timelist)
    median = statistics.median(timelist)
    std = statistics.stdev(timelist)
    return mean, median, std

def measure_time(n):
    start = time.time()
    fib(n)
    elapsed_time = time.time() - start
    return elapsed_time


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--trials", type=int, default=10)
    parser.add_argument("--max_n", type=int, default=35)

    args = parser.parse_args()
    trials = args.trials
    max_n = args.max_n
    scale = 1000.0

    record = {}
    record["n"] = []
    record["mean"] = []
    record["median"] = []
    record["std"] = []

    for n in range(1, max_n):
        timelist = []
        for i in range(trials):
            t = measure_time(n)
            timelist.append(t)
        mean, median, std = compute_statistics(timelist)
        record["n"].append(n)
        record["mean"].append(mean)
        record["median"].append(median)
        record["std"].append(std)

    print(record)
    record["n"] = np.asarray(record["n"])
    record["mean"] = np.asarray(record["mean"])
    record["median"] = np.asarray(record["median"])
    record["std"] = np.asarray(record["std"])
    plot(record, file_name="fib_graph.png", sec_scale="no")

