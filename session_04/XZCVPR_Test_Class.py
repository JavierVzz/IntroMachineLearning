import os, struct
import matplotlib as plt
import pylab
import numpy as np
from array import array as pyarray

class XZCVPR_Test():
    def __init__(self):
        pass

    def test_X(self, X):
        print("\033[1m\nX TEST\033[0m")
        print("X shape", X.shape)
        print("X min", np.amin(X))
        print("X max", np.amax(X))
        self.vectortoimg(X[4], X[-1], label="X")

    def test_Z(self, Z, X_bar):
        print("\033[1m\nZ TEST\033[0m")
        print("X_bar shape", X_bar.shape)
        print("X_bar min", np.amin(X_bar))
        print("X_bar max", np.amax(X_bar))
        self.printPlot(Z, label="Z")
        print("Z shape", Z.shape)
        print("Z min", np.amin(Z))
        print("Z max", np.amax(Z))

    def vectortoimg(self, *args, width=28, size=1, label):
        n = len(args)
        fig = plt.pyplot.figure(label)
        for i, arg in enumerate(args):
            plt.pyplot.subplot(1,n,i+1)
            plt.pyplot.imshow(arg.reshape(width, width), interpolation="None", cmap=plt.pyplot.cm.gray)
            plt.pyplot.axis("off")
        fig.tight_layout(pad=0)
        fig.set_size_inches(w=n*size, h=size)
        plt.pyplot.show()

    def printPlot(self, X, label):
        fig = plt.pyplot.figure(label)
        plt.pyplot.imshow(X[20].reshape(28, 28), interpolation='None', cmap=plt.pyplot.cm.gray)
        plt.pyplot.show()

if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")