# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re


def clean(lst):
    clean_name = []
    if lst:
        for l in lst:
            if re.match('^(\s+)?(.*?)(\s+)$', l) is not None:
                l = re.match('^(\s+)?(.*?)(\s+)$', l).group(2)
            clean_name.append(l)
    return clean_name


class OssnPipeline(object):
    def process_item(self, item, spider):

        item['name'] = clean(item['name'])
        item['location'] = clean(item['location'])
        item['title_company'] = clean(item['title_company'])
        item['biography_summary'] = clean(item['biography_summary'])

        return item



