# Javier Vazquez
# Histogram
# Feb 2, 2017
# Python 3.6

from readExcel import excelOperations
import os, pprint

def main():
    excelOp = excelOperations()
    wb , ws = excelOp.readExcelFile("assigment_01.xlsx")
    print(wb.get_sheet_names())
    # excelOp.ws = wb.get_sheet_by_name("Data")
    excelOp.displayContent()
    # excelOp.countByLabel()
    list1, list2 = excelOp.excelColsToList()
    excelOp.listToTextFile(list1)

if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()