# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log
import json

class BilibiliPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'bilibili_user':
            with open('bilibili_user_info.json', 'a+') as f:
                f.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
            return item
        elif spider.name == 'bilibili_user_follow':
            with open('bilibili_user_follow.json', 'a+') as f:
                f.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
            return item
