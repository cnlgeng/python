#!/usr/bin/env python
#coding:utf8

def isSushu(var):
	if var==1:
		return 0
	ls1=[]
	for a in xrange(2,var):
		for b in xrange(2,(var/a+1)+1):
			if a*b == var:
				#print a,b
				ls1.append((a,b))
	if len(ls1) == 0:
		return var
	#else:
	#	print var,ls1  #列出所有的因数

for i in xrange(100):
	if isSushu(i):
		print i,
