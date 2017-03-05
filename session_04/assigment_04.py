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
    X = mnist.load_mnist('training', digits=[a,b])
    # mnist.printPlot(X, label="X")
    # mnist.vectortoimg(X[4], X[-1], label="X")
    # X = np.array([[72., 101., 94.], [50., 96., 70.], [14., 79., 10.], [8., 70., 1.]], np.float64)
    xzcvpr = XZCVPR.XZCVPR()
    X_bar = xzcvpr.X(X)
    print("X_bar")
    print(X_bar.shape)
    print(X_bar)
    Z = xzcvpr.Z(X, X_bar)
    # mnist.printPlot(Z, label="Z")
    print("Z")
    print(Z)
    C = xzcvpr.C(Z)
    print("C")
    print(C)
    # mnist.printPlot(C, label="C")
    mnist.checkCplot(C, label="C")
    # mnist.vectortoimg(C, label="C")
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
    print(V.shape)
    # print(np.dot(C, row) / (w[0] * row))
    # print(np.dot(C, col) / (w[0] * col))
    # print(np.dot(C, col) == (w[0] * col))
    w = np.flipud(w)
    V = np.flipud(V.T)
    # print(V1[0,:] == V[:,783])
    # print(V[0,:])
    # print(V[1,:])
    V2d= V[0:2, :].copy()
    # print(V[0,:] == V2d[0,:])
    # print(V[0,:] is V2d[0,:])
    # df = pd.DataFrame(V[0,:])
    # df.to_excel("V1.xlsx", sheet_name="V1")
    # df = pd.DataFrame(V[1,:])
    # df.to_excel("V2.xlsx", sheet_name="V2")
    # row = V1[0,:]
    # print(np.dot(C,row) == (w1[0]*row))
    # print("V.shape")
    # print(V.shape)

    # print(v.shape)
    # print(v)
    P = xzcvpr.P(Z,V2d)
    print("P")
    print(P)
    print(P.shape)
    print(np.mean(P,axis=0))
    print(np.where(P >= 0))

    # Xrec = xzcvpr.Xrec(P, V2d, X_bar)
    # print(Xrec)
    # mnist.printPlot(Xrec, label="Xrec")
    # mnist.vectortoimg(Xrec[4], Xrec[-1], label="Xrec")

    # R = xzcvpr.R(P,V,Z)
    # print("R")
    # print(R)









if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()