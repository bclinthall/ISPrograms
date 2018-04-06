# -*- coding: utf-8 -*-

def problem1(n):
    # L[b, h] is the number of proper arrangements of b blocks with
    # first tower height less than or equal to h
    L = {}
    # Base cases
    L[0, 0] = 1
    for b in range(1, n+1):
        L[b, 1] = 1

    for b in range(1, n+1):
        for h in range(2, b+1):
            """
            To get the number of proper arrangements of b blocks with
            first tower height less than or equal to h, start by 
            calculating the number of such arrangements with first 
            tower height of exactly h.

            Since the h blocks are taken up by the first tower, we have
            b - h blocks remaining to make proper arrangements no higher than 
            h. So,
            """
            L[b, h] = L[b-h, min(h, b-h)]
            """
            Then we add in the proper arrangements with b blocks
            and first tower height less than or equal to h - 1
            """
            L[b, h] += L[b, h-1]
    return L

#problem1(5)