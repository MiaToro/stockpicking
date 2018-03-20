# https://www.paypal.me/miajiao

from datetime import date, timedelta
from datetime import datetime

import requests
from class_fd.Getprice import Getprice
from openpyxl import load_workbook
from pandas import DataFrame


class Getearningcalendar():
    def __init__(self):
        pass
        # self.start = start
        # self.end = end

    def set_date(self, start, end):
        self.start = start
        self.end = end

    def get_tag(self, list_ip, p_or_f='p'):

        tmp_a_1 = list_ip.split('<th')

        for i, row in enumerate(tmp_a_1[0:]):
            if row.find('display:none') > -1:
                continue

        tb_tags = []

        for i, row in enumerate(tmp_a_1[0:]):
            if row.find('display:none') > -1:
                continue

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

        # 0, company_name, 1, symbol, 2, market_cap, 3, reported_date,
        # 4, fiscal_quarter_ending, 5, consensus_eps_forecast,
        # 6, num_of_ests, 7, eps,  8, surprise

        tmp_c_2 = tmp_c_1[0:3] + tmp_c_1[4:6]
        tmp_c_2.append(tmp_c_1[6] + '_' + tmp_c_1[7] + '_' + tmp_c_1[8])
        tmp_c_2.append(tmp_c_1[9] + '_' + tmp_c_1[10])
        tmp_c_2.append(tmp_c_1[11])
        if p_or_f == 'f':
            tmp_c_2.append(tmp_c_1[12] + '_' + tmp_c_1[13])
        if p_or_f == 'p':
            tmp_c_2.append(tmp_c_1[12])
            tmp_c_2.append(tmp_c_1[13])
        tmp_c_2 = tmp_c_2 + tmp_c_1[14:16]

        # print('tmp_c_2 = ', tmp_c_2)

        return tmp_c_2

    def get_data(self, list_data, p_or_f='p'):
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
                        tmp_size = 'n/a'  # tmp_b_3[0].split('<')[0].strip()
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

    # mm/dd/yyyy to yyyy-month-day e.g.:  01/19/2018 to 2018-Jan-18
    def convert_date(self, date):

        tmp_1 = date.month  # month
        if tmp_1 == 1:
            tmp_1 = 'Jan'
        if tmp_1 == 2:
            tmp_1 = 'Feb'
        if tmp_1 == 3:
            tmp_1 = 'Mar'
        if tmp_1 == 4:
            tmp_1 = 'Apr'
        if tmp_1 == 5:
            tmp_1 = 'May'
        if tmp_1 == 6:
            tmp_1 = 'Jun'
        if tmp_1 == 7:
            tmp_1 = 'Jul'
        if tmp_1 == 8:
            tmp_1 = 'Aug'
        if tmp_1 == 9:
            tmp_1 = 'Sep'
        if tmp_1 == 10:
            tmp_1 = 'Otc'
        if tmp_1 == 11:
            tmp_1 = 'Nov'
        if tmp_1 == 12:
            tmp_1 = 'Dec'

        date_re = str(date.year) + '-' + str(tmp_1) + '-' + str(date.day)
        return date_re

    def get_one_day_list(self, date, filter=0, p_or_f='p'):
        ck_date = date  # mm/dd/yyyy  '01/19/
        ct_date = self.convert_date(ck_date)
        # print('converted date = ', ct_date)
        url_list = 'http://www.nasdaq.com/earnings/earnings-calendar.aspx?date=' + ct_date

        # if it's today, remove the part after question mark
        tmp_1 = ck_date  # datetime.strptime(ck_date, '%m/%d/%Y').date()
        tmp_2 = datetime.now().date()
        if tmp_1 == tmp_2:
            url_list = 'http://www.nasdaq.com/earnings/earnings-calendar.aspx'

        page = requests.get(url_list)
        page_txt = page.text

        tmp_con_1 = page_txt.split('ECCompaniesTable')
        if len(tmp_con_1) > 1:
            tmp_con_1 = tmp_con_1[1]
        else:
            print('Empty')
            return 'null'
        tmp_con_2 = tmp_con_1.split('</table>')[0]
        tmp_con_3 = tmp_con_2.split('<tr>')[1:]

        j = 0

        # get table tags
        for row in tmp_con_3[0:1]:
            # print(row)
            tmp_a_1 = self.get_tag(row, p_or_f)

        # get table data
        list_data = []
        for row in tmp_con_3[1:]:
            list_data.append(self.get_data(row, p_or_f))

        getprice = Getprice()

        list_data_1 = []
        if filter == 1:
            list_data_1 = self.get_filter(list_data)
        else:
            list_data_1 = list_data

        if p_or_f == 'p':
            for i, row in enumerate(list_data_1[0:]):
                # print('row = ', row)
                data_st = getprice.get_diff_dtod(row[1], ck_date)
                if data_st != 'n/a':
                    for j, col in enumerate(data_st):
                        row.append(col)
                    list_data_1[i] = row

        list_cal = list_data_1[0:]

        return list_cal

    def get_calendar_all(self, start, end, filter=0, p_or_f='p'):

        list_cal = []
        list_date = []

        s_year = int(start[6:10])  # '11/08/2017'
        s_month = int(start[0:2])
        s_day = int(start[3:5])

        e_year = int(end[6:10])  # '11/08/2017'
        e_month = int(end[0:2])
        e_day = int(end[3:5])

        d1 = date(s_year, s_month, s_day)  # start date
        d2 = date(e_year, e_month, e_day)  # end date

        # print('d1 = ', d1, 'd2 = ', d2)

        delta = d2 - d1  # timedelta

        for i in range(delta.days + 1):
            list_date.append(d1 + timedelta(days=i))
            # print('delta = ', d1 + timedelta(days=i))

        for i, row in enumerate(list_date[0:]):
            # tmp_2 = datetime.strptime(row, "%m/%d/%Y")
            # if (tmp_2 >= dt_start) & (tmp_2 <= dt_end):
            # print('date = ', row)

            tmp_2 = self.get_one_day_list(row, filter, p_or_f='p')
            if tmp_2 != 'null':
                list_cal = list_cal + tmp_2

        return list_cal

    def get_filter(self, list_data):

        list_re = []
        # 0, company_name, 1, symbol, 2, market_cap, 3, reported_date,
        # 4, fiscal_quarter_ending, 5, consensus_eps_forecast,
        # 6, num_of_ests, 7, eps,  8, surprise, 9, percentage of difference
        # 10, start_price, 11, end_price

        # data example:
        # ['Accuray Incorporated', 'ARAY', '478.34M',
        #  '01/23/2018', 'Dec 2017', '-0.11', '2', '-0.06', '45.45', 7.860262008733628, 5.2, 4.75]

        for i, row in enumerate(list_data[0:]):
            # getprice.set_url(row[1])
            if (float(row[6]) > 10) & (row[5] != 'n/a'):
                if (float(row[5]) > 0) & (row[2].find('B') != -1):
                    list_re.append(row)

        return list_re

    def get_filter2(self, list_data):

        list_re = []
        # 0, company_name, 1, symbol, 2, market_cap, 3, reported_date,
        # 4, fiscal_quarter_ending, 5, consensus_eps_forecast,
        # 6, num_of_ests, 7, eps,  8, surprise, 9, percentage of difference
        # 10, start_price, 11, end_price

        # data example:
        # ['Accuray Incorporated', 'ARAY', '478.34M',
        #  '01/23/2018', 'Dec 2017', '-0.11', '2', '-0.06', '45.45', 7.860262008733628, 5.2, 4.75]

        for i, row in enumerate(list_data[0:]):
            # getprice.set_url(row[1])
            if (float(row[6]) > 10) & (row[5] != 'n/a') & (row[8] != 'n/a'):
                if (float(row[5]) > 0) & (row[2].find('B') != -1) & (float(row[8]) > 0):
                    if float(row[5]) > float(row[8]):
                        list_re.append(row)

        return list_re

    def write_to_xlsx(self, list_data, length):
        success = 0
        file_path = '/datacenter/calendarlist.xlsx'

        # df = DataFrame({})

        labels = ['company_name', 'symbol', 'market_cap', 'reported_date',
                  'fiscal_quarter_ending', 'consensus_eps_forecast',
                  'num_of_ests', 'eps', 'surprise', 'percentage of difference',
                  'end_price', 'end_date', 'start_price', 'start_date']

        df = DataFrame.from_records(list_data, columns=labels[0: length])
        df.to_excel(file_path, sheet_name='sheet1', index=False)

        return success

    def create_write_file(self, filename, list_data):
        success = 1

        file = open('/datacenter/' + filename,'w')
        for row in list_data:
            file.write(row + '\r\n')
        file.close()

        return success

    def read_txt_file(self, filename):

        with open('/datacenter/' + filename) as file:
            data = file.read()

        data_1 = data.split('\n')
        data_2 = data_1[0:(len(data_1) - 1)]

        return data_2

    def read_from_xlsx(self, path):

        # get data from file to DataFrame of pandas

        fpath = path

        wb = load_workbook(filename = fpath)
        # sheet_ranges = wb['Activities']
        ws = wb.active

        df1 = DataFrame(ws.values)

        return df1

    def get_last_eps(self):
        last_eps = 0

        return last_eps
