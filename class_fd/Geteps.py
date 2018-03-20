from lxml import html
import requests
from matplotlib import pyplot as plt
from datetime import datetime, date, time
import csv


class Geteps:
    def __init__(self, st_name='DOL'):
        self.st_name = st_name

    def get_data(self, list_1):
        # table tags
        tab_tag_1 = list_1[0]
        tab_tag_2 = tab_tag_1.split('<th>')
        tab_tag_3 = tab_tag_2[1].split('</th>')
        tab_tag_4 = []
        tab_tag_5 = []

        for i, row in enumerate(tab_tag_3[0:4]):
            tmp_t_1 = row.split(">")
            if len(tmp_t_1) > 1:
                tab_tag_4.append(tmp_t_1[1].replace(' ', '_'))
            else:
                tab_tag_4.append(tmp_t_1[0].replace(' ', '_'))

        tab_tag_5.append(tab_tag_4)
        # print('tags: ', tab_tag_4)

        tab_data_1 = list_1[1:]
        list_re = []

        list_data = []

        for j, col in enumerate(tab_data_1):
            # print(j, col)
            tmp_c_1 = col.split('>')
            tmp_c_2 = tmp_c_1[1:8]
            list_row = []
            for l in range(0, len(tmp_c_2), 2):
                tmp_l_1 = tmp_c_2[l].split('<')
                list_row.append(tmp_l_1[0])
            # print(list_row)
            list_data.append(list_row)

        list_re = tab_tag_5 + list_data

        return list_re

    def get_yearly_earning(self):

        g_st_name = self.st_name

        # https://web.tmxmoney.com/earnings.php?qm_symbol=DOL

        # get data from webpage

        url = ''

        if g_st_name == 'DOL':
            url = 'https://web.tmxmoney.com/earnings.php?qm_symbol=DOL'

        page = requests.get(url)
        page_txt = page.text

        page_1 = page_txt.split('Earnings History')
        page_2 = page_1[1].split('More Corporate Earnings')
        page_3 = page_2[0]

        page_4 = page_3.split('<tr>')

        # get the data of quarterly earning

        earning_y = []
        tmp_1 = []
        tmp_1 = self.get_data(page_4)
        earning_y = tmp_1[1:]

        # caculate the yearly earning

        for i, row in enumerate(earning_y):
            print(i, row)

        # 2014.11.18 split 2:1, it's 2014 Q4, so it's Q4
        # the data has been adjusted

        tmp_y_len = len(earning_y)
        tmp_y = []

        for i, row in enumerate(earning_y):
            tmp_four = 0
            if tmp_y_len - i >= 4:
                for j in range(0, 4):
                    tmp_four += float(earning_y[j + i][2])
                tmp_y.append([earning_y[i][1], tmp_four])

        return tmp_y

    def get_last_year_eps(self):
        eps = []

        return eps
