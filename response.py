#encoding:utf-8
# -*- coding: utf-8 -*-
import requests
from urllib.parse import urlparse

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
class Response:
	def __init__(self,url,method='GET',headers=headers, **kwargs):
		self.host = urlparse(url).scheme+'://'+urlparse(url).netloc
		self.rep = requests.request(url=url,me)
  