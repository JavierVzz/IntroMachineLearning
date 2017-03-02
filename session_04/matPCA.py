# Javier Vazquez
# Grid Printer
# Date
# Description:

import os
import numpy as np
from matplotlib.mlab import PCA

def main():
    # X = np.loadtxt("X.txt")
    X = np.array([[72., 101., 94.], [50., 96., 70.], [14., 79., 10.], [8., 70., 1.]], np.float64)
    pca = PCA(X)
    print(pca.s)


if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()