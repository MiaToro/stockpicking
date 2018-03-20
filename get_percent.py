from datetime import datetime

from class_fd.Getearningcalendar import Getearningcalendar

getcalendar = Getearningcalendar()

# mm/dd/yyyy
# start = '01/22/2018'
# end = '01/23/2018'
# 10 5.619853724335916

# start = '01/18/2018'
# end = '01/19/2018'
# 8 4.707249839682246

# start = '01/24/2018'
# end = '01/25/2018'
# 7 2.418747331936746

# start = '01/24/2018'
# end = '01/24/2018'
# 3 0.6101574901465424

# start = '01/01/2018'
# end = '01/21/2018'
# 12 4.032851803756796

# start = '12/01/2017'
# end = '12/31/2017'
# 13 3.978674935144926

# start = '11/10/2017'
# end = '11/30/2017'
# 22 6.044298139985733

# start = '11/08/2017'
# end = '11/30/2017'
# 33 4.5463414977219365

# start = '11/08/2017'
# end = '01/25/2018'
# # 75 4.310347117249412

start = '03/01/2018'
end = '03/08/2018'

list_data = getcalendar.get_calendar_all(start, end, 1)

for i, row in enumerate(list_data):
    print(i, row)

# getcalendar.write_to_xlsx(list_data)
list_filtered = getcalendar.get_filter(list_data)

for i, row in enumerate(list_filtered):
    print(i, row)

fl_val = 0
in_sum = 0
fl_avg = 0

date_xs = []
date_xe = []
data_ys = []
data_ye = []

data_line = []
ind_stop = 0

for i, row in enumerate(list_filtered):
    if len(row) >= 10:
        fl_val += row[9]
        tmp_1 = datetime.strptime(row[12], '%m/%d/%Y')
        date_xs.append(tmp_1)
        data_ys.append(row[13])
        tmp_2 = datetime.strptime(row[10], '%m/%d/%Y')
        date_xe.append(tmp_2)
        data_ye.append(row[11])
        in_sum += 1
        data_line.append([[tmp_1, tmp_2], [row[13], row[11]]])
    else:
        ind_stop = i

if in_sum == 0:
    print('Empty')
else:
    fl_avg = fl_val / in_sum

print(in_sum, fl_avg)



# rdm_val = 0
# rdm_num = 0
# rdm_avg = 0
#
# print('ind_stop = ', ind_stop)
#
# for i in range(0, 20):
#     p = random.randint(0, ind_stop - 1)
#     rdm_val += list_filtered[p][9]
#     rdm_num += 1
#     print(i, p)
#
# if rdm_num == 0:
#     print('Empty')
# else:
#     rdm_avg = rdm_val / rdm_num
#
# print('rdm_avg = ', rdm_avg)
#
# getcalendar.write_to_xlsx(list_filtered)


# #
# for i, row in enumerate(data_line):
#     print(i, row)
#     plt.plot(row[0], row[1], label=i)
#
# # plt.plot(date_xs,  data_ys, '.', label='start')
# # plt.plot(date_xe,  data_ye, '+', label='end')
#
# plt.title('title')
# plt.legend(bbox_to_anchor=(1, 0), loc=3, borderaxespad=0.2)
#
# plt.show()
