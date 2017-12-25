#ProxyHandler处理器（代理设置）
import urllib.request

#参数是一个字典，代理ip
#开放代理 {"http" : "118.193.107.207:80"}
#私密代理 {"http" : "账号:密码@118.193.107.207:80"}
httpproxy_handler = urllib.request.ProxyHandler({"http" : "118.193.107.207:80"})
nullproxy_handler = urllib.request.ProxyHandler({})

proxySwitch = True #定义一个代理开关

if property:
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    #不用代理
    opener = urllib.request.build_opener(nullproxy_handler)


# 1. 如果这么写，只有使用opener.open()方法发送请求才使用自定义的代理，而urlopen()则不使用自定义代理。
response = opener.open("http://www.baidu.com/")

# 2. 如果这么写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
#urllib.request.install_opener(opener)
#response = urllib.request.urlopen("http://www.baidu.com/")

#不清楚代理服务器返回的编码，这里解析为utf-8
print(response.read().decode('utf-8'))