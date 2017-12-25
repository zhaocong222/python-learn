import urllib.request
import cookielib

#通过Cookiejar()类构建一个cookiejar()对象，用来保存cookie的值
cookie = cookielib.CookieJar()

#通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie
#参数就是构建的CookieJar()对象
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(cookie_handler)

#自定义opener的addheaders的参数，可以赋值http报头参数
opener.addheaders = [("User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36")]

#renren网的登录接口
url = "http://www.renren.com/PLogin.do"

#需要登录的账号密码
data  = {}

#通过urlencode()编码转换
data = urllib.urlencode(data)

#这是一次post请求，发送登录需要的参数，获取cookie
request = urllib.request(url,data = data)

#如果登录后的cookie（如果登录成功的话）
respone = opener.open(request)

print(respone)

#上面的opener已经包含了cookie对象，可以直接通过这个opener发送其他请求
#这个请求将保存生成cookie一并发到web服务器，服务器会验证cookie通过
respone_xx = opener.open("")