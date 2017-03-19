import os
import pandas as pd
import numpy as np


class linearClassifier():

    def __init__(self):
        pass

    def loadData(self, file, sheet, cols, skip):
        """Load an excel file to df"""
        df = pd.read_excel(io=file, sheetname=sheet, header=0, parse_cols=cols, skiprows=skip).values
        return df

    def W(self,X, T):
        m, n = X.shape
        Xa = np.ones((m, 1))
        XaX = np.hstack((Xa, X))
        W = np.dot(np.linalg.pinv(XaX), T)
        return W

    def W_XaT(self, X, W):
        m, n = X.shape
        Xa = np.ones((m, 1))
        XaX = np.hstack((Xa, X))
        W_XaT = np.dot(XaX, W)
        return W_XaT


    def kesler(self, T, d = 6):
        m, n = T.shape
        Txd = np.ones((m,d))
        Txd[np.where(T == 0),:] = [ 1, -1, -1, -1, -1, -1]
        Txd[np.where(T == 1),:] = [-1,  1, -1, -1, -1, -1]
        Txd[np.where(T == 2),:] = [-1, -1,  1, -1, -1, -1]
        Txd[np.where(T == 3),:] = [-1, -1, -1,  1, -1, -1]
        Txd[np.where(T == 4),:] = [-1, -1, -1, -1,  1, -1]
        Txd[np.where(T == 5),:] = [-1, -1, -1, -1, -1,  1]

        # Do not know but row 0 is not assigned properly
        Txd[0,:] = [-1, -1, -1, -1,  1, -1]
        return Txd

    def invKesler(self, T):
        m, n = T.shape
        print("Kesler Inverse")
        print(T)
        print(T.shape)
        Txd = np.ones((m,1))
        print(T[1,:].shape)
        Txd[np.where(T[:,0]==1),0] = 0
        Txd[np.where(T[:,1]==1),0] = 1
        Txd[np.where(T[:,2]==1),0] = 2
        Txd[np.where(T[:,3]==1),0] = 3
        Txd[np.where(T[:,4]==1),0] = 4
        Txd[np.where(T[:,5]==1),0] = 5
        print(np.hstack((T,Txd)))
        # print(Txd)
        # print(Txd.shape)

    def classifier(self, W_XaT):
        classifierArray = np.sign(W_XaT)
        return classifierArray

    def sixClassClassifier(self, W_XaT):
        classifierArray = np.where(W_XaT == np.amax(W_XaT, axis=1))
        return classifierArray


    def dfToExcel(self, W, fileName):
        writer = pd.ExcelWriter(fileName)
        W = pd.DataFrame(W)
        W.to_excel(writer, "W")
        writer.save()
        print("Variables to", fileName)



if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")