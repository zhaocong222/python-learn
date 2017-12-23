class Home:
    def __init__(self,area,info,address):
        self.area = area
        self.info = info
        self.addr = address
        self.item = []
        self.left_area = area
    
    def add_item(self,item):
        self.item.append(item)
        self.left_area == item.area 

    def __str__(self):
        return "房子的总面积是:%d,可用面积是:%d,户型是:%s,地址是:%s"%(self.area,self.left_area,self.info,self.addr)

class Bed:
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area = new_area
  
    def __str__(self):
        return "%s占用的面积是:%d"%(self.name,self.area)

fangzi = Home(129,"三室一厅","北京市 朝阳区 长安街 666号")
print(fangzi)

bed1 = Bed("席梦思",4)
print(bed1)

fangzi.add_item(bed1)