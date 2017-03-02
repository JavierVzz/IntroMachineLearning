import os
import numpy as np
import pandas as pd

class XZCVPR():

    def __init__(self):
        pass

    def X(self, X):
        # np.savetxt("X.txt", X)
        # df =pd.DataFrame(X)
        # df.to_excel("XZCVPR.xlsx", sheet_name="X")
        X_bar = np.mean(X,axis=0)
        # df = pd.DataFrame(X_bar)
        # np.savetxt("X_bar.txt", X_bar)
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
        # return np.fliplr(V)
        return w, V

    def P(self, Z, V):
        P = np.dot(Z,V.T)
        return P

    def R(self, Z, V):
        P = np.dot(Z,V.T)
        return P



if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")