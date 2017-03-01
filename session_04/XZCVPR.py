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
        row = V[0, :]
        col = V[:, 0]
        test = np.dot(C,row)/(w[0]*row)
        # test = np.dot(C, col) / (w[0] * col)
        return test



if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")