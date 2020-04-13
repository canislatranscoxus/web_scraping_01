from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())
print( 'soup.a.text         : {}'.format( soup.a.text ) )
print( 'soup.head.title     : {}'.format( soup.head.title ) )
print( 'soup.head.title.text: {}'.format( soup.head.title.text ) )
print( 'soup.body.text      : {}'.format( soup.body.text ) )

print( soup.find( 'a' ) )

print( '\n ------ find all -------- \n' )
for i in soup.find_all( 'a' ):
    print( i.text )