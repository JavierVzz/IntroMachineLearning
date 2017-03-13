import os
import pandas as pd
import numpy as np


class linearClassifier():

    def __init__(self):
        pass

    def loadData(self, file, cols):
        """Load an excel file to df"""
        df = pd.read_excel(io=file, sheetname=0, header=0, parse_cols=cols).values
        return df

if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")