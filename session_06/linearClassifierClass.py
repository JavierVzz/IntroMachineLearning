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
        Txd = np.ones((m,1))
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

    def confusion6thMatrix(self, original, generated):
        table = np.hstack((original, generated))
        np.set_printoptions(edgeitems=10)
        tp00 = table[np.where((table == (0,0)).all(axis=1))]
        tp01 = table[np.where((table == (0,1)).all(axis=1))]
        tp02 = table[np.where((table == (0,2)).all(axis=1))]
        tp03 = table[np.where((table == (0,3)).all(axis=1))]
        tp04 = table[np.where((table == (0,4)).all(axis=1))]
        tp05 = table[np.where((table == (0,5)).all(axis=1))]
        
        tp10 = table[np.where((table == (1,0)).all(axis=1))]
        tp11 = table[np.where((table == (1,1)).all(axis=1))]
        tp12 = table[np.where((table == (1,2)).all(axis=1))]
        tp13 = table[np.where((table == (1,3)).all(axis=1))]
        tp14 = table[np.where((table == (1,4)).all(axis=1))]
        tp15 = table[np.where((table == (1,5)).all(axis=1))]

        tp20 = table[np.where((table == (2,0)).all(axis=1))]
        tp21 = table[np.where((table == (2,1)).all(axis=1))]
        tp22 = table[np.where((table == (2,2)).all(axis=1))]
        tp23 = table[np.where((table == (2,3)).all(axis=1))]
        tp24 = table[np.where((table == (2,4)).all(axis=1))]
        tp25 = table[np.where((table == (2,5)).all(axis=1))]

        tp30 = table[np.where((table == (3,0)).all(axis=1))]
        tp31 = table[np.where((table == (3,1)).all(axis=1))]
        tp32 = table[np.where((table == (3,2)).all(axis=1))]
        tp33 = table[np.where((table == (3,3)).all(axis=1))]
        tp34 = table[np.where((table == (3,4)).all(axis=1))]
        tp35 = table[np.where((table == (3,5)).all(axis=1))]

        tp40 = table[np.where((table == (4,0)).all(axis=1))]
        tp41 = table[np.where((table == (4,1)).all(axis=1))]
        tp42 = table[np.where((table == (4,2)).all(axis=1))]
        tp43 = table[np.where((table == (4,3)).all(axis=1))]
        tp44 = table[np.where((table == (4,4)).all(axis=1))]
        tp45 = table[np.where((table == (4,5)).all(axis=1))]


        tp50 = table[np.where((table == (5,0)).all(axis=1))]
        tp51 = table[np.where((table == (5,1)).all(axis=1))]
        tp52 = table[np.where((table == (5,2)).all(axis=1))]
        tp53 = table[np.where((table == (5,3)).all(axis=1))]
        tp54 = table[np.where((table == (5,4)).all(axis=1))]
        tp55 = table[np.where((table == (5,5)).all(axis=1))]

        print("Counts 0")
        print(tp00.shape, tp01.shape, tp02.shape, tp03.shape, tp04.shape, tp05.shape)
        print("Counts 1")
        print(tp10.shape, tp11.shape, tp12.shape, tp13.shape, tp14.shape, tp15.shape)
        print("Counts 2")
        print(tp20.shape, tp21.shape, tp22.shape, tp23.shape, tp24.shape, tp25.shape)
        print("Counts 3")
        print(tp30.shape, tp31.shape, tp32.shape, tp33.shape, tp34.shape, tp35.shape)
        print("Counts 4")
        print(tp40.shape, tp41.shape, tp42.shape, tp43.shape, tp44.shape, tp45.shape)
        print("Counts 5")
        print(tp50.shape, tp51.shape, tp52.shape, tp53.shape, tp54.shape, tp55.shape)



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