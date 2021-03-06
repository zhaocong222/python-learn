# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['http://www.itcast.cn/']
    # 爬虫其实的url
    start_urls = [
        "http://www.itcast.cn/channel/teacher.shtml",
    ]

    #解析方法
    def parse(self, response):
        # 通过scrapy自带的xpath匹配出所有老师的根节点列表集合
        teacher_list = response.xpath('//div[@class="li_txt"]')
        
        # 所有老师信息的列表集合
        #teacherItem = []
        # 遍历根节点集合
        # 遍历根节点集合
        for each in teacher_list:

            # Item对象用来保存数据的
            item = ItcastItem()
            # 不加extract() 结果为xpath匹配对象
            name = each.xpath('./h3/text()').extract()
            # title
            title = each.xpath('./h4/text()').extract()
            # info
            info = each.xpath('./p/text()').extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            #利用yield
            #将获取的数据交给管道 pipelines文件
            yield item

            #teacherItem.append(item)
            
        #return teacherItem

