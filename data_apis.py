'''
-------------------------------------------------------------------------------
description : scraping data from APIs

site        : https://dog.ceo/dog-api/

-------------------------------------------------------------------------------
'''
import requests, pandas

all_dogs = requests.get( 'https://dog.ceo/api/breeds/list/all' )
content = all_dogs.content
print( '\n content: {}'.format( content ) )

dog_breeds = requests.get( 'https://dog.ceo/api/breeds/list/all' ).json()
print( '\n dog_breeds: {}'.format( dog_breeds ) )

breed = dog_breeds[ 'message' ][ 'bulldog' ]
print( 'bulldog breeds: {}'.format( breed ) )


dog_image_link = 'https://dog.ceo/api/breed/bulldog/images/random'
dog_image = requests.get( dog_image_link ).json()

print( 'dog_image : {}'.format( dog_image ) )

url = dog_image[ 'message' ]
file_name = 'C:/aat/data/perro.jpg'

# download the image to local disk
import urllib.request
urllib.request.urlretrieve( url, file_name )

'''
f = open( file_name , 'w+b')
#byte_arr = [120, 3, 255, 0, 100]
byte_arr = [120, 3, 255, 0, 100] 
binary_format = bytearray(byte_arr)
f.write( binary_format )
f.close() '''


print( 'end.' )