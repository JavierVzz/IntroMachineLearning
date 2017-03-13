import os
import numpy as np
import pandas as pd

class XZCVPR():

    def __init__(self):
        pass

    def X(self, X):
        X_bar = np.mean(X,axis=0)
        # df = pd.DataFrame(X_bar)
        # df.to_excel("X_Bar.xlsx", sheet_name="X_Bar")
        return X_bar

    def Z(self, X, X_bar):
        Z = X - X_bar
        return Z

    def C(self, Z):
        C = np.cov(Z, rowvar=False)
        return C

    def V(self, C):
        w, V = np.linalg.eigh(C)
        w = np.flipud(w)
        V = np.flipud(V.T)
        V = V[0:2, :].copy()
        # df = pd.DataFrame(V)
        # df.to_excel("V.xlsx", sheet_name="V")
        # df = pd.DataFrame(X_bar)
        # df.to_excel("X_Bar.xlsx", sheet_name="X_Bar")
        return w, V

    def P(self, Z, V):
        P = np.dot(Z,V.T)
        return P

    def R(self, P, V, Z):
        R = np.dot(P,V) - Z
        return R

    # According to Lecture_1_4, pg 83, bullet 3
    def Xrec(self, P, V2d, X_bar):
        Xrec = np.dot(P, V2d) + X_bar
        return Xrec

    def mup_mun(self, P, T, labelp, labeln):
        mup = np.mean(P[T==labelp], axis=0)
        mun = np.mean(P[T==labeln], axis=0)
        return mup, mun

    def cp_cn(self, P, T, labelp, labeln):
        cp = np.cov(P[T==labelp], rowvar = False)
        cn = np.cov(P[T==labeln], rowvar = False)
        return cp, cn

    def min_max(self, P, T, label):
        min = np.min(P[T==label])
        max = np.max(P[T==label])
        return min, max

    def hist(self, P, T, label):
        P = P[T == label]
        # print(P[:,0])
        H, xedges, yedges = np.histogram2d(P[:,0],P[:,1], bins=[25, 25])
        # writer = pd.ExcelWriter("Pn_histogram_2d.xlsx")
        # h = pd.DataFrame(H)
        # xd = pd.DataFrame(xedges)
        # yd = pd.DataFrame(yedges)
        # h.to_excel(writer,"H")
        # xd.to_excel(writer,"x_edges")
        # yd.to_excel(writer,"y_edges")
        # writer.save()
        return H, xedges, yedges

    def xlabel(self, X, T, label):
        xp = X[T==label]
        return xp, xp[np.argmax(np.sum(xp, axis=1)),:]







if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")