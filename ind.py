#!/usr/bin/env python3 -*- coding: utf-8 -*-


def foo(*args):
    start, end = [i for i in range(len(args)) if args[i] == 0]
    return sum(args[start + 1: end])


print(foo(1, 2, 3, 0, 5, 6, 7, 0, 8, 9))
