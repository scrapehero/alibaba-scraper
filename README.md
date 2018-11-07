# Scrape Alibaba.com search results using Scrapy

A scrapy spider to extract the following fields from any search result page of alibaba.com. For example https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=headphones

## Fields

The scraper will extract the following fields 
- Product Name
- Price Range (in US dollars)
- Minimum Order
- Seller Name
- Seller Response Rate
- Number of years as a seller on Alibaba
-Transactional Level

## Requirements 
- Python 3 
- Scrapy

## Running the Scraper

1. Add search keyword to [keywords.csv](https://github.com/scrapehero/alibaba-scraper/blob/master/scrapy_alibaba/resources/keywords.csv)
2. Run command `scrapy crawl alibaba_crawler -o out.csv -t csv` to get data as CSV into a file called out.csv or `scrapy crawl alibaba_crawler -o out.json -t json` to get data as JSON File. 

## Learn more about the scraper 
You can read more on how this scraper was built 
