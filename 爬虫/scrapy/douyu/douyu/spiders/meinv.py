# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem


class MeinvSpider(scrapy.Spider):
    name = 'meinv'
    allowed_domains = ['capi.douyucdn.cn']
    
    offset = 0
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    start_urls = [url + str(offset)]

    def parse(self, response):
        
        res = json.loads(response.text)
        for each in res['data']:
            item = DouyuItem()
            item["nickname"] = each["nickname"]
            item["imagelink"] = each["vertical_src"] 
            yield item
            
        self.offset += 20
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)