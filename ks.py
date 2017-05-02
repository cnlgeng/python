#!/usr/bin/evn python
#coding:utf-8
print "="*20+" 第一题 "+"="*20
def reversed_sequence(var):
    #obj = reversed_sequence(var)
    if type(var) == str:
        obj = reversed(var)
        print ''.join(obj)
    elif isinstance(var,tuple):  # <==> type(var) == tuple
        obj = reversed(var)
        print tuple(list(obj))
    elif isinstance(var,list): # <==> type(var) == list
        obj = reversed(var)
        print list(obj)
    else:
        print "Type Error."

reversed_sequence('abc')  # str
reversed_sequence((1,2,3,4)) #tuple
reversed_sequence([1,2,3,'a','b','c']) #list
reversed_sequence({'a':1,'b':2,'c':3}) #

print "="*20+" 第二题 "+"="*20
def converted_case(var):
    def fun1(var):
        if var.islower():
            return var.upper()
        elif var.isupper():
            return var.lower()
        else:
            return var
    if type(var)==str:
        ls1 = []
        for i in xrange(len(var)):
            ls1.append(fun1(var[i]))
        return ''.join(ls1)
    if type(var) == tuple or type(var) == list:
        ls2=[]
        for x in var:
            ls2.append(converted_case(x))      #converted_case() 递归,  处理元组或列表中嵌套情况
        return tuple(ls2)

print converted_case('AbcDs123')
print converted_case(('a','b','C','d','a','B'))
print converted_case(('ABc','b','C','China','c','B','c','D','-','g','+'))                  #扩展1，单个元素 由多个字符组成的情况
print converted_case(['a','BcD','c','E',('Abc','c','BBc',['a','ArI','B','b'],'D','++')])  #扩展2, 元组(或列表)中嵌套(多层嵌套)元组(或列表)的情况






print "="*20+" 第三题 "+"="*20
def which_order(var):
    o2l = list(var)
    o2s = sorted(var)
    if o2s == o2l:
        print "Up"
    elif o2s == o2l[::-1]:
        print "Down"
    else:
        #return 0
        print None

which_order('abc')
which_order([3,2,1])
which_order('132')
which_order('China')





print "="*20+" 第四题 "+"="*20

def charcount(var):
    Count = {'whitespase': 0, 'other': 0, 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
             'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
             'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for i in xrange(len(var)):
        #if ord(var[i]) == 32:
        if var[i].isspace():
            Count['whitespase'] += 1
        elif var[i].isalpha():
            Count[var[i].lower()] +=1
        else:
            Count['other'] += 1
    print Count

charcount('123AA   a ^_^')
charcount('a b c d >_< ')



print "="*20+" 第五题 "+"="*20

def frange(start=None,stop=None,step=None):
    def fun5(v1,v2,v3=1):
        ls5=[]
        while v1<v2:
            ls5.append(float(v1))
            v1 += v3
        return ls5
    if step is None and start is not None:
        #一个参数
        if stop is None:
            stop,start = start, 0
            print fun5(start,stop)
        #两个参数
        else:
            print fun5(start,stop)
    else:
        print fun5(start,stop,step)

frange(5)
frange(1,5)
frange(1,10,2)

print "=-----"

def frange2(*var):
    def fun6(v1,v2,v3=1):
        ls5 = []
        while v1 < v2:
            ls5.append(float(v1))
            v1 += v3
        return ls5
    if len(var)==1:
        v2,v1=var[0],0
        print fun6(v1,v2)
    if len(var) == 2:
        print fun6(var[0],var[1])
    if len(var) == 3:
        print fun6(var[0],var[1],var[2])


frange2(5)
frange2(1,10)
frange2(1,10,2)

