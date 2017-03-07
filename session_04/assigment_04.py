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
    # mnist.printPlot(C, label="C")
    # mnist.checkCplot(C, label="C")
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