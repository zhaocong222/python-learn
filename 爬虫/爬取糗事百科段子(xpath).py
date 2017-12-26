'''
要求：
使用requests获取页面信息，用XPath / re 做数据提取
获取每个帖子里的用户头像链接、用户姓名、段子内容、点赞次数和评论次数
'''

import urllib.request,urllib.error
import io
import sys
import re
import requests
from lxml import etree

#兼容win系统
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

page = 1
url = 'http://www.qiushibaike.com/8hr/page/' + str(page)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

try:
    respone = requests.get(url,headers = headers)
    #print(respone)
    resHtml = respone.text
    
    html = etree.HTML(resHtml)
    #查找根节点下 id属性包含qiushi_tag字符的div节点 -> @id属性id ， contains包含
    result = html.xpath('//div[contains(@id,"qiushi_tag")]')

    for site in result:

        #当前节点下的div下的a下的img节点的属性src
        imgUrl  = site.xpath('./div/a/img/@src')[0]
        username = site.xpath('.//h2')[0].text
        #获取标签里面的所有text   ab<br/>cd<br/>   .xpath('string(.)').strip() -> abcd
        #如果单纯使用 text 只能获得ab
        content = site.xpath('.//div[@class="content"]/span')[0].xpath('string(.)').strip()

        # 投票次数
        vote = site.xpath('.//i')[0].text
        # 评论数
        comments = site.xpath('.//i')[1].text

except Exception as e:
    print(e)






