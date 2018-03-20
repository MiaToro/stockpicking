# get all Stock Symbols  .
# it should include all stocks in US stock market

# from matplotlib import pyplot as plt
# from datetime import date, timedelta
import pandas as pd
from class_fd.Getearningcalendar import Getearningcalendar

getcalendar = Getearningcalendar()

path_1 = '/datacenter/stock_list_nasdaq.xlsx'
df = getcalendar.read_from_xlsx(path_1)

df.columns = df.iloc[0]

df = df.reindex(df.index.drop(0))  # remove first line (index=0)
df_i = df.reset_index(drop=True)

df_1 = df_i.drop(df.columns[[0]], 1)  # remove old index
df_e = df[['symbol', 'company_name', 'market_cap', 'eps', 'num_est', 'reported_date']]
df_e = df_e.reset_index(drop=True)
# print(df_e.head(5))

path_2 = 'stock_mean_rating'
rating = getcalendar.read_txt_file(path_2)

# st_1 = 'AAC 1.67'
# rating.insert(3, st_1)

rtg_col_1 = []
rtg_col_2 = []

for i, row in enumerate(rating):
    tmp_r_1 = row.split(' ')
    rtg_col_1.append(tmp_r_1[0])
    rtg_col_2.append(tmp_r_1[1])

df_rtg = pd.DataFrame({'rating': rtg_col_2}, index=rtg_col_1)
# print(df_rtg)

result_1 = df_e.join(df_rtg, on='symbol')
print(result_1)

result_2 = result_1.sort_values(by=['rating'])

result_3 = result_2[result_2.rating != 'n/a'] # drop rows where rating is n/a
result_4 = result_3[result_3.eps > '0']
result_5 = result_4[result_4.num_est > '5']
result_5 = result_5[result_4.rating < '1.7']

result_6 = result_5.reset_index(drop=True)

print(result_6)

getcalendar