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
    cols = "A:O"
    X = lc.loadData(file, cols)
    cols = "P"
    T = lc.loadData(file, cols)
    W, W_XaT = lc.W_XaT(X, T)
    print("\n\033[1mW\033[0m")
    print(W)
    print(W.shape)
    print("\n\033[1mW_XaT\033[0m")
    print(W_XaT)
    print(W_XaT.shape)
    classifierArray = lc.classifier(W_XaT)
    print(classifierArray)
    print(classifierArray.shape)
    print(classifierArray == T)
    lc.dfToExcel(W, W_XaT, classifierArray)


if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()