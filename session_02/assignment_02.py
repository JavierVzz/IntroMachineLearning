# Javier Vazquez
# Date March 5, 2017
# Description:

import os
import histogramClass
import numpy as np

def main():
    h = histogramClass.histogram()
    file = "Assignment_2_to_Pandas.xlsx"
    df = h.loadData(file)
    label1 = "Female"
    label2 = "Male"
    dfFemale, dfMale = h.sortDataPerLabel(df, label1, label2)
    Fmean, Fmin, Fmax, Fsize = h.basicStats(dfFemale)

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

    print("\033[1mMale Data\033[0m")
    print("Size: ", np.size(dfMale)/3)

    print("\nHeight")
    print("Min: ",np.amin(dfMale[:,1]))
    print("Max: ",np.amax(dfMale[:,1]))
    print("Mean: ",np.mean(dfMale[:,1]))

    print("\nHandSpan")
    print("Min: ",np.amin(dfMale[:,2]))
    print("Max: ",np.amax(dfMale[:,2]))
    print("Mean: ", np.mean(dfMale[:,2]))

    print("Cov:")
    Mcov = h.cov(dfMale[:,1], dfMale[:,2])
    print(Mcov)

    Hm, Hdm, xedges, yedges = h.hist2d(dfMale)
    print("Histogram:")
    print(Hdm)

    # normPDF2d(Fcov, Mcov, )

 

if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()