# Javier Vazquez
# Grid Printer
# Date
# Description:

import os
import linearClassifierClass
import pandas as pd
import numpy as np



def main():
    lc = linearClassifierClass.linearClassifier()
    file = "Assignment_4_to_Pandas.xlsx"

    # Training Data - Begins
    print("\n\033[1mTraining Data\033[0m")
    sheet = 0
    cols = "A:O"
    skip = 0
    X = lc.loadData(file, sheet, cols, skip)
    print(X)

    # Tb for Binary Classifier
    cols = "P"
    Tb = lc.loadData(file, sheet, cols, skip)

    Wb = lc.W(X, Tb)
    print("\n\033[1mW - Binary Classifier\033[0m")
    print(Wb)
    print(Wb.shape)

    # T6c for 6-Class Classifier
    cols = "Q"
    T6c = lc.loadData(file, sheet, cols, skip)
    T6c = lc.kesler(T6c)
    W = lc.W(X, T6c)

    print("\n\033[1mW - 6-Class Classifier\033[0m")
    print(W)
    print(W.shape)

    # Training Data - Ends


    # Testing Data - Begins
    print("\n\033[1mTesting Data\033[0m")
    sheet = 2
    cols = "A:O"
    skip = 3
    X = lc.loadData(file, sheet, cols, skip)

    print(X)

    # TODO
    # Testing Data - Ends


if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()