# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentPipeline(object):
    
   #可选初始化方法
    def __init__(self):
        #创建1个文件
        self.filename = open("position.json","w")

    #必须有的方法 处理数据, item就是传过来的数据
    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item),ensure_ascii=False)
        self.filename.write(jsontext)

    #可选方法，最后执行（相当于php析构方法）
    def close_spider(self,spider):
        #关闭文件
        self.filename.close()