#完成一个简单的tcp服务器
from socket import *

serSocket = socket(AF_INET,SOCK_STREAM)

#重复使用绑定的信息
