#模拟登陆知乎

#导入webdriver api对象，可以调用浏览器和操作页面
from selenium import webdriver
#导入keys,可以操作键盘，标签，鼠标
from selenium.webdriver.common.keys import Keys
import time

#操作phantomjs浏览器对象
driver  = webdriver.PhantomJS()

driver.get("https://www.zhihu.com/signin")

#输入账号密码
driver.find_element_by_name("username").send_keys("账号")
driver.find_element_by_name("password").send_keys("密码")

# 模拟点击登录
driver.find_element_by_css_selector(".SignFlow .SignFlow-submitButton").click()

# 等待3秒（登陆后跳转）
time.sleep(3)

# 生成登陆后快照
driver.save_screenshot("zhihu.png")

#保存网页渲染后的源代码
with open("zhihu.html","w") as f:
    f.write(driver.page_source)

driver.quit()