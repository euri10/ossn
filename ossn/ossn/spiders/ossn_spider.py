__author__ = 'euri10'


from ossn.items import OssnItem
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.spiders import Rule, CrawlSpider
import re
from ConfigParser import SafeConfigParser

class ossnSpider(CrawlSpider):
    parser = SafeConfigParser()
    parser.read('config.ini')
    allowed = parser.get('site_settings', 'allowed')
    start = parser.get('site_settings', 'start')

    name = "ossn_spider"
    allowed_domains = [allowed]

    start_urls = [start]
    rules = (Rule(LxmlLinkExtractor(allow_domains=allowed_domains, restrict_xpaths='.//*[@id="sched-content-inner"]/div[2]/a'),callback='parse_page', follow=False),
            Rule(LxmlLinkExtractor(allow_domains=allowed_domains, restrict_xpaths='.//*[@id="sched-content-inner"]/div[1]/div/div[*]/h2/a'),callback='parse_user'))

    def parse_page(self, response):
        pass

    def parse_user(self, response):
        item = OssnItem()

        item['name'] = response.xpath('.//*[@id="sched-page-me-name"]/text()').extract()
        item['image_url'] = response.xpath('.//*[@id="myavatar"]/@src').extract()
        #item['title_company'] = response.xpath('.//*[@id="sched-page-me-profile-data"]/text()').extract()
        item['title_company'] = response.xpath('.//*[@id="sched-page-me-profile-data"]/br/preceding-sibling::text()').extract()
        item['location'] = response.xpath('.//*[@id="sched-page-me-profile-data"]/br/following-sibling::text()').extract()
        item['social'] = response.xpath('.//*[@id="sched-page-me-networks"]/div/a/@href').extract()
        item['biography_summary'] = response.xpath('.//*[@id="sched-page-me-profile-about"]/text()').extract()
        item['friends_names'] = response.xpath('.//*[@id="sched-page-me-connections"]/ul/li[*]/a/@title').extract()

        return item

