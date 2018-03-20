# get stock data from the webpage

from lxml import html
import requests
from datetime import date, timedelta, datetime


class Getprice:
    def __init__(self, symbol=''):
        self.url = 'http://www.nasdaq.com/symbol/' + symbol + '/historical'
        # self.hdtg_raw = hdtg_raw
        # self.tb_cont_raw = tb_cont_raw
        self.pickstring = []

    def set_url(self, symbol):
        self.url = 'http://www.nasdaq.com/symbol/' + symbol + '/historical'

    def pick_headtag(self):
        str_1 = self.hdtg_raw
        head_tags = []
        str_2 = str_1.split("<th>")
        for i in range(1, len(str_2)):
            # print(str_2[i])
            temp_1 = str_2[i]
            temp_2 = temp_1.split("<")
            if len(temp_2) == 2:
                head_tags.append(temp_2[0])
            else:
                # print(temp_2[1])
                temp_3 = temp_2[1].split(">")
                head_tags.append(temp_3[1].strip())
        return head_tags

    def pick_tablecontent(self, tb_cont_raw):
        tb_content = []
        tb_1 = tb_cont_raw
        tb_conts = []

        tb_2 = tb_1.split("<tr>")[1:]
        tb_2[len(tb_2) - 1] = tb_2[len(tb_2) - 1].split("</tr>")[0]

        for i in range(0, len(tb_2)):
            # print(i, '  ', tb_2[i])
            temp_1 = tb_2[i].split()
            temp_2 = []
            for j in range(1, len(temp_1), 3):
                # print(j, '  ', temp_2)
                temp_2.append(temp_1[j].replace(',', ''))
            tb_conts.append(temp_2)

        tmp_t_1 = tb_conts[0][0]
        # print(type(tmp_t_1))
        if tmp_t_1.find('td') > -1:
            tb_conts = tb_conts[1:]

        return tb_conts

    def get_price(self, symbol):
        self.url = 'http://www.nasdaq.com/symbol/' + symbol + '/historical'
        page = requests.get(self.url)
        page_txt = page.text

        page_slt_1 = page_txt.split("quotes-left-content")
        page_slt_2 = page_slt_1[1].split("thead")
        pickstring = []

        if len(page_slt_2) >= 3:
            pickstring = self.pick_tablecontent(page_slt_2[2])
            price_dif = (float(pickstring[0][4]) - float(pickstring[15][1]))/float(pickstring[0][4]) * 100
        else:
            price_dif = 'n/a'
        return price_dif

    def get_date_list(self, symbol = 'fb'):

        list_date = []

        self.url = 'http://www.nasdaq.com/symbol/' + symbol + '/historical'
        page = requests.get(self.url)
        page_txt = page.text

        page_slt_1 = page_txt.split("quotes-left-content")
        page_slt_2 = page_slt_1[1].split("thead")

        self.pickstring = self.pick_tablecontent(page_slt_2[2])

        for i, row in enumerate(self.pickstring):
            list_date.append(row[0])
        return list_date

    def get_diff_dtod(self, symbol, date): # date: mm/dd/yyyy

        self.url = 'http://www.nasdaq.com/symbol/' + symbol + '/historical'
        page = requests.get(self.url)
        page_txt = page.text

        page_slt_1 = page_txt.split("quotes-left-content")
        page_slt_2 = page_slt_1[1].split("thead")

        # print(page_slt_2)

        pickstring = []
        index = 0

        list_date = self.get_date_list(symbol)

        tmp_1 = str(datetime.now().month)
        if len(tmp_1) == 1:
            tmp_1 = '0' + str(tmp_1)
        list_date[0] = tmp_1 + '/' + str(datetime.now().day) + '/' + str(datetime.now().year)

        if len(page_slt_2) >= 3:
            pickstring = self.pick_tablecontent(page_slt_2[2])
            index = self.get_index(date, symbol)
            # print('index = ', index)
            if (index + 10) < len(pickstring):
                price_dif = (float(pickstring[index][4]) - float(pickstring[index+10][1]))/float(pickstring[index][4]) * 100
            else:
                price_dif = 'n/a'
        else:
            print(self.url)
            price_dif = 'n/a'

        list_re = []
        if price_dif != 'n/a':
            list_re.append(price_dif)
            list_re.append(list_date[index])
            list_re.append(float(pickstring[index][4]))
            list_re.append(list_date[index+10])
            list_re.append(float(pickstring[index+10][1]))

        return list_re

    def get_index(self, date, symbol):
        # print('get_index = ', date)
        self.get_date_list(symbol)
        for i, row in enumerate(self.pickstring):
            if date == row[0]:
                # print(date, row[0])
                return i
        return 0
