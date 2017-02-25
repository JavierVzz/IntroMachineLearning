# Javier Vazquez
# Grid Printer
# Date
# Description:

import os
import numpy as np

def readFile(filename):
    fo = open(filename, "r")
    return fo.readlines()

def writeFile(content, filename):
    fo = open(filename, "w")
    fo.write(content)
    fo.close()
    return True

def parsing(lines):
    content = ""
    for line in lines:
        content += line
    content = content.replace("\n","\t")
    content = content.replace("\t", "\n")
    # content = content.replace("\xa0", "")
    return content

def createPGM(content, filename):
    fo = open(filename+".pgm", "w")
    fo.write("P2\n28 28\n 255\n"+content)
    return True

def createArray(lines):
    array = []
    for line in lines:
        array.append(int(line.replace("\n","")))
    return np.array(array)

def main():
    filename = "zero.txt"
    lines = readFile(filename)
    content = parsing(lines)
    createPGM(content, filename.replace(".txt",""))
    writeFile(content, filename.replace(".txt","Parsed.txt"))
    lines = readFile(filename.replace(".txt","Parsed.txt"))
    x = createArray(lines)
    x.shape = -1, x.size
    # print(x.size)
    # print(x.shape)
    # print(x)

if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()