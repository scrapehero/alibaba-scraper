# -*- coding: utf-8 -*-
import scrapy
import csv
import os


class AlibabaCrawlerSpider(scrapy.Spider):
    name = 'alibaba_crawler'
    allowed_domains = ['alibaba.com']
    start_urls = ['http://alibaba.com/']

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
        """Function to process alibaba search results page"""
        search_keyword=response.meta["search_text"]
        products=response.xpath("//div[@class='item-main']")
        # iterating over search results
        for product in products:
            # Defining the XPaths
            XPATH_PRODUCT_NAME=".//div[@class='item-info']//h2[contains(@class,'title')]//a/@title"
            XPATH_PRODUCT_PRICE=".//div[@class='item-info']//div[@class='price']/b/text()"
            XPATH_PRODUCT_MIN_ORDER=".//div[@class='item-info']//div[@class='min-order']/b/text()"
            XPATH_SELLER_YEARS=".//div[@class='item-info']//div[@class='stitle util-ellipsis']//div[contains(@class,'supplier-year')]//text()"
            XPATH_SELLER_NAME=".//div[@class='item-info']//div[@class='stitle util-ellipsis']//a/@title"
            XPATH_SELLER_RESPONSE_RATE=".//div[@class='item-info']//div[@class='sstitle']//div[@class='num']/i/text()"
            XPATH_TRANSACTION_LEVEL=".//div[@class='item-info']//div[@class='sstitle']//a[@class='diamond-level-group']//i[contains(@class,'diamond-level-one')]"
            XPATH_TRANSACTION_LEVEL_FRACTION=".//div[@class='item-info']//div[@class='sstitle']//a[@class='diamond-level-group']//i[contains(@class,'diamond-level-half-filled')]"
            XPATH_PRODUCT_LINK=".//div[@class='item-info']//h2/a/@href"

            raw_product_name=product.xpath(XPATH_PRODUCT_NAME).extract()
            raw_product_price=product.xpath(XPATH_PRODUCT_PRICE).extract()
            raw_minimum_order=product.xpath(XPATH_PRODUCT_MIN_ORDER).extract()
            raw_seller_years=product.xpath(XPATH_SELLER_YEARS).extract()
            raw_seller_name=product.xpath(XPATH_SELLER_NAME).extract()
            raw_seller_response_rate=product.xpath(
                XPATH_SELLER_RESPONSE_RATE).extract()
            raw_transaction_level=product.xpath(
                XPATH_TRANSACTION_LEVEL).extract()
            raw_product_link=product.xpath(XPATH_PRODUCT_LINK).extract()
            # getting the fraction part
            raw_transaction_level_fraction=product.xpath(
                XPATH_TRANSACTION_LEVEL_FRACTION)

            # cleaning the data
            product_name=''.join(raw_product_name).strip(
            ) if raw_product_name else None
            product_price=''.join(raw_product_price).strip(
            ) if raw_product_price else None
            minimum_order=''.join(raw_minimum_order).strip(
            ) if raw_minimum_order else None
            seller_years_on_alibaba=''.join(
                raw_seller_years).strip() if raw_seller_years else None
            seller_name=''.join(raw_seller_name).strip(
            ) if raw_seller_name else None
            seller_response_rate=''.join(raw_seller_response_rate).strip(
            ) if raw_seller_response_rate else None
            # getting actual transaction levels by adding the fraction part
            transaction_level=len(raw_transaction_level)+.5 if raw_transaction_level_fraction else len(raw_transaction_level)
            product_link="https:" + raw_product_link[0] if raw_product_link else None

            yield {
                'product_name': product_name,
                'product_price': product_price,
                'minimum_order': minimum_order,
                'seller_years_on_alibaba': seller_years_on_alibaba,
                'seller_name': seller_name,
                'seller_response_rate': seller_response_rate,
                'transaction_level': transaction_level,
                'product_link': product_link,
                'search_text': search_keyword
            }
