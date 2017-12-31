#获取斗鱼的js分页加载

#python的测试模块
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup as bs

#类需要继承unittest.TestCase
class douyuSelenium(unittest.TestCase):
    #初始化方法
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        
    #测试方法必须有test字样开头
    def testDouyu(self):
        self.driver.get("https://www.douyu.com/directory/all")
        while True:
            html = bs(self.driver.page_source,'lxml')
            # 返回当前页面所有房间标题列表 和 观众人数列表
            titles = html.find_all('h3', {'class': 'ellipsis'})
            nums = html.find_all('span', {'class': 'dy-num fr'})

            #zip(titles,nums) 将titles和nums合并为一个元祖[(1,2),(3,4)]
            for title,num in zip(titles,nums):
                print("观众人数"+num.get_text().strip()+"\t房间名"+title.get_text().strip())
            
            # page_source.find()未找到内容则返回-1
            if self.driver.page_source.find('shark-pager-disable-next') != -1:
                break

            # 模拟下一页点击
            self.driver.find_element_by_class_name('shark-pager-next').click()

    #退出时的清理方法
    def tearDown(self):
        print("加载完成")
        self.driver.quit()

if __name__ == "__main__":
    #启动测试模块
    unittest.main()