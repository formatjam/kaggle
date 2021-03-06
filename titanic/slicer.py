"""
slice train.cvs into 5 fold and generate files for cross validation.
"""

import csv as csv
import numpy as np

fin = open('train.csv', 'rb') #Load in the csv file
header = fin.readline()

data=[]
for row in fin:
    data.append(row)
j = 0
for i in range(0, len(data), len(data)/5):
    if j >=5:
        break
    ftrain = open('train' + str(j) + '.csv', 'w')
    ftest = open('test' + str(j) + '.csv', 'w')
    ftrain.write(header)
    ftest.write(header)
    for k in range(len(data)):
        if i <= k and k < i + len(data)/5:
            ftest.write(data[k])
        else:
            ftrain.write(data[k])
    j += 1
    ftrain.close()
    ftest.close()

