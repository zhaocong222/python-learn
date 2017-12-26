import urllib.request,urllib.error
import io
import sys
import re

#兼容win系统
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

class Spider(object):

    def __init__(self,url,page):
        self.url = url
        self.page = page
        self.enable = True

    """
    内涵段子爬虫类
    """
    def loadPage(self,page):
        """
            @brief 定义一个url请求网页的方法
            @param page 需要请求的第几页
            @returns 返回的页面html
        """
        url = self.url.format(page=page)
        #user-agent头
        user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1; Trident/5.0'
        headers = {'User-Agent': user_agent}
        req = urllib.request.Request(url,headers=headers)
        respone = urllib.request.urlopen(req)
        html = respone.read().decode('gb2312')

        #找到所有的段子内容<div class = "f18 mb20"></div>
        #re.S 如果没有re.S 则是只匹配一行有没有符合规则的字符串，如果没有则下一行重新匹配
        # 如果加上re.S 则是将所有的字符串将一个整体进行匹配
        pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>',re.S)
        item_list = pattern.findall(html)
        return item_list

    #打印数据
    def printOnePage(self,item_list,page):
        """
        @brief 处理得到的段子列表
        @param item_list 得到的段子列表
        @param page 处理第几页
        """
        print("******* 第 %d 页 爬取完毕...*******" %page)
        for item in item_list:
            print("=====================")
            item = item.replace("<p>","").replace("</p>","").replace("<br />", "")
            print(item)
            self.writetoFile(item)

    #保存数据
    def writetoFile(self,text):
        '''
        @brief 将数据追加写进文件中
        @param text 文件内容
        @指定utf-8编码写入
        '''
        myFile = open("./duanzi.txt", 'a',encoding='utf-8') #追加形式打开文件
        myFile.write(text)
        myFile.write("---------------------------------------------")
        myFile.close()
    
    def doWork(self):
        '''
        让爬虫工作
        '''
        while self.enable:
            try:
                item_list = self.loadPage(self.page)
            except urllib.error.URLError as e:
                print(e.reason)
                continue

            #得到item_list 处理
            self.printOnePage(item_list,self.page)
            self.page += 1
            print("按回车继续...")
            print("输入 quit 退出")
            command = input()
            if command == 'quit':
                self.enable = False
                break

if __name__ == '__main__':
    url = 'http://www.neihan8.com/article/list_5_{page}.html'
    spider = Spider(url,1)
    spider.doWork()