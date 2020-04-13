'''
--------------------------------------------------------------------------------
description : fetch emails from gmail :)

install     : conda install -c conda-forge google-api-python-client
              conda upgrade google-api-python-client

              pip install google-api-python-client



references  : https://developers.google.com/gmail/api/quickstart/python
--------------------------------------------------------------------------------
'''

from apiclient    import discovery, errors
from httplib2     import Http
from oauth2client import file, client, tools
import base64
from bs4 import   BeautifulSoup
import os
import json

'''import getpass
user     = getpass.getpass( 'user:' )
password = getpass.getpass( 'password:' )
print( '{} - {}'.format( user, password ) )
'''
# ----------------------------------------------------------------------------

def get_header( header_name = 'Subject' ):
    headers = m[ 'payload' ][ 'headers' ]
    name  = ''
    value = ''

    print( 'get_header(), headers \n\n' )

    for h in headers:
        name  = h[ 'name' ]
        value = h[ 'value' ]

        print(h)

        if  header_name in name:
            return value

    return ''

# ----------------------------------------------------------------------------

os.chdir( 'C:/aat/data/email_fetching' )
creds_file = 'C:/aat/data/email_fetching/credentials.json'

SCOPES = 'https://www.googleapis.com/auth/gmail.modify'
#SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'


store = file.Storage( 'storage.json' )
creds = store.get()
if not creds or creds.invalid:
    flow  = client.flow_from_clientsecrets( creds_file, SCOPES )
    creds = tools.run_flow( flow, store )

GMAIL = discovery.build( 'gmail', 'v1', http= creds.authorize( Http() ) )


user_id = 'me'
label_id_one = 'INBOX'

inbox_msg = GMAIL.users().messages().list( userId = user_id, labelIds = [ label_id_one ]  ).execute()
inbox_list = inbox_msg[ 'messages' ]


print( '\n The inbox_list \n' )
for i in inbox_list:
    print( i )

print( 'first mail' )
msg = inbox_list[ 0 ]
id  = msg[ 'id' ]
m   = GMAIL.users().messages().get( userId = user_id, id = id ).execute()
#print( json.dumps( m, indent=4 ) )

m_snippet   = m[ 'snippet' ]
m_subject   = get_header( 'Subject' )
m_from      = get_header( 'From' )
m_to        = get_header( 'To' )

print( 'm_snippet: {}'.format( m_snippet ) )
print( 'm_subject: {}'.format( m_subject ) )
print( 'm_from   : {}'.format( m_from    ) )
print( 'm_to     : {}'.format( m_to      ) )


print( '\n\n email_fetching ... end.' )

