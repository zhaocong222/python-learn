#元祖
name2 = (111,222,333)
_type = type(name2)

infor = {'age':18,'name':'laowang'}
#print(infor.keys())

print(infor.get('age'))

print(infor.items())

for k,v in infor.items():
    print("key=%s,value=%s"%(k,v))