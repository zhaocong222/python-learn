# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

#教程https://www.jianshu.com/p/461d74641e80

import scrapy

#定义结构化数据字段,用来保存爬取到的数据
#这里可以理解成类似于ORM的映射关系
class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()