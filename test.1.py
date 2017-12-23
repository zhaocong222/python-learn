print("="*50)
print("   名片管理系统 v0.01")
print("1. 添加一个新的名片")
print("2. 删除")
print("3. 修改")
print("4. 查询")
print("5. 退出")
print("="*50)

card = []

while True:
    num = int(input("请输入操作序号:"))

    if num == 1:
        new_name = input("请输入新的名字:")
        new_qq = input("请输入新的qq:")

        #定义空字典
        new_infor = {}
        new_infor['name'] = new_name
        new_infor['qq'] = new_qq
        
        card.append(new_infor)
        print(card)
    elif num==2:
        name = input("请输入要删除的名字：")
        for item in card:
            if item["name"] == name:
               card.remove(item)  #删除数组里某字典
    elif num==3:
        pass
    elif num==4:
        name = input("请输入查找的名字:")
        flag = 0
        for item in card:
            if item["name"] == name:
                print("qq号为:%s"%(item["qq"]))
                flag = 1
                break
        
        if flag == 0:
            print("没有找到名字")        

    elif num==5:
        print(card)
    else :
        print("输入有误，请重新输入")


