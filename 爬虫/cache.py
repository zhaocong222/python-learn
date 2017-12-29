from redis import StrictRedis, ConnectionPool

pool = ConnectionPool(host='localhost', port=6379, decode_responses=True)
redis = StrictRedis(connection_pool=pool)

class CacheTool:

    @staticmethod
    def set(name,value):
        return redis.set(name,value)

    def get(name):
        return redis.get(name)

    @staticmethod
    def sadd(value):
        return redis.sadd('url',value)

    @staticmethod
    def smembers():
        return redis.smembers('url')

'''
print(CacheTool.sadd("www.baidu.com"))
print(CacheTool.sadd("www.baidu.com"))
print(CacheTool.sadd("www.baidu.com"))
print(CacheTool.sadd("www.baidu.com"))
print(CacheTool.sadd("www.qq.com"))
print(CacheTool.smembers())
'''