# -*- coding: utf-8 -*-

# Scrapy settings for ossn project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ossn'

SPIDER_MODULES = ['ossn.spiders']
NEWSPIDER_MODULE = 'ossn.spiders'
DOWNLOADER_MIDDLEWARES = {'ossn.middlewares.ProxyMiddleware': 1}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ossn (+http://www.yourdomain.com)'
ITEM_PIPELINES = {'ossn.pipelines.OssnPipeline': 1}