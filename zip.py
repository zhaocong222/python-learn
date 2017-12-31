names = ["xiaomin","lily","tom"]
ages = [12,10,21]

#列表合并为元祖 [(xiaomin,12),(lily,10),(tom,21),]
data = zip(names,ages)

for name,age in data:
    print("名字是"+name+",年龄"+str(age))