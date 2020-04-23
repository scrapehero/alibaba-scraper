# Scrape Alibaba.com search results using Scrapy

A scrapy spider to extract the following fields from any search result page of alibaba.com. For example https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=headphones

## Fields

The scraper will extract the following fields 
- Product Name
- Price Range
- Product Image
- Link to Product
- Minimum Order
- Seller Name
- Seller Response Rate
- Number of years as a seller on Alibaba

## Requirements 
- Python 3 
- Scrapy
- Selectorlib 

## Running the Scraper

1. Add search keyword to [keywords.csv](https://github.com/scrapehero/alibaba-scraper/blob/master/scrapy_alibaba/resources/keywords.csv)
1. Modify max_pages variable from [alibaba_crawler.py](scrapy_alibaba/spiders/alibaba_crawler.py), to the maximum number of pages to scrape data from. The default is 5 pages.
1. Run command `scrapy crawl alibaba_crawler -o out.csv -t csv` to get data as CSV into a file called out.csv or `scrapy crawl alibaba_crawler -o out.json -t json` to get data as JSON File. 

## Sample Output 

|name                                                                                                                                                         |price        |seller_name                                        |seller_years|seller_response_rate|image                                                                           |link                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|---------------------------------------------------|------------|--------------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
|New private model fashion promotion wireless charging function X6 Pixart PAU1603 wireless Earphone earphone headphone for sports                             |$12.05-$13.85|Shenzhen Eriwin Technology Limited                 |11 YRS      |                    |https://s.alicdn.com/@sc01/kf/H6d02bc74346b4c65ac095201bf8c3a0e0.jpg_300x300.jpg|https://www.alibaba.com/product-detail/New-private-model-fashion-promotion-wireless_62393635559.html       |
|The Great Bass Sound Noise Cancelling Headphone                                                                                                              |$14.00-$17.00|Guangzhou Artiste Technology Co., Ltd.             |7 YRS       |86.1%               |https://img.alicdn.com/tfs/TB1S_7kkY5YBuNjSspoXXbeNFXa-700-700.jpg_350x350.jpg  |https://www.alibaba.com/product-detail/The-Great-Bass-Sound-Noise-Cancelling_62446550917.html?s=p          |
|Bluetooth Headphone Ear over Ear Comfortable Protein Earpad Matte Finish Premium Rechargeable Bulit-In Mic Foldable Wirele Headphone Headset                 |$4.70-$6.00  |Shenzhen Zhongxu Electronics Technology Co., Ltd.  |7 YRS       |91.8%               |https://img.alicdn.com/tfs/TB1S_7kkY5YBuNjSspoXXbeNFXa-700-700.jpg_350x350.jpg  |https://www.alibaba.com/product-detail/Bluetooth-Headphone-Ear-over-Ear-Comfortable_62282896949.html?s=p   |
|Bluetooth Headphone Earphone in Ear Wireless Earphones Mini in Ear Tws Fone De Ouvido Wireless Bluetooth Handsfree Magnetic Earbud Headphone Earphone Headset|$2.79-$29.99 |Dongguan Youtuo Electronic Technology Co., Ltd.    |1 YRS       |91.9%               |https://img.alicdn.com/tfs/TB1S_7kkY5YBuNjSspoXXbeNFXa-700-700.jpg_350x350.jpg  |https://www.alibaba.com/product-detail/Bluetooth-Headphone-Earphone-in-Ear-Wireless_62350522248.html?s=p   |
|3 channel Silent Disco Headphone for silent party with LED lights                                                                                            |$10.00-$30.00|Shenzhen Go-On Electronics Co., Ltd.               |15 YRS      |82.3%               |https://img.alicdn.com/tfs/TB1S_7kkY5YBuNjSspoXXbeNFXa-700-700.jpg_350x350.jpg  |https://www.alibaba.com/product-detail/3-channel-Silent-Disco-Headphone-for_2015692880.html?s=p            |

## Learn more about the scraper 
You can read more on how this scraper was built here https://www.scrapehero.com/scrape-alibaba-using-scrapy/
