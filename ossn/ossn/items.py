# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OssnItem(scrapy.Item):

    name = scrapy.Field()
    image_url = scrapy.Field()
    #title = scrapy.Field()
    #company= scrapy.Field()
    title_company= scrapy.Field()
    location= scrapy.Field()
    social = scrapy.Field()
    biography_summary = scrapy.Field()
    friends_names= scrapy.Field()
