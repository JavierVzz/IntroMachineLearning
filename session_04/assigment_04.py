import read_MNIST_Class, XZCVPR, os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    mnist = read_MNIST_Class.read_MNIST()
    # a = int(input("Negative Digit : "))
    # b = int(input("Positive Digit : "))
    print("Negative Digit : -5")
    print("Positive Digit : 9")
    a = -5
    b = 9
    X = mnist.load_mnist('training', digits=[a,b])
    xzcvpr = XZCVPR.XZCVPR()
    X_bar = xzcvpr.X(X)
    Z = xzcvpr.Z(X, X_bar)
    C = xzcvpr.C(Z)
    V = xzcvpr.V(C)
    print(V.shape)





if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()