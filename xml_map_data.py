'''
description : get data from a map

site        : https://www.openstreetmap.org

'''

import csv, os, requests, pandas as pd
import sys
import xml.etree.ElementTree as ET

file_name = 'castana_map.osm'


os.chdir(  'c:/aat/data/' )
map_data = ET.parse( file_name )
map_data_root = map_data.getroot()

print( map_data_root )
print( map_data_root[ 25 ].tag )
print( map_data_root[ 25 ].attrib )

print( '\n\n children nodes \n\n' )

for i in range( len( map_data_root ) ):
    node = map_data_root[ i ]

    for j in range( len( node ) ):
        child = node[ j ]

        try:
            if child.tag == 'tag' and child.attrib[ 'k' ] == 'name' :
                print('{} - {} - {}'.format( node.attrib[ 'id' ], child.tag, child.attrib))

        except Exception as e:
            error_msg = sys.exc_info()[0]
            #print( 'ws_utils.get_website_parser(), error: {}'.format(error_msg) )




print( '... end.' )
