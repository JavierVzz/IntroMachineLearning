# Javier Vazquez
# Grid Printer
# Date
# Description:

import os
import numpy as np
import numpy.linalg as LA

def main():
    X = np.array([[72., 101., 94.], [50., 96., 70.], [14., 79., 10.], [8., 70., 1.]], np.float64)
    # X = np.loadtxt("X.txt")
    print("X")
    print(X)
    μ = np.mean(X, axis=0)
    print("μ")
    print(μ)
    Z = X - μ
    print("Z")
    print(Z)
    C = np.cov(Z, rowvar=False);
    print("C")
    print(C)
    [λ, V] = LA.eigh(C)
    print("λ")
    print(λ)
    print("V")
    print(V)
    # row=V[0,:]
    # col=V[:,0]
    # test = np.dot(C, row) / (λ[0] * row)
    # print("Test")
    # print(test)
    # test2 = np.dot(C, col) / (λ[0] * col)
    # print("Test 2")
    # print(test2)
    print(np.linalg.norm(V[0]))
    print(np.linalg.norm(V[1]))
    print(np.dot(V[0,:], V[1,:]))
    print(V.shape)


if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()