# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#下载图片的模板

#获取设置
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os

class DouyuPipeline(ImagesPipeline):

    #获取settings文件里设置的变量值
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    #获取图片链接，并发送请求
    def get_media_requests(self,item,info):
        image_url = item["imagelink"]
        yield scrapy.Request(image_url,meta={
            "item":item
        })
    
    #处理图片
    def item_completed(self,results,item,info):
        # ok判断是否下载成功
        image_paths = [x["path"] for ok, x in results if ok]
        
        if not image_paths:
            raise DropItem("Item contains no images")
        
        #os.rename(self.IMAGES_STORE + image_path[0], self.IMAGES_STORE + item["nickname"] + ",jpg")
        item["imagePath"] = image_paths[0]

        return item
    
    #需要重写一下ImagesPipeline中的file_path方法
    def file_path(self, request, response=None, info=None):
        item = request.meta["item"]
        return self.IMAGES_STORE + item["nickname"] + ".jpg"
