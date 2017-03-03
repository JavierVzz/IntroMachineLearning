import read_MNIST_Class, XZCVPR, os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    mnist = read_MNIST_Class.read_MNIST()
    # a = int(input("Negative Digit : "))
    # b = int(input("Positive Digit : "))
    # print("Negative Digit : -5")
    # print("Positive Digit : 9")
    a = -5
    b = 9
    # X = mnist.load_mnist('training', digits=[a,b])
    # mnist.printPlot(X)
    # mnist.vectortoimg(X[4], X[-1])
    X = np.array([[72., 101., 94.], [50., 96., 70.], [14., 79., 10.], [8., 70., 1.]], np.float64)
    xzcvpr = XZCVPR.XZCVPR()
    X_bar = xzcvpr.X(X)
    # print(X_bar)
    Z = xzcvpr.Z(X, X_bar)
    # mnist.printPlot(Z)
    # print(Z)
    C = xzcvpr.C(Z)
    # mnist.printPlot(C)
    # mnist.vectortoimg(C[4], C[-1])
    # print("C.shape")
    # print(C.shape)
    # mnist.printPlot(C)
    w, V = xzcvpr.V(C)
    print("V")
    print(V)
    # print(np.dot(V[0,:],V[1,:]))
    # print(np.linalg.norm(V[0]))
    # print(np.linalg.norm(V[1]))
    # print(V)
    # row = V[0,:]
    # col = V[:,0]
    # print(w)
    # print(V)
    # print(np.dot(C, row) / (w[0] * row))
    # print(np.dot(C, col) / (w[0] * col))
    # w = np.flipud(w)
    V1 = np.flipud(V.T)

    # print("V.shape")
    # print(V.shape)
    # row = V[0,:]
    # v = np.dot(C,row)/(w[0]*row)
    # print(v.shape)
    # print(v)
    P = xzcvpr.P(Z,V1)
    print("P")
    print(P)
    R = xzcvpr.P(P,V1)
    print("R")
    print(R)








if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()