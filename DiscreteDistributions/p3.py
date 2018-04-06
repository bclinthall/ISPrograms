"""
Now we are going to play a game. There are W players and we have n blocks.
We take each block and randomly assign it to a player (each block has an equal
chance of getting assigned to any player). Then we have each player build a tower
with their blocks and we arrange the towers into a proper arrangement.

What is the expected height of the ith tower?
"""
import math
import time
from scipy.special import comb

#from DiscreteDistributions import p2
import matplotlib.pyplot as plt
prev_n = 0
prev_w = 0
prev_L = {}

def get_L(n, W):
    global prev_n, prev_w, prev_L
    if n == prev_n and W == prev_w:
        L = prev_L
    else:
        L = p2.problem2(n, W)
    prev_n = n
    prev_w = W
    prev_L = L
    return L

def exp_dist_h_i(n, W):
    #L = get_L(n, W)
    L = None
    total_proper_arrangements = pts_in_simplex(W, n)

    exps = []
    for i in range(1, W+1):
        exps.append(expected_h_i(L, n, W, i, total_proper_arrangements))
    plt.plot(exps)
    plt.savefig("n%d_w%d.png" % (n, W))
    plt.show()
    return exps


def expected_h_i(L, n, W, i, tot):
    """
    :param n: number of blocks
    :param W: max width of arrangement
    :param i:
    :return: The expected height of the ith tower for proper arrangements
    of n blocks into no more than W towers
    """
    # L[b, h, w] is the number of proper arrangements of b blocks with
    # first tower height less than or equal to h and w or fewer tower.

    print("Calculating expectation for the %dth tower" % i)

    '''
    Since all previous towers must be at least as tall as the ith, 
    there is a max height it could be. 
    '''
    max_height = math.floor(n/i)
#    max_height = n
    exp = 0
    arr = 0
    for h in range(0, max_height + 1):
        a = arrangements_i(n, W, L, i, h)
        exp += h * a
        arr += a
    if arr == 0:
        return exp
    return exp/arr

def get_arrangementsBad(L, b, h, w):
    if b == 0:
        return 1
    if w > b:
        w = b
    if h > b:
        h = b
    if w * h < b:
        return 0
    else:
        return L[b, h, w]


facts = [1, 1]
max_fact = 1
max_fact_ans = 1
def fact(n):
    global max_fact, max_fact_ans
    if max_fact < n:
        for i in range(max_fact + 1, n+1):
            max_fact_ans *= i
            facts.append(max_fact_ans)
        max_fact = n
    return facts[n]


def pts_in_simplex(dimensions, component_sum):
    if dimensions <= 0:
        return 0
    if component_sum <= 0:
        return 0
    n = component_sum + dimensions - 1
    k = component_sum - 1
    return fact(n) // (fact(k) * fact(n-k))
    # p = dimensions ** component_sum
    # dups = fact(dimensions) * fact(component_sum)
    # return p / dups


def get_arrangements(L, b, h, w):
    total_pts = pts_in_simplex(w, b)
    pts_with_a_dimension_outside_h = w * pts_in_simplex(w, b-h-1)
    if total_pts < pts_with_a_dimension_outside_h:
        return 0
    else:
        return total_pts - pts_with_a_dimension_outside_h


def arrangements_i(n, W, L, i, h):
    """
    :param W: max width
    :param L: The data table
    :param i: Tower rank
    :param h: height
    :return: The number of proper arrangements of max width
    W where the ith tower is h blocks tall.
    """

    '''
    There are n blocks total. h of them are used building the ith tower.
    (i-1)*h of them make a kind of foundation for the first i-1 towers.
    There are b-i*h blocks remaining to work with.
    
    Some of them may be used to build towers on top of the foundation left of 
    i. Those towers can be as high as they please, but there can be no 
    more than i-1 of them.
    
    Rest rest will be used to build towers to the right of the ith. Those
    can be no taller than h, and there can be no more than W-i of them.
    
    We will start by putting none of the remaining blocks to the right of i, 
    and cycle through till they are all to the right of i (or until there 
    are h * W-i of them to the right of i). 
    '''
    remaining_blocks = n - i*h
    arrangements = 0
    max_right = (W-i) * h
    for right_blocks in range(0, min(remaining_blocks, max_right) + 1):
        left_blocks = remaining_blocks - right_blocks
        left_arrangements = get_arrangements(L, left_blocks, left_blocks, i-1)
        right_arrangements = get_arrangements(L, right_blocks, h, W-i)
        arrangements += left_arrangements * right_arrangements
    return arrangements


start = time.process_time();

n = 10000
w = 100
#L = get_L(n, w)
L = None
i = 3

#r = arrangements_i(n, w, L, i, 6)
r = exp_dist_h_i(n, w)
print("time elapsed", time.process_time() - start)

print([round(p) for p in r])
#print (r)