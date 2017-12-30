from selenium import webdriver

driver = webdriver.PhantomJS()

#加载http://www.baidu.com/
driver.get("http://www.baidu.com/")

#截取 加载页面 保存为 baidu.png
driver.save_screenshot("baidu.png")