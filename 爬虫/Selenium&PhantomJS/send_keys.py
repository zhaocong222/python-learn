from selenium import webdriver

driver = webdriver.PhantomJS()

#加载http://www.baidu.com/
driver.get("http://www.baidu.com/")

#给浏览器的输入框 输入美女
driver.find_element_by_id("kw").send_keys(u"美女")

#截图
driver.save_screenshot("baidu1.png")