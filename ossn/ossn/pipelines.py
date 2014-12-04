# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class OssnPipeline(object):
    def process_item(self, item, spider):
        item['name']
        return item
    def remove_leading_space(self,list):
        try:
            for l in list:
            re.sub(r'\s+', '', item)
