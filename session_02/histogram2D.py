# Javier Vazquez
# Histogram
# Feb 15, 2017
# Python 3.6

import numpy as np
import os
import pandas as pd
import numpy as np

def main():
    female2 = np.zeros((10,10), dtype="i")
    hmin = 66
    hmax = 78
    smin = 18
    smax = 25.5
    bins = 10
    r = c = 0

    df = pd.read_excel(io="data.xlsx", sheetname=1, header=0).values
    # for n in range(df.shape[0]):
    #     r = np.int(np.round(1 + (bins - 1) * ((df[n, 0] - hmin) / (hmax - hmin))) - 1)
    #     c = np.int(np.round(1 + (bins - 1) * ((df[n, 1] - smin) / (smax - smin))) - 1)
    #     female[r, c] += 1
    #
    # print(female)

    height = np.linspace(hmin, hmax, bins+1)
    span = np.linspace(smin, smax, bins+1)

    for n in range(df.shape[0]):
        if df[n,0] >= height[0] and df[n,0] <= height[1]:
            r = 0
        elif df[n,0] > height[1] and df[n,0] <= height[2]:
            r = 1
        elif df[n,0] > height[2] and df[n,0] <= height[3]:
            r = 2
        elif df[n,0] > height[3] and df[n,0] <= height[4]:
            r = 3
        elif df[n,0] > height[4] and df[n,0] <= height[5]:
            r = 4
        elif df[n,0] > height[5] and df[n,0] <= height[6]:
            r = 5
        elif df[n,0] > height[6] and df[n,0] <= height[7]:
            r = 6
        elif df[n,0] > height[7] and df[n,0] <= height[8]:
            r = 7
        elif df[n,0] > height[8] and df[n,0] <= height[9]:
            r = 8
        elif df[n,0] > height[9] and df[n,0] <= height[10]:
            r = 9

        if df[n,1] >= span[0] and df[n,1] <= span[1]:
            c = 0
        elif df[n,1] > span[1] and df[n,1] <= span[2]:
            c = 1
        elif df[n,1] > span[2] and df[n,1] <= span[3]:
            c = 2
        elif df[n,1] > span[3] and df[n,1] <= span[4]:
            c = 3
        elif df[n,1] > span[4] and df[n,1] <= span[5]:
            c = 4
        elif df[n,1] > span[5] and df[n,1] <= span[6]:
            c = 5
        elif df[n,1] > span[6] and df[n,1] <= span[7]:
            c = 6
        elif df[n,1] > span[7] and df[n,1] <= span[8]:
            c = 7
        elif df[n,1] > span[8] and df[n,1] <= span[9]:
            c = 8
        elif df[n,1] > span[9] and df[n,1] <= span[10]:
            c = 9
        female2[r,c] += 1

    print(female2)

    # print(female == female2)

if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()