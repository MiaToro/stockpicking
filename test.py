# import random
# from lxml import html
# import requests
import requests

print(sum(i*i for i in range(10)))                 # sum of squares


xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))       # dot product


from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}

print(sine_table)

page = ['1', '2', '3', '4']

print(set(page))

unique_words = set(word for line in page for word in line.split())

print(unique_words)

# valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))

# class Reverse:
#     """Iterator for looping over a sequence backwards."""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
#
#
# rev = Reverse('spam')
# print(iter(rev))

# for char in rev:
#     print(char)


# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
#
# x = Complex(3.0, -4.5)
#
# x.counter1 = 1
# while x.counter1 < 10:
#     x.counter1 = x.counter1 * 2
# print(x.counter1)
# del x.counter1
#
# #
# def scope_test():
#     def do_local():
#         spam = "local spam"
#
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#
#     def do_global():
#         global spam
#         spam = "global spam"
#
#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)
#
# scope_test()
# print("In global scope:", spam)

# symbol = 'fb'
# url = 'https://www.reuters.com/finance/stocks/analyst/AMZN.O'
# page = requests.get(url)
# page_txt = page.text
#
# print(page_txt)

#
# file = open('/datacenter/testfile.txt','w')
# file.write('Hello World \r\n')
# file.close()
#
# with open('/datacenter/symbols.txt') as file:
#     data = file.read()
#
# data_1 = data.split('\n')
# print(data_1[0:(len(data_1) - 1)])

# datelist = pd.date_range(pd.datetime.today(), periods=100).tolist()
#
# for i, row in enumerate(datelist[0:]):
#     print(i, row)

# d1 = date(2018, 1, 29)  # start date
# 
# print('d1 = ', type(d1), d1)
# d2 = date(2018, 1, 29)  # end date
# 
# delta = d2 - d1  # timedelta
# 
# for i in range(delta.days + 1):
#     print('dayth = ', d1 + timedelta(days=i))
# 
# start = '01/29/2018'
# tmp_1 = datetime.strptime(start, '%m/%d/%Y').date()
# tmp_2 = datetime.now().date()
# 
# print('datetime.now = ', type(tmp_1), type(tmp_2))

# if tmp_1 == tmp_2:
#     url_list = 'http://www.nasdaq.com/earnings/earnings-calendar.aspx'
#     print(url_list)

# print(round(5.46))

# import dryscrape
# from bs4 import BeautifulSoup

# pick_int = []
#
# for i in range(0, 20):
#     p = random.randint(0, 65)
#     if p in pick_int:
#         pass
#     else:
#         pick_int.append(p)
#     if len(pick_int) > 9:
#         break
#
# print(pick_int)
#

# #
# url = 'https://web.tmxmoney.com/pricehistory.php?qm_page=10267&qm_symbol=AMZN:US'

#
# page = requests.get(url)
# page_txt = page.text
#
# print(page_txt)

#
# session = dryscrape.Session()
# session.visit(url)
# response = session.body()
# soup = BeautifulSoup(response)
# soup.find(id="intro-text")

# from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.get(url)
# # driver.execute_script('document.title')
