import os
import pandas as pd
import numpy as np


class linearClassifier():

    def __init__(self):
        pass

    def loadData(self, file, cols):
        """Load an excel file to df"""
        df = pd.read_excel(io=file, sheetname=0, header=0, parse_cols=cols).values
        return df

    def W_XaT(self,X, T):
        m, n = X.shape
        Xa = np.ones((m, 1))
        XaX = np.hstack((Xa, X))
        W = np.dot(np.linalg.pinv(XaX), T)
        W_XaT = np.dot(XaX, W)
        return W_XaT

    def classifier(self, W_XaT):
        classifierArray = np.sign(W_XaT)
        return classifierArray


if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")