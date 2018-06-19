# -*- coding: UTF-8 -*-

def def01(name,age):
    return (name,age)

def def02(name,age):
    print name
    print age
    return

# print def02(1,2)

def def04(arg1, **vartuple ):
   for (key,value) in vartuple.items():
      print (key,value)
   return

def04("123",a=1,b="b",c=[1,2,3])