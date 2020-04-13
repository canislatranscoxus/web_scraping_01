'''
description: demo using the selenium library. This is for interacting with the web page, open a web browser,
                send keystrokes, click objects, click buttons, get data ...

            to extract data from web page we can use beautiful soup
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support     import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time
from bs4 import BeautifulSoup
import re
import pandas

url_mt  = 'https://www.amazon.com/s/ref=nb_sb_ss_c_3_16?url=search-alias%3Ddigital-text&field-keywords=navy+seal+mental+toughness&rh=n%3A133140011%2Ck%3Anavy+seal+mental+toughness'
url     = 'https://www.amazon.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}


driver  = webdriver.Chrome( 'C:/aat/chromedriver_win32/chromedriver.exe' )
driver.get( url )

print( 'driver: {}'.format( driver.title ) )

'''
ID                = "id"
XPATH             = "xpath"
LINK_TEXT         = "link_text"
PARTIAL_LINK_TEXT = "partial_link_text"
NAME              = "name"
TAG_NAME          = "name"
CLASS_NAME        = "class_name"
CSS_SELECTOR      = "css selector"
'''
# ----------------------------------------------------------------------------
# search element by id
search_ddbox    = driver.find_element_by_id( 'searchDropdownBox' )
search_ddbox.send_keys( 'k' )
search_ddbox.send_keys( Keys.RETURN )

#driver.find_element_by_class_name( 'next' )

search_text_box = driver.find_element_by_id( 'twotabsearchtextbox' )
search_text_box.send_keys( 'navy seal mental toughness' )
search_text_box.send_keys( Keys.RETURN )

# ----------------------------------------------------------------------------
# navigate backward or fordward
driver.back()
driver.forward()

# search element by class

# ----------------------------------------------------------------------------
# search element by XPATH
driver.back()

element = driver.find_element( By.XPATH, '//*[@id = "searchDropdownBox"]'  )
select = Select( element )
select.select_by_visible_text( 'Sports & Outdoors' )

element_textbox = driver.find_element( By.XPATH, '//*[@id = "twotabsearchtextbox"]'  )
element_textbox.send_keys( 'hand grip strenght' )
element_textbox.send_keys( Keys.RETURN )
# ----------------------------------------------------------------------------

# find elements

ddbox_01 = driver.find_element_by_class_name( 'nav-search-dropdown' )
#ddbox_02 = driver.find_element( By.CLASS_NAME, 'nav-search-dropdown' )
ddbox_03 = driver.find_element_by_name( 'url' )
# ----------------------------------------------------------------------------

# get the html source
html = driver.page_source

'''
# to do web scraping, we use beautiful soup, like we do it in:
    
    * blog_acm.py, 
    * blog_chupperfitness.py, 
    * ecommerce_01.py,
    * ws_utils.py, ...
    
'''

soup = BeautifulSoup( html, 'html.parser' )

# more code here ...

# ----------------------------------------------------------------------------

driver.close()
print( 'end' )