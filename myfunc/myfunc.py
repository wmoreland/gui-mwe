#!/usr/bin/env python3

def myfunc(x):
    try:
        return int(x) ** 2
    except ValueError:
        return float(x) ** 2

if __name__ == '__main__':
    myfunc(2)
