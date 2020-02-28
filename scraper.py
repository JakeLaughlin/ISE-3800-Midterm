# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:31:23 2020

ISE 3800 Web scraper project 

@author: Laughlin
"""


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

path = "https://www.unitedstateszipcodes.org/"

zipcode = input("Enter zip code: ")

path = path+str(zipcode)+"/"
print(path)