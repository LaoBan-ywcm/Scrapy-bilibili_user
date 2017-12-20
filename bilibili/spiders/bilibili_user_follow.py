# -*- coding: utf-8 -*-
import scrapy
import random
import os
import json
import time

from pprint import pprint

from bilibili.items import Bilibili_followItem


class BilibiliUserFollowSpider(scrapy.Spider):
    name = 'bilibili_user_follow'
    allowed_domains = ['api.bilibili.com']
    mid = 0

    def start_requests(self):
            # userAgents = []
            user_follow_url = 'https://api.bilibili.com/x/relation/stat?'
            # with open('/Users/qiuqi/Public/Python/scrapy/bilibili/bilibili/user_agents.txt') as f:
            #     for line in f.readlines():
            #         line = line.strip()[1:-1]
            #         userAgents.append(line)

            for userid in range(42000,52000):
                self.mid = userid
                # userAgent = random.choice(userAgents)
                headers = {
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'User-Agent': '',
                    'Origin': 'https://space.bilibili.com',
                    'Referer': 'https://space.bilibili.com/%s' % userid,
                    'X-Requested-With': 'XMLHttpRequest',
                }
                yield scrapy.Request('%svmid=%s&jsonp=jsonp&callback=__jp2' % (user_follow_url, str(userid)),headers=headers, callback=lambda response, mid=userid: self.bilibili_follow_parse(response, mid))
                time.sleep(random.randint(1, 3))


    def bilibili_follow_parse(self, response, mid):
        item = Bilibili_followItem()
        r = json.loads(response.body.decode()[6:-1])
        # r = json.loads(response.body)
        if response.status == 200 and r['message'] == '成功':
            data = r['data']
            for key in item.fields:
                if key == 'mid':
                    item[key] = mid
                else:
                    item[key] = data[key]
            yield item
