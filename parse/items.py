# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Import(scrapy.Item):
    title = scrapy.Field()
    name = scrapy.Field()
    date = scrapy.Field()
    division = scrapy.Field()
    finale_one = scrapy.Field()
    finale_x = scrapy.Field()
    finale_two = scrapy.Field()
    tempo_one = scrapy.Field()
    tempo_x = scrapy.Field()
    tempo_two = scrapy.Field()
