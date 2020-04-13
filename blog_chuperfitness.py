import csv
import os
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup as bs


def get_text( node ):
    txt = ''
    try:
        txt = node.text.replace( '\n', '' )
    except Exception as e:
        txt = ''
    return txt

def exist(posts_list, p_title):
    for i in posts_list:
        if i[ 'p_title' ] == p_title:
            return True

    return False



url = 'http://chuperfitness.blogspot.com/'


r = requests.get( url )
html = r.content

soup = bs( html, 'html.parser' )

print( '\n' )

# find all the html div tags, with a "class" attribute,
# with value that start with 'article-summary-info'
# and can contain one or more characters after that.
posts = soup.find_all( 'div', { 'class' : re.compile ( 'post' ) } )

posts_list = []

titles = []

for i in posts:

    node = i.find( 'div', re.compile( 'r-snippetized' ) )
    if node == None:
        continue

    p_title = get_text( node )
    if exist( posts_list, p_title ):
        continue

    node = i.find( 'time', { 'class' : re.compile ( 'published' ) } )
    if node != None:
        p_date = get_text( node )

    post_dict = {
                    'p_title'  : p_title,
                    #'p_author' : p_author,
                    'p_date'   : p_date
                 }

    print( '❥ {}. {}'.format( p_title , p_date ) )
    posts_list.append( post_dict )


# save extracted data to file
file_name_1 = 'chuperFitness_01.csv'
file_name_2 = 'chuperFitness_02.csv'

df = pd.DataFrame( posts_list )
os.chdir( 'c:/aat/data' )

# method 1 to write csv - using pandas
df.to_csv( file_name_1 )

# method 2 to write csv - using os library

keys = posts_list[ 0 ].keys()
with open( file_name_1, 'w' ) as output_file:
    dict_writer = csv.DictWriter( output_file, keys )
    dict_writer.writeheader()
    dict_writer.writerows( posts_list )

print( 'files created: \n* c:/aat/data/{}\n* c:/aat/data/{} \n\n'.format( file_name_1, file_name_2) )