# -*- coding: utf-8 -*-
import scrapy
import re
from tencent.items import TencentItem


class PositionSpider(scrapy.Spider):
    name = 'position'
    allowed_domains = ['tencent.com']
    url = 'http://hr.tencent.com/position.php?&start='
    offset = 0

    start_urls = [url + str(offset)]



    def parse(self, response):
        for each in response.xpath('//*[@class="even"]'):
            item = TencentItem()
            item['positionname'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['positionlink'] = each.xpath('./td[1]/a/@href').extract()[0]
            item['positionType']  = each.xpath('./td[2]/text()').extract()[0]
            item['peopleNum'] = each.xpath('./td[3]/text()').extract()[0]
            item['workLocation'] = each.xpath('./td[4]/text()').extract()[0]
            item['publishTime'] = each.xpath('./td[5]/text()').extract()[0]
            
            yield item


        if self.offset < 1680:
            self.offset += 10
        else:
            print("结束")
            exit()         

        #每次处理完一页的数据之后，重新发送下一次的页面请求
        #调用回调函数 self.parse处理 respone
        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
