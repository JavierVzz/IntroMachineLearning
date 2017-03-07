import read_MNIST_Class, XZCVPR, XZCVPR_Test_Class, os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    mnist = read_MNIST_Class.read_MNIST()
    xzcvpr = XZCVPR.XZCVPR()
    test = XZCVPR_Test_Class.XZCVPR_Test()
    # a = int(input("Negative Digit : "))
    # b = int(input("Positive Digit : "))
    # print("Negative Digit : 5")
    # print("Positive Digit : 9")
    a = 5
    b = 9
    X = mnist.load_mnist('training', digits=[a,b])

    test.test_X(X)

    # X = np.array([[72., 101., 94.], [50., 96., 70.], [14., 79., 10.], [8., 70., 1.]], np.float64)

    X_bar = xzcvpr.X(X)
    Z = xzcvpr.Z(X, X_bar)

    print("Z")
    print(Z)
    test.test_Z(Z, X_bar)

    C = xzcvpr.C(Z)
    print("C")
    print(C)
    test.test_C(C)

    w, V = xzcvpr.V(C)
    print("V")
    w = np.flipud(w)
    V = np.flipud(V.T)
    V2d= V[0:2, :].copy()
    print(V2d)
    test.test_V(V2d)

    P = xzcvpr.P(Z,V2d)
    # print("P")
    # print(P)
    print(P.shape)
    # print(np.mean(P,axis=0))
    # print(np.where(P >= 0))

    print("\n\033[1mmup\033[0m")
    mup1, mup2 = xzcvpr.mup(P)
    print(mup1)
    print(mup2)

    print("\n\033[1mmun\033[0m")
    mun1, mun2 = xzcvpr.mun(P)
    print(mun1)
    print(mun2)

    print("\n\033[1mcp\033[0m")
    p0, p1 = xzcvpr.cp(P)
    print(p0.shape)
    print(p1.shape)



    


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