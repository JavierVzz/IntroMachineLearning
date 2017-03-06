# Javier Vazquez
# Date March 5, 2017
# Description:

import os
import histogramClass
import numpy as np

def main():
    h = histogramClass.histogram()
    file = "Assignment_1_to_Pandas.xlsx"
    df = h.loadData(file)
    dfInches = h.convertToInches(df)
    label1 = "Female"
    label2 = "Male"
    print("\033[1mMin\033[0m: {0}\n\033[1mMax\033[0m: {1}".format(np.amin(dfInches[:,0]), np.amax(dfInches[:,0])))
    dfFemale, dfMale = h.sortDataPerLabel(dfInches, label1, label2)
    hist = h.hist(dfFemale)
    print("\033[1m\nFemale: \nLabel Frequency\033[0m:\n{0}".format(hist))
    hist = h.hist(dfMale)
    print("\033[1m\nMale: \nLabel Frequency\033[0m:\n{0}".format(hist))
    h.plotHist(dfFemale, label1, label2)
    h.plotHist(dfMale, label1, label2)


if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()