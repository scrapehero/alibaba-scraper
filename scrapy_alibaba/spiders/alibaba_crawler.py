# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import csv
import os
from selectorlib import Extractor
import re 

class AlibabaCrawlerSpider(scrapy.Spider):
    name = 'alibaba_crawler'
    allowed_domains = ['alibaba.com']
    start_urls = ['http://alibaba.com/']
    extractor = Extractor.from_yaml_file(os.path.join(os.path.dirname(__file__), "../resources/search_results.yml"))
    max_pages = 5

    def start_requests(self):
        """Read keywords from keywords file amd construct the search URL"""

        with open(os.path.join(os.path.dirname(__file__), "../resources/keywords.csv")) as search_keywords:
            for keyword in csv.DictReader(search_keywords):
                search_text=keyword["keyword"]
                url="https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={0}&viewtype=G".format(
                    search_text)
                # The meta is used to send our search text into the parser as metadata
                yield scrapy.Request(url, callback = self.parse, meta = {"search_text": search_text})


    def parse(self, response):
        data = self.extractor.extract(response.text,base_url=response.url)
        for product in data['products']:
            yield product
        
        # Try paginating if there is data
        if data['products']:
            if '&page=' not in response.url and self.max_pages>=2:
                yield Request(response.request.url+"&page=2")
            else:
                url = response.request.url
                current_page_no = re.findall('page=(\d+)',url)[0]
                next_page_no = int(current_page_no)+1
                url = re.sub('(^.*?&page\=)(\d+)(.*$)',rf"\g<1>{next_page_no}\g<3>",url)
                if next_page_no <= self.max_pages:
                    yield Request(url,callback=self.parse)