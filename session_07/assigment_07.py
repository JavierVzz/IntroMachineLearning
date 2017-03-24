# Javier Vazquez
# Car Data
# Date: March 23, 2017
# Description: Classifier of how people buy cars

import os
import linearClassifierClass
import pandas as pd
import numpy as np

def main():
    lc = linearClassifierClass.linearClassifier()
    file = "Car_Data.xlsx"

    # Training Data - Begins
    print("\n\033[1mTraining Data\033[0m")
    sheet = 0
    cols = "A:G"
    skip = 1
    Xtrain = lc.loadData(file, sheet, cols, skip)
    price = lc.kesler4Labels(Xtrain[:,0])
    maintenance = lc.kesler4Labels(Xtrain[:,1])
    doors = lc.kesler4LabelsIntStr(Xtrain[:,2])
    persons = lc.kesler3LabelsIntStr(Xtrain[:,3])
    trunk = lc.kesler3Labels(Xtrain[:,4])
    print(price)
    print(maintenance)
    print(doors)
    print(persons)
    print(trunk)

    # print(np.unique(Xtrain[:,2]))



if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()