class Person(object):
    '''人类'''
    def __init__(self,name):
        #super().__init__() #调用父类object功能
        self.name = name
        self.gun = None
        self.hp = 100 #血量
    
    def anzhuang_zidan(self,dan_jia,zi_dan):
        '''把子弹装到弹夹中'''

        #弹夹.保存子弹(子弹)
        dan_jia.baocum_zidam(zi_dan)

    def.anzhuang_danjia(self,gun,dan_jia):
        '''把弹夹安装到枪中'''
        gun.baocun_danjia(dan_jia)

    def naqiang(self,gun):
        '''拿起一把枪'''
        self.gun = gun

    def kaiqiang(self,diren):
        '''让枪发射子弹打敌人'''
        self.gun.fire(diren)
    
    def diao_xue(self,sha_shang_li):
        self.hp -= sha_shang_li 


class Gun(object):
    '''枪类'''
    def __init__(self,name):
         #super().__init__() #调用父类object功能
         self.name = name #记录枪的类型
         self.danjia = None

    def baocun_danjia(self,dan_jia):
        self.danjia = dan_jia
    
    def fire(self,diren):
        '''让弹夹弹出一发子弹'''
        zidan_temp = self.danjia.tanchu_zidan()
        
        if zidan_temp:
            zidan_temp.dazhong(diren)
        else:
            print("没有子弹了")
        

class Danjia(object):
    '''弹夹'''
    def __init__(self,max_num):
        #super().__init__()
        self.max_num = max_num#记录弹夹最大容量
        self.zidan_list = [] #用户来记录所有的子弹

    def baocum_zidam(self,zi_dan):
        '''将子弹保存'''
        self.zidan_list.append(zi_dan)

    def tanchu_zidan(self):
        '''弹出最上面那颗子弹'''
        if self.zidan_list:
            return self.zidan_list.pop()
        else:
            return None

class Zidan(object):
    '''子弹类'''
    def __init__(self,sha_shang):
         self.sha_shang = sha_shang#子弹威力
    
    def dazhong(self,diren):
        '''打中敌人掉血'''
        diren.diao_xue(self.sha_shang)

def main():
    pass

    #1.创建老王对象
    laowang = Person("老王")
    #2.创建一个枪对象
    ak47 = Gun("AK47")
    #3.创建一个弹夹对象
    dan_jia = Danjia(20)
    #4.创建一些子弹
    for i in range(15):
        zi_dan = Zidan(10)
        #5.老王安装子弹
        laowang.anzhuang_zidan(dan_jia,zi_dan)

    #6.老王把弹夹安装到枪
    laowang.anzhuang_danjia(ak47,dan_jia)
    #7.创建敌人
    laowang.naqiang(ak47)
    #创建敌人
    gebi_laosong = Person("隔壁老宋")
    #9.老王开枪打敌人
    laowang.kaiqiang(gebi_laosong)


if __name__ == '__main__'
    main()