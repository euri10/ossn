__author__ = 'euri10'

from scrapy import cmdline
cmdline.execute("scrapy crawl ossn_spider --set FEED_URI=output.csv --set FEED_FORMAT=csv --set CSV_DELIMITER=';'".split())