import csv
import os
import pandas as pd
import sys

import re
import requests
from bs4 import BeautifulSoup as bs

def save_2_csv( posts_list, file_name_1, file_name_2 ):
    '''
    save extracted data to 2 CSV file. For learning purposes we show 2 methods.
    One method is using pandas data frame and the other is with os library.

    :param posts_list:
    :param file_name_1:
    :param file_name_2:
    :return:
    '''

    try:

        df = pd.DataFrame(posts_list)
        os.chdir('c:/aat/data')

        # method 1 to write csv - using pandas
        df.to_csv( file_name_1, index = False )

        # method 2 to write csv - using os library

        keys = posts_list[0].keys()
        with open(file_name_2, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(posts_list)

        print('files created: \n* c:/aat/data/{}\n* c:/aat/data/{} \n\n'.format(file_name_1, file_name_2))

    except Exception as e:
        error_msg = sys.exc_info()[0]
        print('error: {}'.format(error_msg))


def dic_2_csv( posts_list, output_dir, file_name, num_page ):
    '''
    save a dictionary of rows as a CSV file.
    :param posts_list:
    :param file_name:
    :param num_page:
    :return:
    '''
    try:
        df = pd.DataFrame(posts_list)
        os.chdir( output_dir )

        # method 1 to write csv - using pandas
        df.to_csv( file_name + '_' + num_page + '.csv', index = False )
    except Exception as e:
        error_msg = sys.exc_info()[0]
        print( 'ws_utils.dic_2_csv(), error: {}'.format( error_msg ) )

def get_website_parser( url ):
    '''
    open a website and return the beautiful soup parser.
    :param url:
    :return:
    '''
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

        r = requests.get(url, headers=headers)
        html = r.content

        #soup = bs( html, 'html.parser' )
        soup = bs(r.content, "lxml")
        return soup
    except Exception as e:
        error_msg = sys.exc_info()[0]
        print( 'ws_utils.get_website_parser(), error: {}'.format(error_msg) )

    try:
        soup = bs(open( url ), 'html.parser' )
        return soup
    except Exception as e:
        raise



def get_website_content( url ):
    '''
    open a website and return the beautiful soup parser.
    :param url:
    :return:
    '''
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

        r = requests.get(url, headers=headers)
        return  r.content

    except Exception as e:
        error_msg = sys.exc_info()[0]
        print( 'ws_utils.get_website_parser(), error: {}'.format(error_msg) )
        raise
