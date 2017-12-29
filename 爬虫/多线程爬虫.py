#使用线程库
import threading
#队列
from queue import Queue
#解析库
from lxml import etree
import json
import jsonpath
import time
import requests

exitFlag_Parser = False
lock = threading.Lock()

class ThreadCrawl(threading.Thread):
    def __init__(self,threadName,pageQueue,dataQueue):
        #调用父类初始化 第一个参数自己类的名字，第二个参数self
        super(ThreadCrawl,self).__init__()
        #线程名
        self.threadName = threadName
        #页码队列
        self.pageQueue = pageQueue
        #数据队列
        self.dataQueue = dataQueue
        #头信息
        self.headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                    'Accept-Language': 'zh-CN,zh;q=0.8'
        }
    
    #线程执行
    def run(self):
        #队列为空循环终止
        print("启动"+self.threadName)
        while not self.pageQueue.empty():
            try:
                #取出1个页面
                #可选参数block,默认值是true
                #1.如果队列为空,block为true，就会进入阻塞状态，直到队列有新数据
                #2.如果队列为空，block为false,就会弹出1个Queue.empty()异常
                page = self.pageQueue.get(False)
                url = "https://www.qiushibaike.com/8hr/page/" + str(page) +"/"
                content = requests.get(url,headers = self.headers)
                self.dataQueue.put(content.text)
            except:
                pass
        print("结束"+self.threadName)

#解析线程
class ThreadParse(threading.Thread):
    def __init__(self,threadName,dataQueue,filename):
        super(ThreadParse,self).__init__()
         #线程名
        self.threadName = threadName
        #数据解析队列
        self.dataQueue = dataQueue
        #文件名
        self.f = filename
    
    def run(self):
        global exitFlag_Parser
        while not exitFlag_Parser:
            try:
                html = self.dataQueue.get(False)
                self.parse(html)
            except:
                pass

    #解析类
    def parse(self,html):
        html = etree.HTML(html)
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

            result = {
                    'imgUrl': imgUrl,
                    'username': username,
                    'content': content,
                    'vote': vote,
                    'comments': comments,
            }

            result = json.dumps(result, ensure_ascii=False)
            global lock
            #获取锁
            lock.acquire()
            self.f.write(result+"\n")
            #释放锁
            lock.release()

        
def main():
    #存放页数的队列,10表示10个页面
    pageQueue = Queue(10)
    # 放入1-10个数字，先进先出
    for i in range(1,11):
        pageQueue.put(i)
    
    #采集数据结果队列.参数为空表示无限制
    dataQueue = Queue()

    filename = open("duanzi.json","a")

    #采集线程的名字
    crawlList = ['采集线程1号','采集线程2号','采集线程3号']

    #存储三个采集线程
    threadcrawl = []
    #创建线程
    for threadName in crawlList:
        #创建线程对象
        thread = ThreadCrawl(threadName,pageQueue,dataQueue)
        thread.start()
        threadcrawl.append(thread)

    #解析线程
    parseList = ['解析线程1号','解析线程2号','解析线程3号']
    threadparse = []
    
    for threadName in parseList:
        thread = ThreadParse(threadName,dataQueue,filename)
        thread.start()
        threadparse.append(thread)
 
    #while not pageQueue.empty():
    #    pass

    #子线程加入阻塞 （主要作用的 阻塞掉主线程）
    for thread in threadcrawl:
        thread.join()
        print('x')

    global exitFlag_Parser
    exitFlag_Parser = True
    
    '''
    for thread in threadparse:
        thread.join()
        print('x')
    '''


if __name__ == "__main__":
    main()