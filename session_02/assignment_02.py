# Javier Vazquez
# Date March 5, 2017
# Description:

import os
import histogramClass
import numpy as np
import matplotlib.pyplot as plt

def main():
    h = histogramClass.histogram()
    file = "Assignment_2_to_Pandas.xlsx"
    df = h.loadData(file)
    label1 = "Female"
    label2 = "Male"
    dfFemale, dfMale = h.sortDataPerLabel(df, label1, label2)
    Fmean, Fmin, Fmax, Fsize = h.basicStats(dfFemale)
    Mmean, Mmin, Mmax, Msize = h.basicStats(dfMale)

    print("\033[1mFemale Data\033[0m")
    print("Size: ", Fsize)

    print("\nHeight")
    print("Min: ", Fmin[0])
    print("Max: ", Fmax[0])
    print("Mean: ", Fmean[0])

    print("\nHandSpan")
    print("Min: ", Fmin[1])
    print("Max: ", Fmax[1])
    print("Mean: ", Fmean[1])

    print("Cov:")
    Fcov = h.cov(dfFemale[:,1], dfFemale[:,2])
    print(Fcov)

    Hf, Hdf, xedges, yedges = h.hist2d(dfFemale)
    print("Histogram")
    print(Hdf)

    # print("\n\033[1mMale Data\033[0m")
    # print("Size: ", np.size(dfMale)/3)
    #
    # print("\nHeight")
    # print("Min: ", Mmin[0])
    # print("Max: ", Mmax[0])
    # print("Mean: ", Mmean[0])
    #
    # print("\nHandSpan")
    # print("Min: ", Mmin[1])
    # print("Max: ", Mmax[1])
    # print("Mean: ", Mmean[1])
    #
    # print("Cov:")
    Mcov = h.cov(dfMale[:,1], dfMale[:,2])
    # print(Mcov)
    #
    # Hm, Hdm, xedges, yedges = h.hist2d(dfMale)
    # print("Histogram:")
    # print(Hdm)

    print("\nQueries - Female")
    queryArray = np.array([[57, 16], [72, 23], [70, 21.5], [69, 23.5]])
    normPDF2d = h.normPDF2d(Fcov, Mcov, Fmean, Mmean, Fsize, Msize, queryArray)
    query = h.displayQueryPDF(queryArray, normPDF2d)
    print(query)

    print("\nPDF - Female")
    print(xedges)
    print(yedges)
    queryArray = np.dstack(np.meshgrid(xedges, yedges)).reshape(-1, 2)
    normPDF2d = h.normPDF2d(Fcov, Mcov, Fmean, Mmean, Fsize, Msize, queryArray)
    query = h.displayQueryPDF(queryArray, normPDF2d)
    print(query)

    x = dfFemale[:, 1].astype(float)
    y = dfFemale[:, 2].astype(float)

    plt.hist2d(x,y,bins=10,normed=True)
    plt.show()

    # print(queryArray)
    # np.set_printoptions(edgeitems = np.nan)
    # normPDF2d = h.normPDF2d(Fcov, Mcov, Fmean, Mmean, Fsize, Msize, queryArray)
    # query = h.displayQueryPDF(queryArray, normPDF2d)


if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()