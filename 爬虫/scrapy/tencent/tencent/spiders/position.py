#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
# 导入CrawlSpider类和Rule
from scrapy.spiders import CrawlSpider, Rule
# 导入链接规则匹配类，用来提取符合规则的连接
from scrapy.linkextractors import LinkExtractor
from tencent.items import TencentItem

#Spider类的设计原则是只爬取start_url列表中的网页，而CrawlSpider类定义了一些规则(rule)来提供跟进link的方便的机制，从爬取的网页中获取link并继续爬取的工作更适合。
class TencentSpider(CrawlSpider):
    name = "position"
    allow_domains = ["hr.tencent.com"]
    start_urls = ["http://hr.tencent.com/position.php?&start=0#a"]

    # Response里链接的提取规则，返回的符合匹配规则的链接匹配对象的列表
    pagelink = LinkExtractor(allow=("start=\d+"))
    #匹配出start_urls页面里匹配规则的url 请求
    rules = [
        # 获取这个列表里的链接，依次发送请求，并且继续跟进，调用指定回调函数处理
        Rule(pagelink, callback = "parseTencent", follow = True)
    ]

    # 指定的回调函数
    def parseTencent(self, response):
        #如果不设置rule里的follow 默认为false, 获取的url就是start_urls这个页面里匹配的url，不会更近
        '''
        http://hr.tencent.com/position.php?&start=10
        http://hr.tencent.com/position.php?&start=2740
        http://hr.tencent.com/position.php?&start=70
        http://hr.tencent.com/position.php?&start=60
        http://hr.tencent.com/position.php?&start=50
        http://hr.tencent.com/position.php?&start=40
        http://hr.tencent.com/position.php?&start=30
        http://hr.tencent.com/position.php?&start=20
        '''
        """
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentItem()
            # 职位名称
            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['peopleNum'] =  each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]
          
            yield item
       """