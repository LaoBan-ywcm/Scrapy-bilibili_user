# -*- coding: utf-8 -*-
import scrapy
import random
import os
import json
import time

from pprint import pprint

from bilibili.items import BilibiliItem

class BilibiliUserSpider(scrapy.Spider):
    name = 'bilibili_user'
    allowed_domains = ['space.bilibili.com']

    def start_requests(self):
        userAgents = []
        user_info_url = 'https://space.bilibili.com/ajax/member/GetInfo'
        # with open('/Users/qiuqi/Public/Python/scrapy/bilibili/bilibili/user_agents.txt') as f:
        #     for line in f.readlines():
        #         line = line.strip()[1:-1]
        #         userAgents.append(line)

        for userid in range(32000,42000):
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
            body = {
                'mid': str(userid),
                'csrf': 'null',
            }
            yield scrapy.FormRequest(user_info_url, headers=headers, formdata=body, callback=self.bilibili_parse)
            time.sleep(random.randint(1, 3))


    def bilibili_parse(self, response):
        item = BilibiliItem()
        r = json.loads(response.body)
        if response.status == 200 and r['status'] != False:
            data = r['data']
            for key in item.fields:
                if key == 'currentLevel':
                    item[key] = data['level_info']['current_level']
                else:
                    item[key] = data[key] if key in data.keys() else 'no'
            yield item
        else:
            return

