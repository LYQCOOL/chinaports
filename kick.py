# _*_ encoding:utf-8 _*_
__author__ = 'LYQ'
__data__ = '2018/8/7 9:47'
import requests
from bs4 import BeautifulSoup
# proxies = {'https': '8.8.8.8:1080'}
response=requests.get('https://www.kickstarter.com/projects/edgeofbelgravia/shiroi-hana-chef-knife-collection-japanese-steel?ref=discovery')
print(response.text)