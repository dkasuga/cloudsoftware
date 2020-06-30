#-*- using utf-8 -*-
import time
import argparse
import statistics
import math
from matplotlib import pyplot as plt

import numpy as np

def plot(record, file_name="img.png", sec_scale="mill"):
    fig = plt.figure()
    if sec_scale == "mill":
        scale = 1000.0
        sec_unit = "[ms]"
    elif sec_scale == "micro":
        scale = 1e6
        sec_unit = "[micros]"
    else:
        scale = 1.0
        sec_unit = "[s]"

    for data in record:
        n = data["n"]
        mean = data["mean"] * scale
        median = data["median"] * scale
        std = data["std"] * scale
        label = data["label"][0]
        plt.plot(n, mean, label=label)
        plt.fill_between(n, (mean-std), (mean+std), alpha=0.4, color="g")

    plt.legend()
    plt.xlabel("n of fibonacci")
    plt.ylabel("time" + sec_unit)
    fig.savefig(file_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    fib_npz = np.load("out/fib_linux.npz")
    record = []
    record.append(fib_npz)

    plot(record, file_name="fib_graph.png", sec_scale="no")

