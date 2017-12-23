f = open('a.txt','w')
f.write("hello world1\n")
f.write("hello world2")

f.close()

'''
f = open('a.txt','r')
content = f.read(3)
print(content)
f.close()
'''

f = open('a.txt','r')
content = f.readlines()
#print(type(content))

i = 1
for temp in content:
    print("%d:%s"%(i,temp))
    i+=1

f.close()

