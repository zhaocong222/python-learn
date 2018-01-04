# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start = 0
    
    url = 'https://movie.douban.com/top250?start={offset}&filter='

    start_urls = [url.format(offset=start)]

    def parse(self, response):
        
        print(response.url+"\n")

        item = DoubanItem()
        #获取电影介绍的 ele
        movies = response.xpath("//div[@class='info']")

        for each in movies:
            
            # 标题
            item['title'] = each.xpath(".//span[@class='title'][1]/text()").extract()[0]
            # 信息
            item['content'] = each.xpath(".//div[@class='bd']/p/text()").extract()[0]
            # 评分
            item['score'] = each.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract()[0]
            # 简介
            info = each.xpath(".//p[@class='quote']/span/text()").extract()
            if len(info) != 0:
                item['info'] = info[0]

            #返回管道
            yield item
        
        if self.start <= 225:
            self.start += 25
            yield scrapy.Request(self.url.format(offset=self.start),callback=self.parse)