# -*- coding: utf-8 -*-
import io
import urllib.request,urllib.parse,urllib.error
import http.cookiejar
import sys

#兼容win系统
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#通过Cookiejar()类构建一个cookiejar()对象，用来保存cookie的值
cookie_filename = './cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(cookie_filename)

#也可以不指定cookie参数，默认
#cookie = http.cookiejar.MozillaCookieJar()

#通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie
#参数就是构建的CookieJar()对象
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(cookie_handler)

#自定义opener的addheaders的参数，可以赋值http报头参数
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

#renren网的登录接口
url = "http://www.renren.com/PLogin.do"

#需要登录的账号密码
data  = {"email":"账号","password":"密码"}

#通过urlencode()编码转换
data = urllib.parse.urlencode(data).encode()


#这是一次post请求，发送登录需要的参数，获取cookie
request = urllib.request.Request(url,data,headers)

try:
    #如果登录后的cookie（如果登录成功的话）
    respone = opener.open(request)
    page = respone.read().decode()
    #print(page)

except urllib.error.URLError as e:
    print(e.code, ':', e.reason)

cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中

#上面的opener已经包含了cookie对象，可以直接通过这个opener发送其他请求
#这个请求将保存生成cookie一并发到web服务器，服务器会验证cookie通过
respone_detail = opener.open("http://www.renren.com/962500579/profile?v=info_timeline")
print(respone_detail.read().decode())

