#!/usr/bin/env python3 -*- coding: utf-8 -*-

def fun(lst, flag=True, res=0, tmp=0):
    for num in lst:
        if not num:
            if flag:
                flag = False
            else:
                res += tmp
                tmp = 0

        if not flag:
            tmp += num

    return res


s = [0, 1, 5, 0, 4, 8, 5, 0, 6, 7, 0, 0, 8, 9, 0]
print(fun(s))
