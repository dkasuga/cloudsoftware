#-*- using utf-8 -*-
import time
import sys

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

if __name__ == '__main__':
    args = sys.argv
    num = 1
    if len(args) >= 2:
        if args[1].isdigit():
            num = int(args[1])
    start = time.time()
    for i in range(1000):
        print(fib(num))
    elapsed_time = time.time() - start
    print("avg:{0}".format(elapsed_time/1000.0) + "[sec]")

