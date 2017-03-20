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
        return Txd

    def binaryClassClassifier(self, W_XaT):
        classifierArray = np.sign(W_XaT)
        return classifierArray

    def sixClassClassifier(self, W_XaT):
        m, n = W_XaT.shape
        m = np.arange(m)
        n = np.argmax(W_XaT, axis=1)
        W_XaT[m,n] = 1
        classifierArray = np.sign(W_XaT)
        return classifierArray

    def confusionBinaryMatrix(self, original, generated):
        table = np.hstack((original, generated))
        np.set_printoptions(edgeitems=10)
        tp = table[np.where((table == (1,1)).all(axis=1))]
        fn = table[np.where((table == (1,-1)).all(axis=1))]
        tn = table[np.where((table == (-1,-1)).all(axis=1))]
        fp = table[np.where((table == (-1,1)).all(axis=1))]
        tp, n = tp.shape
        fn, n = fn.shape
        tn, n = tn.shape
        fp, n = fp.shape
        return tp, fn, tn, fp





    def dfToExcel(self, var1, var2, var3, fileName):
        writer = pd.ExcelWriter(fileName)
        var1 = pd.DataFrame(var1)
        var2 = pd.DataFrame(var2)
        var3 = pd.DataFrame(var3)
        var1.to_excel(writer, "Tb")
        var2.to_excel(writer, "Confusion")
        var3.to_excel(writer, "True-False")
        writer.save()
        print("Variables to", fileName)

if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")