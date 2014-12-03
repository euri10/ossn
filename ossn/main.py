__author__ = 'euri10'

from scrapy import cmdline
cmdline.execute("scrapy crawl ossn_spider -o items.csv".split())
