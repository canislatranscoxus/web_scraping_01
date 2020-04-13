'''

description : web scraping on xml
site        : https://www.acm.org/sitemap

'''
import pathlib
import re
import sys
import time
import ws_utils

import pandas

'''
r       = requests.get( url, headers = headers )
#r       = requests.get( url )
html    = r.content

#soup = bs( html, 'html.parser' )
soup    = bs(r.content, "lxml")
'''

#url     = 'https://www.acm.org/sitemap'
url     = 'https://www.edx.org/es/sitemap'
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

soup = ws_utils.get_website_parser( url )

_class = 'view view-sitemap view-id-sitemap view-display-id-page.+'
d = soup.find( 'div', {'class': re.compile( _class  )})

subjects = d.find_all( 'li' )

n = 0
for i in subjects:
    n = n + 1
    text = i.text.replace( '\n', '' )
    print( '{}.- {}'.format( n, text ) )

print( '... end.' )