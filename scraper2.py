#importing libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import csv

#Giving the path to fetch 
BRIGHT_STAR_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome("/Users/ISHITA AGGARWAL/Downloads/chromedriver_win32/chromedriver")
page = requests.get(BRIGHT_STAR_URL, verify=False)
print(page)

#Location to find the data 
soup=BeautifulSoup(page.text,'html.parser')
star_table=soup.find('table')
temp_list=[]
table_rows=star_table.find_all('tr')

#Loop
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

#Variables
Star_names = []
Distance =[]
Mass = []
Radius =[]

#Loop
for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])

#Giving csv
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

#Creating the csv file
df2.to_csv('dwarf_stars.csv')