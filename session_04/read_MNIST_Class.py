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

        return X

    def printPlot(self, X):
        plt.pyplot.imshow(X[20].reshape(28, 28), interpolation='None', cmap=plt.pyplot.cm.gray)
        plt.pyplot.show()

    def vectortoimg(self, *args, width=28, size=1):
        n = len(args)
        fig = plt.pyplot.figure()
        for i, arg in enumerate(args):
            plt.pyplot.subplot(1,n,i+1)
            plt.pyplot.imshow(arg.reshape(width, width), interpolation="None", cmap=plt.pyplot.cm.gray)
            plt.pyplot.axis("off")
        fig.tight_layout(pad=0)
        fig.set_size_inches(w=n*size, h=size)
        plt.pyplot.show()


if __name__ == '__main__':
    print("Direct access to "+ os.path.basename(__file__))
else:
    print(os.path.basename(__file__)+" class instance")