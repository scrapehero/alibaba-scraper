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

## Sample Output 
| product_name                                                                                                        | product_price      | minimum_order | seller_years_on_alibaba | seller_name                                    | seller_response_rate | transaction_level | product_link                                                                                                | search_text |
|---------------------------------------------------------------------------------------------------------------------|--------------------|---------------|-------------------------|------------------------------------------------|----------------------|-------------------|-------------------------------------------------------------------------------------------------------------|-------------|
| high quality wireless bluetooth headphone   bluetooth sport wireless with mic                                       | US $4.90-$5.40     | 500 Pieces    | 1 YR                    | Shantou City Liangying Industrial Ltd.         | 97.40%               | 2                 | https://www.alibaba.com/product-detail/high-quality-wireless-bluetooth-headphone-bluetooth_60774817269.html | headphones  |
| RadioEar B71W bone conduction headphones   for audiometer, B71W Bone Transducer Headset                             | US $275.00-$290.00 | 1 Piece       | 6YRS                    | Guangzhou Melison Medical Instrument Co., Ltd. | 87.00%               | 1.5               | https://www.alibaba.com/product-detail/RadioEar-B71W-bone-conduction-headphones-for_805556758.html?s=p      | headphones  |
| SODO Flip Speaker Headphone Wholesale OEM   Over Ear Sport Mobile Bluetooth Wireless Headphone                      | US $18.80-$25.00   | 4 Pieces      | 4YRS                    | Shenzhen Ditmo Electronic Technology Co., Ltd. | 92.70%               | 3                 | https://www.alibaba.com/product-detail/SODO-Flip-Speaker-Headphone-Wholesale-OEM_60740074052.html?s=p       | headphones  |
| August over ear bluetooth wireless stereo   headphones with EQ APP Control Bass Rich Sound Headset with NFC/aptX-LL | US $23.20-$29.76   | 10 Pieces     | 1 YR                    | Shenzhen August Digital Ltd.                   |                      | 0                 | https://www.alibaba.com/product-detail/August-over-ear-bluetooth-wireless-stereo_60815054687.html?s=p       | headphones  |
| LED light silent disco headphones RF-309                                                                            | US $10.00-$30.00   | 100 Pieces    | 13YRS                   | Shenzhen Go-On Electronics Co., Ltd.           | 77.90%               | 0.5               | https://www.alibaba.com/product-detail/LED-light-silent-disco-headphones-RF_1316830410.html?s=p             | headphones  |

## Learn more about the scraper 
You can read more on how this scraper was built 
