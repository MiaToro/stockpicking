import requests

from class_fd.Getprice import Getprice


def get_tag(list_ip):
    tmp_a_1 = list_ip.split('<th>')
    tb_tags = []
    for row in tmp_a_1[0:]:
        # print(i, row)
        tmp_b_1 = row.split('>')
        for j, col in enumerate(tmp_b_1):
            col = col.lower()
            col = col.replace('*', '')
            col = col.replace('\'', '')
            col = col.replace('#', 'num')
            col = col.replace('%', 'p')
            tmp_b_2 = col.split('<')
            for k, line in enumerate(tmp_b_2):
                if (line.strip() != '') & (line.find('/') == -1) \
                        & (line.find('span') == -1) & (line.find('style') == -1) \
                        & (line.find('href') == -1):
                    tmp_b_3 = line.strip()
                    tmp_b_3 = tmp_b_3.replace(')', '')
                    tmp_b_4 = tmp_b_3.split('(')
                    if len(tmp_b_4) == 1:
                        tb_tags.append(tmp_b_4[0].replace(' ', '_'))
                    else:
                        for cell in tmp_b_4:
                            tb_tags.append(cell.strip().replace(' ', '_'))
    tmp_c_1 = tb_tags[0:3] + tb_tags[5:]
    # for i, row_1 in enumerate(tmp_c_1):
    #     print(i, row_1)

    # 0, company_name, 1, symbol, 2, market_cap, 3, reported_date,
    # 4, fiscal_quarter_ending, 5, consensus_eps_forecast,
    # 6, num_of_ests, 7, eps,  8, surprise

    # for i, row in enumerate(tmp_c_1):
    #     print(i, row)

    tmp_c_2 = tmp_c_1[0:3] + tmp_c_1[4:6]
    tmp_c_2.append(tmp_c_1[6] + '_' + tmp_c_1[7] + '_' + tmp_c_1[8])
    tmp_c_2.append(tmp_c_1[9] + '_' + tmp_c_1[10])
    tmp_c_2.append(tmp_c_1[11])
    # tmp_c_2.append(tmp_c_1[12] + '_' + tmp_c_1[13])
    tmp_c_2 = tmp_c_2 + tmp_c_1[14:16]

    return tmp_c_2


def get_data(list_data):
    list_re = []
    tmp_a_1 = list_data.split('<td')

    # 0, company_name, 1, symbol, 2, market_cap, 3, reported_date,
    # 4, fiscal_quarter_ending, 5, consensus_eps_forecast, 6, num_of_ests,
    # 7, eps, 8, surprise
    for i, row in enumerate(tmp_a_1[2:]):
        # print(i, row)
        if row.find('display:none') == -1:
            if row.find('CompanyTable_companyname') > -1:
                tmp_b_1 = row.split('>')
                tmp_b_2 = tmp_b_1[2].split('(')
                tmp_company_name = tmp_b_2[0].strip()
                if len(tmp_b_2) > 2:
                    tmp_symbol = tmp_b_2[2].split(')')[0].strip()
                else:
                    tmp_symbol = tmp_b_2[1].split(')')[0].strip()
                tmp_b_3 = tmp_b_1[4].split('$')
                if len(tmp_b_1[4].split('$')) > 1:
                    tmp_size = tmp_b_3[1].split('<')[0].strip()
                else:
                    tmp_size = 'n/a' # tmp_b_3[0].split('<')[0].strip()
                list_re.append(tmp_company_name)
                list_re.append(tmp_symbol)
                list_re.append(tmp_size)
            elif row.find('span') != -1:
                tmp_c_1 = row.split('>')[2].split('<')[0].strip()
                list_re.append(tmp_c_1)
            else:
                tmp_d_1 = row.split('>')[1].strip().split('<')[0].strip().replace('$', '')
                list_re.append(tmp_d_1)

    return list_re

ck_date = '01/19/2018'  # mm/dd/yyyy
url_list = 'http://www.nasdaq.com/earnings/earnings-calendar.aspx?date=2018-Jan-18'
url_tmx = 'https://web.tmxmoney.com/quote.php?qm_symbol=FITB:US'

page = requests.get(url_list)
page_txt = page.text

tmp_con_1 = page_txt.split('ECCompaniesTable')
if len(tmp_con_1) > 1:
    tmp_con_1 = tmp_con_1[1]
else:
    print('Empty')
    exit()
tmp_con_2 = tmp_con_1.split('</table>')[0]

tmp_con_3 = tmp_con_2.split('<tr>')[1:]

j = 0

# get table tags
for row in tmp_con_3[0:1]:
    # print(row)
    tmp_a_1 = get_tag(row)

# get table data
list_data = []
for row in tmp_con_3[1:]:
    list_data.append(get_data(row))

getprice = Getprice()

all_tog = 0

cal_num = 0  #

date_list = getprice.get_date_list()

# print(date_list)

for i, row in enumerate(list_data[0:]):
    # getprice.set_url(row[1])
    if (float(row[6]) > 10) & (row[5] != 'n/a'):
        if (float(row[5]) > 0) & (row[2].find('B') != -1):
            data_st = getprice.get_diff_dtod(row[1], ck_date)
            cal_num += 1
            all_tog += data_st
            # if data_st > 10:
            print(i, row)
            print(data_st)

print(cal_num, 'all_tog = ', all_tog / cal_num)
