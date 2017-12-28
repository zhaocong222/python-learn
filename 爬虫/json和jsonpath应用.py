import requests
import json
#sudo pip3 install jsonpath
import jsonpath

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

try:
    respone = requests.get(url,headers = headers)
    res = respone.text
    #读取文件中json形式的字符串元素 转化成python类型
    unicodestr = json.loads(res)
    #提取城市信息
    #list
    city_list = jsonpath.jsonpath(unicodestr,"$..name") 
    
    #数据通过特殊的形式转换为所有程序语言都认识的字符串
    # dumps()默认中文为ascii编码格式，ensure_ascii默认为Ture
    # 禁用ascii编码格式，返回的Unicode字符串，方便使用
    array = json.dumps(city_list,ensure_ascii=False)
    #print(type(array)) str
    with open("lagoucity.json","w") as f:
        f.write(array)

except Exception as e:
    print(e)