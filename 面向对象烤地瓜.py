#面向对象烤地瓜
class SweetPotato:
    def __init__(self):
        self.cookedString = "生的"
        self.cookedLevel = 0
        self.condiments = []

    def __str__(self):
        return "地瓜 状态:%s(%d),添加的佐料有:%s"%(self.cookedString,self.cookedLevel,str(self.condiments))

    def cook(self,time):

        self.cookedLevel += time

        if self.cookedLevel >=0 and self.cookedLevel<3:
            self.cookedString = "生的"
        elif self.cookedLevel >=3 and self.cookedLevel<5:
            self.cookedString = "半生不熟"
        elif self.cookedLevel >=5 and self.cookedLevel<8:
            self.cookedString = "熟了"
        elif self.cookedLevel>8:
            self.cookedString = "烤糊了"
    
    def addCondiments(self,item):
        self.condiments.append(item)

#创建地瓜对象
di_gua = SweetPotato()

di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.cook(1)
di_gua.cook(1)
di_gua.addCondiments("大蒜")
print(di_gua)
di_gua.cook(2)
print(di_gua)
di_gua.addCondiments("孜然")
di_gua.cook(3)
print(di_gua)

