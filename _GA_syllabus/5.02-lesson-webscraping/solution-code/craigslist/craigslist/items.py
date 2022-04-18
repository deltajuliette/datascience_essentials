# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CraigslistItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    # copied from intro-to-web-scraping:
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
