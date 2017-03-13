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

    X, T = mnist.load_mnist('training', digits=[a,b])
    [[labeln, labelp], [Nn,Np]] = np.unique(T, return_counts= True)

    # test.test_X(X)

    X_bar = xzcvpr.X(X)

    Z = xzcvpr.Z(X, X_bar)
    # print("Z")
    # print(Z)
    # test.test_Z(Z, X_bar)

    C = xzcvpr.C(Z)
    # print("C")
    # print(C)
    # test.test_C(C)

    w, V = xzcvpr.V(C)
    # print("V")
    # print(V)
    # test.test_V(V)

    P = xzcvpr.P(Z,V)
    print("P")
    # print(P)
    # test.test_P(P, V, X_bar)

    print("\n\033[1mNp and Nn\033[0m")
    print("Np", Np)
    print("Nn", Nn)

    print("\n\033[1mLabels\033[0m")
    print("Label p", labelp)
    print("Label n", labeln)

    print("\n\033[1mmup_mun\033[0m")
    mup, mun= xzcvpr.mup_mun(P, T, labelp, labeln)
    print("mup :", mup)
    print("mun :", mun)

    print("\n\033[1mcp_cn\033[0m")
    cp, cn = xzcvpr.cp_cn(P, T, labelp, labeln)
    print("cp:",cp)
    print("cn:",cn)

    print("\n\033[1mmin_max\033[0m")
    min, max = xzcvpr.min_max(P, T, labeln)
    print("Pn min:", min)
    print("Pn max:", max)

    min, max = xzcvpr.min_max(P, T, labelp)
    print("Pp min:", min)
    print("Pp max:", max)

    H_p, xedges_p, yedges_p = xzcvpr.hist(P, T, labelp)
    H_n, xedges_n, yedges_n = xzcvpr.hist(P, T, labeln)

    # print("H_p shape: ", H_p.shape)
    # print("H_p: ", H_p)

    # test.checkCplot(H_p,"H_p")

    print(xzcvpr.xp(X, T, labelp))




if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()