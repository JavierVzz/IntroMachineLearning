import os, struct
import matplotlib as plt
import pylab
import numpy as np
from array import array as pyarray

class read_MNIST():

    def __init__(self):
        pass

    def load_mnist(self, dataset="training", digits=range(10), path=os.getcwd()+"\\data_sets"):

        """
        Adapted from: http://cvxopt.org/applications/svm/index.html?highlight=mnist
        """

        if dataset == "training":
            fname_img = os.path.join(path, 'train-images.idx3-ubyte')
            fname_lbl = os.path.join(path, 'train-labels.idx1-ubyte')
        elif dataset == "testing":
            fname_img = os.path.join(path, 't10k-images.idx')
            fname_lbl = os.path.join(path, 't10k-labels.idx')
        else:
            raise ValueError("dataset must be 'testing' or 'training'")

        flbl = open(fname_lbl, 'rb')
        magic_nr, size = struct.unpack(">II", flbl.read(8))
        lbl = pyarray("b", flbl.read())
        flbl.close()

        fimg = open(fname_img, 'rb')
        magic_nr, size, rows, cols = struct.unpack(">IIII", fimg.read(16))
        img = pyarray("B", fimg.read())
        fimg.close()

        ind = [ k for k in range(size) if lbl[k] in digits ]
        N = len(ind)

        images = np.zeros((N, rows, cols), dtype=np.uint8)
        labels = np.zeros((N, 1), dtype=np.int8)
        for i in range(len(ind)):
            images[i] = np.array(img[ ind[i ] * rows *cols : (ind[i ] +1 ) * rows *cols ]).reshape((rows, cols))
            labels[i] = lbl[ind[i]]

        flatimages = list()
        for i in images:
            flatimages.append(i.ravel())
        X = np.asarray(flatimages)

        T = labels.flatten()

        return X, T









if __name__ == '__main__':
    print("Direct access to "+ os.path.basename(__file__))
else:
    print(os.path.basename(__file__)+" class instance")