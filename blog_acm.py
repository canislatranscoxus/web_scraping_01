import csv
import os
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup as bs

url = 'https://cacm.acm.org/blogs/blog-cacm/'

r = requests.get( url )
html = r.content

soup = bs( html, 'html.parser' )

print( '\n' )

# find all the html div tags, with a "class" attribute,
# with value that start with 'article-summary-info'
# and can contain one or more characters after that.
posts = soup.find_all( 'div', { 'class' : re.compile ( 'article-summary-info.+' ) } )

posts_list = []

for i in posts:
    p_title  = i.h4.a.text
    p_author = i.find( 'span', re.compile( 'byline.+' ) ).em.text
    p_date   = i.find( 'span', re.compile( 'byline.+' ) ).text.split('|')[1]
    print( '❥ {}. {}. {}'.format( p_title , p_author, p_date ) )

    post_dict = {
                    'p_title'  : p_title,
                    'p_author' : p_author,
                    'p_date'   : p_date
                 }

    posts_list.append( post_dict )

df = pd.DataFrame( posts_list )
os.chdir( 'c:/aat/data' )

# method 1 to write csv - using pandas
df.to_csv( 'posts_01.csv' )

# method 2 to write csv - using os library

keys = posts_list[ 0 ].keys()
with open( 'posts_02.csv', 'w' ) as output_file:
    dict_writer = csv.DictWriter( output_file, keys )
    dict_writer.writeheader()
    dict_writer.writerows( posts_list )

print( 'files created: \n* c:/aat/data/post_01.csv\n* c:/aat/data/post_02.csv \n\n' )