from Get_Reuter_Info import Get_Reuter_Info
from Getearningcalendar import Getearningcalendar

# get info from reuters.com

getcalendar = Getearningcalendar()
get_reuter = Get_Reuter_Info()

tmp_1 = getcalendar.read_txt_file('symbols.txt')

# tmp_1 = ['FB.O']

st_rating = []

for i, row in enumerate(tmp_1):

    page_txt = get_reuter.get_webpage(row)
    tmp_2 = get_reuter.get_mean_rating(page_txt)
    st_rating.append([row, tmp_2])
    print(row, tmp_2)

for j, col in enumerate(st_rating):
    print(j, col)

getcalendar.create_write_file('stock_mean_rating', st_rating)

