from lxml import html
import requests

# collect info from Reauters.com

class Get_Reuter_Info():

    def __init__(self):
        pass

    def get_webpage(self, symbol = 'FB.O'):

        url_list = 'https://www.reuters.com/finance/stocks/analyst/' + symbol

        page = requests.get(url_list)
        page_txt = page.text
        return page_txt  # webpage text

    def get_recommendation(self, page_txt):

        tmp_1 = page_txt.split('Consensus Recommendation')[2]

        tmp_2 = tmp_1.split('tbody')[0].split('td')

        tmp_rec = tmp_2[1].split('<')[0].replace('>', '')
        tmp_date = tmp_2[7].split('<')[0].replace('>', '')

        return [tmp_rec, tmp_date]

    def get_mean_rating(self, page_txt):

        tmp_1 = page_txt.split('Mean Rating')

        mean_rating = 'n/a'
        if len(tmp_1) >= 2:
            tmp_2 = tmp_1[1]
            tmp_3 = tmp_2.split('tbody')[0]
            tmp_4 = tmp_3.split('>')
            mean_rating = tmp_4[2].split('<')[0]

        return mean_rating