#练习来源于Magnus Lie Hetland的python教科书
#生成字典
def create(data):
    data['first']={}
    data['middle']={}
    data['last']={}
storage={}
create(storage)
#查询全名
def lookup(data,label,name):
    return data[label].get(name)
#姓名的存储
def store(data,*fullnames): #使用*保证能同时接受多个变量，放在元组或者字典中
    for fullname in fullnames:
        names=fullname.split()#使用split方法使每个字符串变成列表
        if len(names)==2: names.insert(1,"")#如果没有middle name则在中间插入空字符串
        labels='first','middle','last'
        for label,name in zip(labels,names):#建立一一对应关系，方便后面处理
            people=lookup(data,label,name)
            if not people:
                data[label][name]=[fullname]
            else:
                people.append(fullname)


Myfamily={}
create(Myfamily)
store(Myfamily,'Wang Li Yao','Ni Xia','Wang Mu Xue')
print(Myfamily.items())
