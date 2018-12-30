# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LhcSpiderItem(scrapy.Item):
    id = scrapy.Field()
    qs = scrapy.Field()
    year = scrapy.Field()
    month = scrapy.Field()
    day = scrapy.Field()
    cc = scrapy.Field()
    type = scrapy.Field()
    sx_card = scrapy.Field()


