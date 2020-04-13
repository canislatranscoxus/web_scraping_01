'''
------------------------------------------------------------------------------------
description : Web scrape one page from a shopping site and extract from a catalog,
              the product name and price

site        : amazon
search      : qiyi cube 3x3x3

references  :
            https://stackoverflow.com/questions/23555283/why-cant-i-scrape-amazon-by-beautifulsoup
------------------------------------------------------------------------------------
'''

import csv
import os
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup as bs

import ws_utils

url     = 'https://www.amazon.com/s/s/ref=sr_nr_p_89_3?fst=as%3Aoff%2Cp90x%3A1&rh=i%3Aaps%2Ck%3Aqiyi+cube+3x3%2Cp_89%3AQIYI&keywords=qiyi+cube+3x3&ie=UTF8&qid=1542658042&rnid=2528832011'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

r       = requests.get( url, headers = headers )
html    = r.content

#soup = bs( html, 'html.parser' )
soup    = bs(r.content, "lxml")

print( 'before search....  \n' )


#n_00 = soup.find_all( 'div', { 'id' : re.compile ( 'a-page' ) } )
#n_01 = n_00[0].find( 'div', { 'id' : re.compile ( 'search-main-wrapper' ) } )

item_list = soup.find_all( 'li', { 'id' : re.compile ( 'result_.+' ) } )
#posts = soup.find_all( 'div', { 'class' : 'a-fixed-left-grid-col a-col-right'  } )
#posts = soup.find_all( 'div', { 'class' : re.compile ( 'a-fixed-left-grid-col.a-col-right' ) } )


posts_list = []

print( 'begin loop...' )

for i in item_list :
    title = i.find( 'h2' ).text
    price = 0

    try:
        price = i.find( 'span', { 'class': re.compile( 'a-offscreen'  ) } ).text.replace( '$', '' )
        price = float( price )

    except Exception as e:
        price = 0

    print( '❥ {}. ${}'.format( title , price ) )

    post_dict = {
                    'p_title'  : title,
                    'price'    : price
                }

    posts_list.append( post_dict )


file_name_1 = 'amazon_1.csv'
file_name_2 = 'amazon_2.csv'
ws_utils.save_2_csv( posts_list, file_name_1, file_name_2 )

print( 'end.' )


