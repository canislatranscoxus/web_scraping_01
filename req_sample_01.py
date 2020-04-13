import requests

url = 'http://fortune.com/fortune500/'
r = requests.get( url )

print( 'status code: {}'.format( r.status_code ) )
print( 'r.encoding : {} \n'.format( r.encoding) )
print( r.content )

'''
print( '\n changing encoding \n' )
r.encoding = 'ISO-8859-1'
print( 'r.encoding : {} \n'.format( r.encoding) )
print( r.content )
'''

