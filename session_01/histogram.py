# Javier Vazquez
# Histogram
# Feb 2, 2017
# Python 3.6

from readExcel import excelOperations
import os, math, statistics

def main():
    excelOp = excelOperations()
    wb , ws = excelOp.readExcelFile("assigment_01.xlsx")
    print(wb.get_sheet_names())
    # excelOp.ws = wb.get_sheet_by_name("Data")
    # excelOp.displayContent()
    # excelOp.countByLabel()
    female, male = excelOp.excelColsToList()
    # excelOp.listToTextFile(list1)
    print("Female population mean: ",statistics.mean(female))
    print("Male population mean: ",statistics.mean(male))
    print("Female population standard deviation: ",statistics.pstdev(female))
    print("Male population standard deviation: ",statistics.pstdev(male))
    print("Female population size: ",len(female))
    print("Male population size: ",len(male))
    mainList = female + male
    print("Population size: ",len(mainList))
    print("Maximum value: ", max(mainList))
    print("Minimum value: ", min(mainList))
    print("Female pop size: ",len(female))
    print("Minimum female value: ", min(female))
    print("Maximum female value: ", max(female))





if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()