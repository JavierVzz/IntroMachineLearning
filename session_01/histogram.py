# Javier Vazquez
# Histogram
# Feb 2, 2017
# Python 3.6

from readExcel import excelOperations
import os, math, statistics, sys

def main():
    excelOp = excelOperations()
    wb , ws = excelOp.readExcelFile("assigment_01.xlsx")
    print(wb.get_sheet_names())
    # excelOp.ws = wb.get_sheet_by_name("Data")
    # excelOp.displayContent()
    # excelOp.sortByLabel()
    print("Type [max] for sample population.")
    size = input("Sample size: ")
    female, male = excelOp.excelColsToList(size)
    # print(female)
    # if female is False:
    #     print("Incorrect input")
    #     sys.exit(0)
    # # excelOp.listToTextFile(list1)
    if size == "max":
        print("Stats population")
        mainList = female + male
        print("Size: ", len(mainList))
        print("F. Size: ", len(female))
        print("M. Size: ", len(male))
        print()
        print("Max: ", max(mainList))
        print("F. Max: ", max(female))
        print("M. Max: ", max(male))
        print()
        print("Min: ", min(mainList))
        print("Min: ", min(female))
        print("Min: ", min(male))
        print()
        print("Mean: ", statistics.mean(mainList))
        print("F. Mean: ", statistics.mean(female))
        print("M. Mean: ", statistics.mean(male))
        print()
        print("Std dev: ", statistics.pstdev(mainList))
        print("F. Std dev: ", statistics.pstdev(female))
        print("M. Std dev: ", statistics.pstdev(male))
    else:
        print("Stats sample: ", size)
        mainList = female + male
        print("F. Size: ", len(female))
        print("M. Size: ", len(male))
        print()
        print("Max: ", max(mainList))
        print("F. Max: ", max(female))
        print("M. Max: ", max(male))
        print()
        print("Min: ", min(mainList))
        print("Min: ", min(female))
        print("Min: ", min(male))
        print()
        print("Mean: ", statistics.mean(mainList))
        print("F. Mean: ", statistics.mean(female))
        print("M. Mean: ", statistics.mean(male))
        print()
        print("Std dev: ", statistics.stdev(mainList))
        print("F. Std dev: ", statistics.stdev(female))
        print("M. Std dev: ", statistics.stdev(male))

    histogram = {}
    for i in range(min(mainList), max(mainList)+1):
        histogram[i] = [0, 0]
    print(histogram)
    female.sort()
    male.sort()
    for data in female:
            histogram[data][0] += 1
    for data in male:
            histogram[data][1] += 1
    for key, item in histogram.items():
        print(key, item)
    normalized = {}
    for i in range(min(mainList), max(mainList) + 1):
        normalized[i] = [0, 0]
    print(normalized)
    female.sort()
    male.sort()
    for key in histogram.keys():
        normalized[key][0] = histogram[key][0]/len(female)
    for key in histogram.keys():
        normalized[key][1] = histogram[key][1]/len(male)
    for key, item in normalized.items():
        print(key, item)

if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()