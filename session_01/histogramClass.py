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

    def normPDF(self, mean, std, x):
        norm = 1/np.sqrt(2*np.pi*std**2)*np.exp((-1*(x-mean)**2)/(2*std**2))
        df = pd.DataFrame(norm)
        df.to_excel("norm.xlsx", sheet_name="norm")
        norm = np.vstack((x, norm)).T
        return norm

    def hist(self, df):
        hist, bin_edges = np.histogram(df[:, 0], bins=np.arange(np.amin(df[:, 0]), np.amax(df[:, 0]) + 2), density=False)
        writer = pd.ExcelWriter("histogram_pdf.xlsx")
        histX = pd.DataFrame(hist)
        bin_edgesX = pd.DataFrame(bin_edges)
        histX.to_excel(writer,"hist")
        bin_edgesX.to_excel(writer,"bin_edges")
        writer.save()
        hist = np.vstack((bin_edges[0:np.alen(bin_edges)-1,], hist)).T
        return hist

    def query(self, queryArray, Fhist, Mhist):
        InF = queryArray[np.in1d(queryArray, Fhist[:, 0])]
        InM = queryArray[np.in1d(queryArray, Mhist[:, 0])]
        FF = InF[np.in1d(InF, InM)]
        notInF = queryArray[np.in1d(queryArray, Fhist[:, 0], invert=True)]
        notInM = queryArray[np.in1d(queryArray, Mhist[:, 0], invert=True)]
        Fquery = Fhist[np.in1d(Fhist[:, 0], queryArray)]
        Mquery = Mhist[np.in1d(Mhist[:, 0], queryArray)]
        FMquery = Fquery[np.in1d(Fquery[:, 0], Mquery[:, 0])]
        MFquery = Mquery[np.in1d(Mquery[:, 0], Fquery[:, 0])]
        query = FMquery[:, 1] / (FMquery[:, 1] + MFquery[:, 1])
        return np.vstack((FF,query)).T

    def plotHist(self, df, label1, label2, hist):
        if(df[0,1] == label1):
            label = label1
            color = "pink"
        elif(df[0,1] == label2):
            label = label2
            color = "blue"
        fig = plt.figure(label)
        fig.suptitle(label, fontsize=14, fontweight='bold')
        ax = fig.add_subplot(111)
        fig.subplots_adjust(top=0.85)
        ax.set_xlabel('Bins')
        ax.set_ylabel('Frequency')
        for item in hist:
            ax.annotate(" "+str(item[0])+": "+str(item[1]), xy=(item[0], item[1]+10))
        plt.hist(df[:, 0],
                 bins=np.arange(np.amin(df[:, 0]), np.amax(df[:, 0]) + 2), rwidth=.90,
                 color=color)
        plt.show()

if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")