#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 21:02:54 2019

@author: shen
"""

import requests
from bs4 import BeautifulSoup
import os
from time import sleep

url = 'https://www.gocomics.com/pearlsbeforeswine'
res1 = requests.get(url)
res1.raise_for_status()
soup1 = BeautifulSoup(res1.text)
date = soup1.select('div.gc-deck.gc-deck--cta-0 a.gc-blended-link.gc-blended-link--primary')[0].get('href')
url1 = 'https://www.gocomics.com/' + date
for i in range(0,10):
    res = requests.get(url1)
    res.raise_for_status()
    soup = BeautifulSoup(res.text)
    
    
    comic_div = soup.select('picture.item-comic-image')
    # find image url
    image_url = comic_div[0].contents[0].attrs['src']
    image_res = requests.get(image_url)
    image_res.raise_for_status()
    
    # save image url
    image_name = soup.select('h1.m-0')[0].contents[0]
    
    image_file = open(image_name + '.jpeg', 'wb')
    for chunk in image_res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()
    
    # get prev url
    prev_link = soup.select('div.gc-calendar-nav__previous')[0].contents[3]
    url1 = 'https://www.gocomics.com' + prev_link.get('href')
    i += 1