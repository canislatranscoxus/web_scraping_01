'''
description: we goto an oreilly course and, get the topics of the course.

'''

import pathlib
import re
import sys
import time
import ws_utils

class CourseTopicScrapper:

    web_site_url   = 'https://www.amazon.com'
    #first_page_url = 'https://www.amazon.com/s/ref=sr_gnr_fkmr0?rh=i%3Aaps%2Ck%3Asusan+polgar&keywords=susan+polgar&ie=UTF8&qid=1542988377'
    #first_page_url = 'C:/aat/data/rice/indian_basmati_rice_list.html'
    #first_page_url = 'file:///C:/aat/data/rice/indian_basmati_rice_list.html'
    #first_page_url = 'https://www.alibaba.com/showroom/indian-basmati-rice.html'
    first_page_url = 'https://www.alibaba.com/products/F0/indian_basmati_rice/----------------------------L.html?spm=a2700.7724857.galleryFilter.7.38532073YAChTF'

    output_dir     = 'c:/aat/data/oreilly/aws_architect_'
    file_name      = 'integrity_training_'



    def scrape_page( self, soup ):
        '''
        use the beautiful soup object, scrape the web page return the data in a post_list array.
        :param soup:
        :return:
        '''
        row_num = 0
        posts_list = []

        try:
            table_of_content = soup.find('div', {'class': 'TableOfContents-TOCPart-R1-Yx'})

            chapters = table_of_content.find_all( 'h3' )


            posts_list = []

            for c in chapters:
                row_num = row_num + 1
                s = c.text

                print( '{} ❥ {} '.format( row_num, c ) )
                posts_list.append( s )

            return posts_list

        except Exception as e:
            error_msg = sys.exc_info()[0]
            print( 'RiceListScrapper.scrape_page(), row_num: {}, error: {}'.format( row_num, error_msg ) )
            raise


    def get_next_page_link( self, n0 ):
        url = None
        try:
            #next_page = soup.find( 'a', {'id': re.compile('pagnNextLink')} )
            #n1 = n0.find('div', {'class': 'l-sub-main-wrap util-clearfix', 'data-widget-cid' :'widget-10'})
            n1 = n0.find('div', {'class': 'l-theme-card-box ns-theme-offer-attr uf-theme-card-border uf-theme-card-margin-bottom'})

            for i in n1.children:
                print( i )

            n2 = n1.find('div', {'data-content': 'abox-Pagination'})
            n3 = n2.find('div', {'class': 'm-pagination util-clearfix'})
            n4 = n3.find('div', {'class': 'util-right util-clearfix'})
            n5 = n4.find('div', {'class': 'ui2 - pagination'})
            n6 = n5.find('div', {'class': 'ui2-pagination-pages'})
            n7 = n6.find('a',   {'class': 'next'})


            #next_page = soup.find('a', {'class': 'next'})
            href      = n5.attrs[ 'href' ]
            url       = self.web_site_url + href

        except Exception as e:
            error_msg = sys.exc_info()[0]
            print( 'RiceListScrapperWebScrapy.get_next_page_link(), error: {}'.format(error_msg) )

        return url


    def run( self ):
        num_page = 0
        try:
            url       = self.first_page_url
            pathlib.Path( self.output_dir  ).mkdir(parents=True, exist_ok=True)

            while url != None:
                num_page    = num_page + 1
                print( '\n page: {}'.format( num_page ) )

                soup        = ws_utils.get_website_parser( url )
                posts_list  = self.scrape_page( soup )
                ws_utils.dic_2_csv( posts_list, self.output_dir, self.file_name, str(num_page).zfill(2) )
                url         = self.get_next_page_link( soup )

                # line: 24639, 24648

                time.sleep( 5 )

        except Exception as e:
            error_msg = sys.exc_info()[0]
            print( '\n\n RiceListScrapper.run(), page:{} , error: {}'.format( num_page, error_msg) )
            print( 'url: {}'.format( url ) )



if __name__ == '__main__':
    try:
       ws = CourseTopicScrapper()
       ws.run()

    except Exception as e:
        error_msg = sys.exc_info()[0]
        print('error: {}'.format(error_msg))



