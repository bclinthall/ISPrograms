import numpy as np
import matplotlib.pyplot as plt
# Say every word token in an n word corpus has an equal probability of
# being any word in a k word language. Lets generate some data sets.

def eq_word_prob(n, k):
    occurances = np.zeros(k)
    for i in range(0, n):
        num = np.random.randint(k)
        occurances[num] += 1
    occurances = np.sort(occurances)
    occurances = occurances[::-1]
    print(occurances)
    plt.plot(occurances)
    plt.show()

def zipf_prob(n, k, gamma):
    alpha = 0
    for i in range(1, n + 1):
        alpha += i ** -gamma
    occurances = [1/(alpha * i**gamma) for i in range(1, k+1)]
    plt.plot(occurances)

def plot_probs(n, k, gamma):
    eq_word_prob(n, k)
    #zipf_prob(n, k, gamma)
    plt.show()

#plot_probs(100000, 1000, 1)


# Probability that any given token is of type rank r
def token_prob(n, k, gamma):
    alpha = 0
    for i in range(1, n + 1):
        alpha += i ** -gamma

    uniform = np.ones(k) * 1/k
    zipf = [1/(alpha * i**gamma) for i in range(1, k+1)]
    return uniform, zipf

#uniform, zipf = token_prob(100000, 1000, 3)
#plt.plot(uniform)
#plt.plot(zipf)
#plt.show()


def harmonic_sum(pop_size, exp):
    sum = 0
    for i in range(0, pop_size + 1):
        sum += i**-exp

def zipf_freq_at_rank(rank, pop_size, exp):
    hns = harmonic_sum(pop_size, rank)
    return


from mpl_toolkits.mplot3d import Axes3D


def plot_valid(B):
    H = B
    W = B
    valid = []
    step = 1
    for b in range(1, B+1, step):
        for w in range(1, W+1, step):
            for h in range(1, H+1, step):
                if h <= b and w <= b and w < b/h:
                    valid.append((b, h, w))
    bs = [p[0] for p in valid]
    hs = [p[1] for p in valid]
    ws = [p[2] for p in valid]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(bs, hs, ws)
    ax.set_xlabel('b')
    ax.set_ylabel('h')
    ax.set_zlabel('w')
    plt.show()

#plot_valid(50)

