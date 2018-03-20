# get all Stock Symbols  .
# it should include all stocks in US stock market

# from matplotlib import pyplot as plt
# from datetime import date, timedelta
import pandas as pd
from Getearningcalendar import Getearningcalendar

getcalendar = Getearningcalendar()

fpath_1 = '/datacenter/calendarlist171101-180128.xlsx'
df_1 = getcalendar.read_from_xlsx(fpath_1)
print(df_1.head(5))

list_1 = {}

fpath_2 = '/datacenter/calendarlist0129-0228.xlsx'
df_2 = getcalendar.read_from_xlsx(fpath_2)

print(df_2.head(5))
list_2 = {}

list_tg = {}

list_1['company_name'] = df_1[0][1:].tolist()
list_2['company_name'] = df_2[0][1:].tolist()
list_tg['company_name'] = list_1['company_name'] + list_2['company_name']

list_1['symbol'] = df_1[1][1:].tolist()
list_2['symbol'] = df_2[1][1:].tolist()

list_tg['symbol'] = list_1['symbol'] + list_2['symbol']

list_1['market_cap'] = df_1[2][1:].tolist()
list_2['market_cap'] = df_2[2][1:].tolist()

list_tg['market_cap'] = list_1['market_cap'] + list_2['market_cap']

list_1['reported_date'] = df_1[3][1:].tolist()
list_2['reported_date'] = df_2[7][1:].tolist()

list_tg['reported_date'] = list_1['reported_date'] + list_2['reported_date']

list_1['eps'] = df_1[7][1:].tolist()
list_2['eps'] = df_2[8][1:].tolist()

list_tg['eps'] = list_1['eps'] + list_2['eps']

list_1['num_est'] = df_1[6][1:].tolist()
list_2['num_est'] = df_2[6][1:].tolist()

list_tg['num_est'] = list_1['num_est'] + list_2['num_est']

# print('num_est = ', list_tg['num_est'])

# for i, row in enumerate(list_tg):
#     print(i, row)

# d_s = sorted(list_tg, key = lambda k: list_tg[k][1])

# for i, row in enumerate(list_tg['company_name']):
#     print(i, list_tg['symbol'][i], row)

df = pd.DataFrame.from_dict(list_tg)
df_s = df.sort_values(by=['symbol'])

print(df_s)

df_d = df_s.drop_duplicates(subset='symbol', keep='first')

print('df_d =', df_d)

df_i = df_d.reset_index(drop=True)

print('df_i = ', df_i)

writer = pd.ExcelWriter('/datacenter/calendarlist.xlsx')
df_i.to_excel(writer,'Sheet1')
writer.save()

# # mm/dd/yyyy
# start = '10/01/2017'
# end = '01/26/2018'
#
# # parameters: start date, end date, filtered 1/ unfiltered 0, past p / future f
# # for future = 'f', the eps isn't known yet
#
# list_data = getcalendar.get_calendar_all(start, end, 0)
# #
# # for j, row in enumerate(list_data):
# #     print(j, row)
# #
# getcalendar.write_to_xlsx(list_data, 9)
#
# file_p_1 = '/datacenter/calendarlist0129-0228.xlsx'
#
# df1 = getcalendar.read_from_xlsx(file_p_1)
#
# file_p_2 = '/datacenter/calendarlist171101-180128.xlsx'
#
# df1 = getcalendar.read_from_xlsx(file_p_1)
#
# df2 = getcalendar.read_from_xlsx(file_p_2)
#
# # print(df1[1])
# # print(df2[1])
#
# symbol_1 = df1[1][1:].tolist()
# symbol_2 = df2[1][1:].tolist()
#
# symbols = symbol_1[1:] + symbol_2[1:]
#
# # for i, row in enumerate(symbols):
# #     print(i, row)
#
# symbols_d = list(set(symbols))
#
# symbols_s = sorted(symbols_d)
# for i, row in enumerate(symbols_s):
#     print(i, row)
#
# getcalendar.create_write_file('symbols.txt', symbols_s)

# print(getcalendar.read_txt_file('symbols.txt'))

# list_cols = list(df1.columns.values)
#
# # print(list(df1.columns.values))
#
# list_data = []
#
# for i, row in enumerate(df1[list_cols[0]][1:]):
#     tmp_d_1 = []
#     for j, col in enumerate(list_cols):
#         tmp_d_1.append(df1[list_cols[j]][i + 1])
#     list_data.append(tmp_d_1)
#
# list_filtered = getcalendar.get_filter2(list_data)
#
# for j, cols in enumerate(list_filtered):
#     print(j, cols)


# date_xs = []
# stocks = []
#
# plt.plot(date_xs,  stocks, '.', label='stock')
#
# plt.title('Stock Report')
# plt.legend(bbox_to_anchor=(1, 0), loc=3, borderaxespad=0.2)
#
# plt.show()