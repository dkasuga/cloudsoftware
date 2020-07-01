#-*- using utf-8 -*-
import time
import argparse
import statistics
import math
from matplotlib import pyplot as plt

import numpy as np
import os.path

def fib(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1

    if n == 0 or n == 1:
        return 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

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
    parser.add_argument("--max_n", type=int, default=10000)
    parser.add_argument("--process", type=str, default="fib_dp")
    parser.add_argument("--output_dir", type=str, default="out")
    parser.add_argument("--env", type=str, default="linux")

    args = parser.parse_args()
    trials = args.trials
    max_n = args.max_n
    output_dir = args.output_dir
    file_name = args.process + "_" + args.env
    output_file_name = os.path.join(output_dir, file_name)

    n_list = []
    mean_list = []
    median_list = []
    std_list = []

    for n in range(1, max_n):
        timelist = []
        for i in range(trials):
            t = measure_time(n)
            timelist.append(t)
        mean, median, std = compute_statistics(timelist)
        n_list.append(n)
        mean_list.append(mean)
        median_list.append(median)
        std_list.append(std)

    n_np = np.asarray(n_list)
    mean_np = np.asarray(mean_list)
    median_np = np.asarray(median_list)
    std_np = np.asarray(std_list)
    label_np = np.array([file_name])
    np.savez(output_file_name, n=n_np, mean=mean_np, median=median_np, std=std_np, label=label_np)

