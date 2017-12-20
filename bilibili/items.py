# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    article = scrapy.Field()
    birthday = scrapy.Field()
    coins = scrapy.Field()
    name = scrapy.Field()
    mid = scrapy.Field()
    place = scrapy.Field()
    # 注册时间
    regtime = scrapy.Field()
    sex = scrapy.Field()
    sign = scrapy.Field()
    # 视屏播放数
    playNum = scrapy.Field()
    currentLevel = scrapy.Field()

class Bilibili_followItem(scrapy.Item):
    mid = scrapy.Field()
    # 被关注了多少
    follower = scrapy.Field()
    # 关注了多少
    following = scrapy.Field()
