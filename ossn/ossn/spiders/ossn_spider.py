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
    rules = (Rule(LxmlLinkExtractor(allow_domains=allowed_domains, restrict_xpaths='.//*[@id="sched-content-inner"]/div[2]/a'),callback='parse_page', follow=True),
            Rule(LxmlLinkExtractor(allow_domains=allowed_domains, restrict_xpaths='.//*[@id="sched-content-inner"]/div[1]/div/div[*]/h2/a'),callback='parse_user'))

    def parse_page(self, response):
        pass

    def parse_user(self, response):
        item = OssnItem()
        name = response.xpath('.//*[@id="sched-page-me-name"]/text()').extract()[0]
        item['name'] = re.sub(r'\s+','',name)
        try:
            item['image_url'] = response.xpath('.//*[@id="myavatar"]/@src').extract()[0]
        except IndexError, e:
            item['image_url'] = None
        try:
            title_company = response.xpath('.//*[@id="sched-page-me-profile-data"]/text()').extract()[0]
            pat_title_company = re.compile('(\s+(.*\S),)?\s+(.*\S)\s+')
            item['title_company'] = response.xpath('.//*[@id="sched-page-me-profile-data"]/text()').extract()
            item['title'] = pat_title_company.match(title_company).group(2)
            item['company'] = pat_title_company.match(title_company).group(3)
        except IndexError, e:
            item['title_company'] = None
            item['title'] = None
            item['company'] = None

        try:
            location = response.xpath('.//*[@id="sched-page-me-profile-data"]/text()').extract()[1]
            item['location'] = re.sub(r'\s+$','',re.sub(r'^\s+','',location))
        except IndexError, e:
            item['location'] = None

        item['social'] = 'social'
        item['biography_summary'] = 'bio'
        item['friends_names'] = 'friends'

        return item

