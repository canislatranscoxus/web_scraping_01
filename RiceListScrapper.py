'''
---------------------------------------------------------------------------------------------------
description : Do web scraping to alibaba web site. Extract data from 5 web pages,
              and save it to CSV files.

inputs      : website_url       = the web site url
              first_page_url    = the url of the first page we want scrape
              output_dir        = the directory where the output csv files will be saved.

site        : www.alibaba.com
search      : indian basmati rice
author      : Canis Latrans Coxus
---------------------------------------------------------------------------------------------------
'''
import pathlib
import re
import sys
import time
import ws_utils

class RiceListScrapper:

    web_site_url   = 'https://www.amazon.com'
    #first_page_url = 'https://www.amazon.com/s/ref=sr_gnr_fkmr0?rh=i%3Aaps%2Ck%3Asusan+polgar&keywords=susan+polgar&ie=UTF8&qid=1542988377'
    #first_page_url = 'C:/aat/data/rice/indian_basmati_rice_list.html'
    #first_page_url = 'file:///C:/aat/data/rice/indian_basmati_rice_list.html'
    #first_page_url = 'https://www.alibaba.com/showroom/indian-basmati-rice.html'
    first_page_url = 'https://www.alibaba.com/products/F0/indian_basmati_rice/----------------------------L.html?spm=a2700.7724857.galleryFilter.7.38532073YAChTF'

    output_dir     = 'c:/aat/data/rice/out'
    file_name      = 'indian_basmati_rice_page_'


    def get_features(self, parent_node ):
        d = {}
        i = 0
        try:
            nodes = parent_node.find_all('div', {'class': 'kv'})

            for n in nodes:
                #print( n )
                i = i + 1
                a   = n.attrs[ 'title' ].lower().split( ':' )
                key = a[ 0 ].strip( ).replace( ' ', '_' )
                val = a[ 1 ].replace( ' ', '' )
                d[ key ]= val

            return d
        except Exception as e:
            error_msg = sys.exc_info()[0]
            print('RiceListScrapper.get_features(), product: {}, error: {}'.format(i, error_msg))
            raise

    def copy_features(self, src, tar):
        try:
            if 'kind' in src:
                tar[ 'kind'] = src['kind']

            if 'color' in src:
                tar[ 'color' ] = src['color']

            if 'style' in src:
                tar[ 'style' ] = src['style']

            if 'variety' in src:
                tar[ 'variety' ] = src['variety']

            if 'cultivation_type' in src:
                tar[ 'cultivation_type' ] = src['cultivation_type']

            if 'texture' in src:
                tar[ 'texture' ] = src['texture']

        except Exception as e:
            error_msg = sys.exc_info()[0]
            print('\t *** RiceListScrapper.copy_features(), error {}'.format( error_msg ))



    def scrape_page( self, soup ):
        '''
        use the beautiful soup object, scrape the web page return the data in a post_list array.
        :param soup:
        :return:
        '''
        row_num = 0
        try:

            #item_list  = soup.find_all('li', {'id': re.compile('result_.+')})

            item_list = soup.find_all('div', {'class': 'item-content'})
            posts_list = []

            for i in item_list:
                row_num = row_num + 1

                d = {
                    'title'             : '',
                    'price'             : '',
                    'min_order'         : '',
                    'kind'              : '',

                    'color'             : '',
                    'style'             : '',
                    'variety'           : '',
                    'cultivation_type'  : '',
                    'texture'           : ''

                }

                title_content = i.find('h2', {'class': 'title'})
                a = title_content.find('a')
                d[ 'title' ] = a.text

                try:
                    price_content = i.find( 'div', { 'class' : 'price' } )
                    b = price_content.find( 'b' )
                    d['price'] = b.text.replace( '\n', '' ).replace( ' ', '' )
                except Exception as e1:
                    d['price'] = ''

                try:
                    min_order_content   = i.find( 'div', { 'class' : 'min-order' } )
                    b = min_order_content.find('b')
                    d['min_order'] = b.text
                except Exception as e2:
                    d['min_order'] = ''


                features_node = i.find('div', {'class': 'kv-prop'})
                features      = self.get_features( features_node )
                self.copy_features( features, d )


                print( '{}❥ {}. ${}, {}, {}, {}, {}, {}, {}, {}'.format( row_num,
                    d['title'], d['price'], d['min_order'] ,
                    d['kind'],
                    d[ 'color'], d['style'], d['variety'], d['cultivation_type'], d['texture'] ) )


                '''
                post_dict = {
                    'title'     : title,
                    'price'     : price,
                    'min_order' : min_order,
                    'kind'      : kind
                }
                '''
                posts_list.append(d)

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
                #posts_list  = self.scrape_page( soup )
                #ws_utils.dic_2_csv( posts_list, self.output_dir, self.file_name, str(num_page).zfill(2) )
                url         = self.get_next_page_link( soup )

                # line: 24639, 24648

                time.sleep( 5 )

        except Exception as e:
            error_msg = sys.exc_info()[0]
            print( '\n\n RiceListScrapper.run(), page:{} , error: {}'.format( num_page, error_msg) )
            print( 'url: {}'.format( url ) )



if __name__ == '__main__':
    try:
       ws = RiceListScrapper()
       ws.run()

    except Exception as e:
        error_msg = sys.exc_info()[0]
        print('error: {}'.format(error_msg))


