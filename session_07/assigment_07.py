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
    file = "Assignment_4_to_Pandas.xlsx"

    # Training Data - Begins
    print("\n\033[1mTraining Data\033[0m")
    sheet = 0
    cols = "A:O"
    skip = 0
    Xtrain = lc.loadData(file, sheet, cols, skip)
    # print(X)

    # Tb for Binary Classifier
    cols = "P"
    Tb = lc.loadData(file, sheet, cols, skip)

    Wb = lc.W(Xtrain, Tb)
    print("\n\033[1mW - Binary Classifier\033[0m")
    print(Wb)
    print(Wb.shape)

    # T6c for 6-Class Classifier
    cols = "Q"
    T6c = lc.loadData(file, sheet, cols, skip)
    T6ck = lc.kesler(T6c)
    W6c = lc.W(Xtrain, T6ck)

    print("\n\033[1mW - 6-Class Classifier\033[0m")
    print(W6c)
    print(W6c.shape)

    # Training Data - Ends


    # Testing Data - Begins
    print("\n\033[1mTesting Data\033[0m")
    sheet = 2
    cols = "A:O"
    skip = 3
    Xtest = lc.loadData(file, sheet, cols, skip)

    print("\n\033[1mW - Binary Classifier\033[0m")

    # Tb for Binary Classifier

    fb = lc.W_XaT(Xtest, Wb)
    fbc = lc.binaryClassClassifier(fb)
    print(fbc)

    # Tb for 6-Class Classifier
    print("\n\033[1mW - 6-Class Classifier\033[0m")
    t6c = lc.W_XaT(Xtest, W6c)
    t6cb = lc.sixClassClassifier(t6c)
    invKeslet = lc.invKesler(t6cb)
    print(invKeslet)

    # lc.dfToExcel(fbc, invKeslet, "classifiers.xlsx")

    # Testing Data - Ends

    # Confusion Matrix Starts
    # Binary Classifier Confusion Matrix (-1=Fail, +1=Pass)
    print("\n\033[1mW - Confusion Binary Class Matrix\033[0m")
    confusion2 = lc.W_XaT(Xtrain, Wb)
    confusion2binary = lc.binaryClassClassifier(confusion2)

    # lc.dfToExcel(Tb, confusion2binary, Tb==confusion2binary, "confusionBinary.xlsx")
    tp, fn, tn, fp = lc.confusionBinaryMatrix(Tb, confusion2binary)

    print("True Positive:", tp)
    print("False Negative:", fn)
    print("True Negative:", tn)
    print("False Positive:", fp)
    print("Sum:", np.sum([tp, fn, tn, fp]))
    print("Accuracy:", (tp + tn) / (tp + fn + fp + tn))
    print("Sensitivity:", tp / (tp + fn))
    print("Specificity:", tn / (fp + tn))
    print("PPV:", tp / (fp + tp))

    print("\n\033[1mW - Confusion 6th Class Matrix\033[0m")

    print("Original")
    print(T6c)
    t6Compare = lc.W_XaT(Xtrain, W6c)
    t6Compare = lc.sixClassClassifier(t6Compare)
    t6Compare = lc.invKesler(t6Compare)
    print("Generated")
    print(t6Compare)
    lc.confusion6thMatrix(T6c, t6Compare)

if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()