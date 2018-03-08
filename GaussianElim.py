import sympy as sp
import numpy as np
import random
random = random.Random(1)


def L(row):
    for i in range(0, len(row)):
        if row[i] != 0:
            return i
    return None


def addRowIntoRow(M, dst, src, scale):
    M.zip_row_op(dst, src, lambda dst_val, src_val: dst_val + scale * src_val)


def turnFirstNonZeroToOne(M, c, l, row_i):
    divisor = M[row_i, l]
    M.row_op(row_i, lambda val, col: val / divisor)
    c.row_op(row_i, lambda val, col: val / divisor)


def zeroOtherRowsAt(M, c, l, row_i):
    for i in range(M.rows):
        if i != row_i:
            scale = -M[i, l]
            addRowIntoRow(M, i, row_i, scale)
            addRowIntoRow(c, i, row_i, scale)


def swapUpBigger(row_i, col_i, M, c):
    for row in range(row_i, M.rows):
        if abs(M[row, col_i]) > abs(M[row_i, col_i]):
            M.row_swap(row_i, row)
            c.row_swap(row_i, row)


def firstColWithNonZeroDownAndRightOf(M, row_i, col_i):
    while col_i < M.cols:
        for row in range(row_i, M.rows):
            if M[row, col_i] != 0:
                return col_i
        col_i += 1
    return col_i


def GaussianEliminate(M, c):
    if len(M.shape) != 2 or len(c.shape) != 2 or M.rows != c.rows:
        print("A and c need to be 2d Sympy Matrices. c.shape[0] must equal A.shape[1]")
        return
    m = M.rows
    n = M.cols
    col_i = 0
    for row_i in range(0, m):
        col_i = firstColWithNonZeroDownAndRightOf(M, row_i, col_i)
        if col_i >= n:
            return
        swapUpBigger(row_i, col_i, M, c)
        col_i = L(M.row(row_i))
        if col_i is None:
            return
        turnFirstNonZeroToOne(M, c, col_i, row_i)
        zeroOtherRowsAt(M, c, col_i, row_i)


test_counter = 0


def generate_random_matrix(sq, sparsity):
    rows = random.randint(1, 10)
    if sq:
        cols = rows
    else:
        cols = random.randint(1, 10)
    M = sp.zeros(rows, cols)
    for i in range(0, rows):
        for j in range(0, cols):
            if random.random() > sparsity:
                M[i, j] = random.randint(-10, 10)
    return M

def test(sparsity, sq):
    global test_counter
    for test_i in range(0, 50):
        test_counter += 1
        print(test_counter)
        M = generate_random_matrix(sq, sparsity)
        M_orig = M.copy()
        M_rref = M.rref()[0]
        c = sp.eye(M.rows, M.cols)
        GaussianEliminate(M, c)
        assert(M == M_rref)
        if sq:
            try:
                M_inv = M_orig.inv()
                assert(c == M_inv)
            except:
                print("matrix not invertable")


def run_tests():
    for sparsity in np.arange(0, 1, 0.1):
        test(sparsity, False)
        test(sparsity, True)


run_tests()