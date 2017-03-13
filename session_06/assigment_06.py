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
    print(T)

if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()