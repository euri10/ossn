# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re

class OssnPipeline(object):
    def process_item(self, item, spider):
        #item['name'] clean, can have whitespaces

        clean_name = []
        if item['name']:
            for l in item['name']:
                l = re.sub(r'\s+', '', l)
                clean_name.append(l)
        item['name'] = clean_name
        #
        #
        # pat_title_company = re.compile('(\s+(.*\S),)?\s+(.*\S)\s+')
        # for t in item['title_company']:
        #     item['title'] = pat_title_company.match(t).group(2)
        #     item['company'] = re.sub(r',', '', pat_title_company.match(t).group(3))
        #
        # clean_location = []
        # for loc in item['location']:
        #     loc = re.sub(r',', '', re.sub(r'\s+$','',re.sub(r'^\s+','',loc)))
        #     clean_location.append(loc)
        #
        # #bio re.sub(r'\s+', '', bio)
        return item



