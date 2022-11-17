#!/usr/bin/env python3

import pandas as pd

from src.system import *

# MODEL CONSTANTS

PATH = "data/SPSectors.txt"

# how risk averse an investor is, gamma >= 0
GAMMA = [1, 2, 3, 4, 5, 10]

# estimation window; how long we will estimate for
M = 120

SPSectorsPandas = pd.read_csv(PATH, delim_whitespace = True)

# clean data by removing the date column
SPSectors = SPSectorsPandas.to_numpy()[:, 1:]

COLS = SPSectors.shape[1]

riskFreeReturns = SPSectors[:, 0] # risk-free asset column
riskyReturns = SPSectors[:, 1:COLS] # risky asset column, includes risk factor

def main():
    SYSTEM = System(riskFreeReturns, riskyReturns, M)

    sr = SYSTEM.getSharpeRatios(GAMMA)

    for key, value in sr.items():
        print(key, value)

if __name__ == "__main__":
    main()