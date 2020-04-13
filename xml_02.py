'''
description : web scraping on xml sitemap
'''

import pathlib
import re
import sys
import time
import ws_utils

import xml.etree.ElementTree as ET

url     = 'https://www.edx.org/sitemap.xml'
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

content = ws_utils.get_website_content( url )

tree = ET.fromstring( content )
print( tree.tag )
print( tree[ 0 ].tag )
print( tree[ 0 ][ 0 ].tag )
print( tree[ 0 ][ 0 ].text )


