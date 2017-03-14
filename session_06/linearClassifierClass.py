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
        return W, W_XaT

    #TODO - Transform Type using Kesler
    def Kesler(self, T):
        pass
    #b[np.where(a == 9),:] = [99,99,99,99]


    def classifier(self, W_XaT):
        classifierArray = np.sign(W_XaT)
        return classifierArray

    def dfToExcel(self, W, W_XaT, classifierArray):
        writer = pd.ExcelWriter("W_W_XaT.xlsx")
        W = pd.DataFrame(W)
        W_XaT = pd.DataFrame(W_XaT)
        classifierArray = pd.DataFrame(classifierArray)
        W.to_excel(writer, "W")
        W_XaT.to_excel(writer, "W_XaT")
        classifierArray.to_excel(writer, "classifierArray")
        writer.save()
        print("Variables to W_W_XaT.xlsx")



if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")