import pandas as pd

def odds(p):
    return p / (1-p)

def getInfo(pA, pAGvnB):
    return {
        'pAGvnB,pA': (pAGvnB, pA),
        'oddsA': odds(pA),
        'oddsAGvnB': odds(pAGvnB),
        'oddsRatio': odds(pAGvnB)/ odds(pA)
    }

def pairsToDf(pairs):
    info = [getInfo(pA, pAGvnB) for pAGvnB, pA in pairs]
    df = pd.DataFrame(info)
    return df.set_index('pAGvnB,pA')


pairs1 = [
    (0.10, 0.05),
    (0.95, 0.90),
    (0.60, 0.20),
    (0.80, 0.40),
    (0.40, 0.20),
    (0.80, 0.60)
]

pairs2 = [
    (0.12, 0.08),
    (0.27, 0.23),
    (0.52, 0.48),
    (0.77, 0.73),
    (0.92, 0.88),
]

pairs3 = [
    (0.10, 0.05),
    (0.95, 0.90),
    (0.15, 0.05),
    (0.95, 0.85),
    (0.20, 0.05),
    (0.95, 0.80),
]

df1 = pairsToDf(pairs1)
df2 = pairsToDf(pairs2)
df3 = pairsToDf(pairs3)

