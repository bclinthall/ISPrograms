"""
Your proper arrangements of blocks were taking up too much space
against your wall. Now you want to know how many proper arrangements
you can make that include W or fewer towers with a first tower
height of H or less.
"""

import math
#from DiscreteDistributions import p1

def problem2(n, W):
    H = n

    # L[b, h, w] is the number of proper arrangements of b blocks with
    # first tower height less than or equal to h and w or fewer tower.
    L = {}
    # Base cases
    L[0, 0, 0] = 1
    L[1, 1, 1] = 1
    for b in range(1, n+1):
        L[b, 1, b] = 1
        L[b, b, 1] = 1
    for b in range(1, n+1):
        for h in range(2, min(H, b) + 1):
            for w in range(max(2, math.ceil(b / h)), min(b, W) + 1):
                """
                To get the number of proper arrangements of b blocks with
                first tower height less than or equal to h and w or fewer tower,
                start by calculating the number of such arrangements with first 
                tower height of exactly h.
                
                Since the h blocks are taken up by the first tower, we have
                b - h blocks remaining to make proper arrangements no higher than 
                h and no wider than w - 1. So,
                """
                b_remaining = b-h;
                L[b, h, w] = L[b_remaining, min(h, b_remaining), min(w - 1, b_remaining)]
                """
                Then we add in the proper arrangements with b blocks, w or fewer 
                towers with first tower height less than or equal to h - 1
                """
                if (b, h-1, w) in L:
                    L[b, h, w] += L[b, h - 1, w]
    return L


def test(n):
    r1 = p1.problem1(n)
    r2 = problem2(n, n)
    for b, h in p1:
        #print("b: %d, h: %d, p1: %d, p2: %d" % (b, h, p1[b, h], p2[b, h, b]))
        assert(r1[b, h] == r2[b, h, b])
    print("Success for n == %d", n)

#r = problem2(200, 200)
