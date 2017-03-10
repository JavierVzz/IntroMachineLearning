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
    dfInches = h.convertToInches(df)
    label1 = "Female"
    label2 = "Male"
    print("\033[1mPopulation Data\033[0m")
    print("Min: ",np.amin(dfInches[:,0]))
    print("Max: ",np.amax(dfInches[:,0]))

    dfFemale, dfMale = h.sortDataPerLabel(dfInches, label1, label2)
    
    # Female data
    print("\033[1m\nFemale: \033[0m")
    Fhist = h.hist(dfFemale)
    Fnorm = h.normPDF(np.mean(dfFemale[:,0]), np.std(dfFemale[:,0]), Fhist[:,0])
    print("Mean: ", np.mean(dfFemale[:,0]))
    print("Std:  ", np.std(dfFemale[:,0]))
    print("Size: ", dfFemale[:,0].size)
    print("Count Histogram\n", Fhist)
    np.set_printoptions(suppress=True)
    print("PDF Histogram\n", Fnorm)
    h.plotHist(dfFemale, label1, label2, Fhist)

    # Male data
    print("\033[1m\nFemale: \033[0m")
    Mhist = h.hist(dfMale)
    Mnorm = h.normPDF(np.mean(dfMale[:,0]), np.std(dfMale[:,0]), Mhist[:,0])
    print("Mean: ", np.mean(dfMale[:,0]))
    print("Std:  ", np.std(dfMale[:,0]))
    print("Size: ", dfMale[:,0].size)
    print("Count Histogram\n", Mhist)
    np.set_printoptions(suppress=True)
    print("PDF Histogram\n", Mnorm)
    h.plotHist(dfMale, label1, label2, Mhist)

    queryArray = np.arange(55, 81, 5)
    print("\033[1m\nHistogram results: \033[0m")
    query = h.query(queryArray, Fhist, Mhist)
    print(query)

    print("\033[1m\nBayesian results: \033[0m")
    query = h.queryPDF(queryArray, Fnorm, Mnorm, dfFemale[:,0].size, dfMale[:,0].size)
    print(query)

if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()