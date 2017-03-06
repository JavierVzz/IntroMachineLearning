import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class histogram():

    def __init__(self):
        pass

    def loadData(self, file):
        """Load an excel file to df"""
        df = pd.read_excel(io=file, sheetname=0, header=0).values
        return df

    def sortDataPerLabel(self, df, label1, label2):
        lb1Data = df[np.where(df[:, 1] == label1)]
        lb2Data = df[np.where(df[:, 1] == label2)]
        return lb1Data, lb2Data

    def convertToInches(self, df):
        dfInches = df[:,0]*12+df[:,1].copy()
        dfInches = np.vstack((dfInches, df[:,2])).T
        return dfInches

    def hist(self, df):
        hist, bin_edges = np.histogram(df[:, 0], np.arange(np.amin(df[:, 0]), np.amax(df[:, 0]) + 2))
        hist = np.vstack((bin_edges[0:np.alen(bin_edges)-1,], hist)).T
        return hist

    def plotHist(self, df, label1, label2):
        if(df[0,1] == label1):
            color = "pink"
        elif(df[0,1] == label2):
            color = "blue"
        plt.hist(df[:, 0],
                 bins=np.arange(np.amin(df[:, 0]), np.amax(df[:, 0]) + 2), rwidth=.90,
                 color=color)
        plt.show()

if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")