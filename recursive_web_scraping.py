'''
description : Do web scraping to amazon web site. Extract data from 5 web pages,
              and save it to CSV files.

inputs      : website_url       = the web site url
              first_page_url    = the url of the first page we want scrape
              output_dir        = the directory where the output csv files will be saved.

site        : www.amazon.com
search      : susan polgar
author      : Canis Latrans Coxus

'''
import pathlib
import re
import sys
import time
import ws_utils

class Web_Scrapy:

    web_site_url   = 'https://www.amazon.com'
    first_page_url = 'https://www.amazon.com/s/ref=sr_gnr_fkmr0?rh=i%3Aaps%2Ck%3Asusan+polgar&keywords=susan+polgar&ie=UTF8&qid=1542988377'
    output_dir     = 'c:/aat/data/susan_polgar'

    def scrape_page( self, soup ):
        '''
        use the beautiful soup object, scrape the web page return the data in a post_list array.
        :param soup:
        :return:
        '''
        row_num = 0
        try:
            row_num    = row_num + 1
            item_list  = soup.find_all('li', {'id': re.compile('result_.+')})
            posts_list = []

            for i in item_list:
                title       = i.find('h2').text
                price       = 0
                price_offer = 0
                try:
                    price = i.find('span', {'class': re.compile('a-offscreen')}).text.replace('$', '')
                    price = float(price)
                except Exception as e:
                    price = 0

                try:
                    a = i.find('a', {'class': re.compile('a-size-small a-link-normal a-text-normal')})
                    price_offer = a.find( 'span', {'class': re.compile('a-size-base a-color-base')}).text.replace('$', '')

                except Exception as e:
                    price_offer = 0

                print('❥ {}. ${} - ${}'.format(title, price, price_offer))

                post_dict = {
                    'p_title'       : title,
                    'price'         : price,
                    'price_offer'   : price_offer
                }
                posts_list.append(post_dict)

            return posts_list

        except Exception as e:
            error_msg = sys.exc_info()[0]
            print( 'WebScrapy.scrape_page(), row_num: {}, error: {}'.format( row_num, error_msg ) )
            raise


    def get_next_page_link( self, soup ):
        url = None
        try:
            next_page = soup.find( 'a', {'id': re.compile('pagnNextLink')} )
            href      = next_page.attrs[ 'href' ]
            url       = self.web_site_url + href

        except Exception as e:
            error_msg = sys.exc_info()[0]
            print( 'WebScrapy.get_next_page_link(), error: {}'.format(error_msg) )

        return url


    def run( self ):
        num_page = 0
        try:
            url       = self.first_page_url
            file_name = 'susan_polgar_page_'
            pathlib.Path( self.output_dir  ).mkdir(parents=True, exist_ok=True)

            while url != None:
                num_page    = num_page + 1

                print( '\n page: {}'.format( num_page ) )

                soup        = ws_utils.get_website_parser( url )
                posts_list  = self.scrape_page( soup )
                ws_utils.dic_2_csv( posts_list, self.output_dir, file_name, str(num_page).zfill(2) )
                url         = self.get_next_page_link( soup )
                time.sleep( 5 )

        except Exception as e:
            error_msg = sys.exc_info()[0]
            print( '\n\n Web_Scrapy.run(), page:{} , error: {}'.format( num_page, error_msg) )
            print( 'url: {}'.format( url ) )
            raise



if __name__ == '__main__':
    try:
       ws = Web_Scrapy()
       ws.run()

    except Exception as e:
        error_msg = sys.exc_info()[0]
        print('error: {}'.format(error_msg))


