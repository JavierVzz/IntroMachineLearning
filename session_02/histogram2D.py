# Javier Vazquez
# Histogram
# Feb 15, 2017
# Python 3.6

import numpy as np
import os
import pandas as pd
import numpy as np



def main():
    female = np.zeros((10,10), dtype="i")
    female2 = np.zeros((10,10), dtype="i")
    hmin = 57
    hmax = 72
    smin = 16
    smax = 23
    bins = 10
    r = c = 0

    df = pd.read_excel(io="data.xlsx", sheetname=0, header=0).values
    # for n in range(df.shape[0]):
    #     r = np.int(np.round(1 + (bins - 1) * ((df[n, 0] - hmin) / (hmax - hmin))) - 1)
    #     c = np.int(np.round(1 + (bins - 1) * ((df[n, 1] - smin) / (smax - smin))) - 1)
    #     female[r, c] += 1
    #
    # print(female)

    # for n in range(df.shape[0]):
    #     if df[n,0] >= 57 and df[n,0] <= 58.5:
    #         r = 0
    #     elif df[n,0] > 58.5 and df[n,0] <= 60:
    #         r = 1
    #     elif df[n,0] > 60 and df[n,0] <= 61.5:
    #         r = 2
    #     elif df[n,0] > 61.5 and df[n,0] <= 63:
    #         r = 3
    #     elif df[n,0] > 63 and df[n,0] <= 64.5:
    #         r = 4
    #     elif df[n,0] > 64.5 and df[n,0] <= 66:
    #         r = 5
    #     elif df[n,0] > 66 and df[n,0] <= 67.5:
    #         r = 6
    #     elif df[n,0] > 67.5 and df[n,0] <= 69:
    #         r = 7
    #     elif df[n,0] > 69 and df[n,0] <= 70.5:
    #         r = 8
    #     elif df[n,0] > 70.5 and df[n,0] <= 72:
    #         r = 9
    #
    #     if df[n,1] >= 16 and df[n,1] <= 16.7:
    #         c = 0
    #     elif df[n,1] > 16.7 and df[n,1] <= 17.4:
    #         c = 1
    #     elif df[n,1] > 17.4 and df[n,1] <= 18.1:
    #         c = 2
    #     elif df[n,1] > 18.1 and df[n,1] <= 18.8:
    #         c = 3
    #     elif df[n,1] > 18.8 and df[n,1] <= 19.5:
    #         c = 4
    #     elif df[n,1] > 19.5 and df[n,1] <= 20.2:
    #         c = 5
    #     elif df[n,1] > 20.2 and df[n,1] <= 20.9:
    #         c = 6
    #     elif df[n,1] > 20.9 and df[n,1] <= 21.6:
    #         c = 7
    #     elif df[n,1] > 21.6 and df[n,1] <= 22.3:
    #         c = 8
    #     elif df[n,1] > 22.3 and df[n,1] <= 23:
    #         c = 9
    #         print(c)
    #     female[r,c] += 1
    #
    # print(female)

    height = np.linspace(hmin, hmax, bins+1)
    span = np.linspace(smin, smax, bins+1)

    # print(height[0])
    # print(height)

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
            print(c)
        female2[r,c] += 1

    print(female2)

    # print(female == female2)



if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()