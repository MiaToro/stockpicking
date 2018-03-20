from openpyxl import load_workbook
from pandas import DataFrame
import numpy as np
import random
from itertools import groupby
from matplotlib import pyplot as plt
import statistics

# range 5,  > 84%  >3.01   97% > 1.5

# get data from file to DataFrame of pandas

fpath = '/datacenter/calendar11080124.xlsx'

wb = load_workbook(filename = fpath)
# sheet_ranges = wb['Activities']
ws = wb.active

df1 = DataFrame(ws.values)

print(df1.columns.values)

# print(df1.head(1))

precentage = df1.ix[1:,9]

# print(df1.head(67)) # index from 1 to 66

# print(df1.ix[1:,12])

# 2: std 2.49   4.5
# 3: std 2.00   4.5
# 4: std 1.72   4.53
# 5: std 1.52   4.53
# 6: std 1.36   4.52
# 10: std 1.01  4.53
# 60: std 0.2   4.53
# 65: std 0.17  4.53

pick_sta = []

for k in range(0, 10000):

    pick_int = []

    for i in range(0, 65):
        p = random.randint(1, 22)
        if p in pick_int:
            pass
        else:
            pick_int.append(p)
        if len(pick_int) > 65:
            break

    # for j, col in enumerate(pick_int):
    #     print(j, col)
    #     pass

    rdm_val = 0
    rdm_num = 0
    rdm_avg = 0

    for i in pick_int[0:]:
        rdm_val += precentage[i]
        rdm_num += 1

    if rdm_num == 0:
        print('Empty')
    else:
        rdm_avg = rdm_val / rdm_num

    # print('rdm_avg = ', rdm_avg)

    pick_sta.append(rdm_avg)

print('ave_sta = ', sum(pick_sta)/len(pick_sta))


pick_sta_p = []

for l, col in enumerate(pick_sta):
    pick_sta_p.append(round(pick_sta[l]))

for i, row in enumerate(pick_sta_p):
    print(i, row)

pick_sta_p = sorted(pick_sta_p)

pick_sta_p = [list(j) for i, j in groupby(pick_sta_p)]

x_list = []
y_list = []

for i, row in enumerate(pick_sta_p):
    print(i, row[0], len(row))
    x_list.append(row[0])
    y_list.append(len(row))

print(x_list, y_list)

std_dev = statistics.stdev(pick_sta)
mean = sum(pick_sta)/len(pick_sta)

print("std_dev = ", std_dev)
print("mean = ", mean)

plt.plot(x_list,  y_list, label='statistics')

plt.title('distribution')
plt.legend(bbox_to_anchor=(1, 0), loc=3, borderaxespad=0.2)

plt.show()

