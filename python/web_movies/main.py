#!/usr/bin/env python
#coding:utf-8

import web
import os,sys

urls=(
    '/','index',
)

render = web.template.render('templates')  #render模板引用
db = web.database(dbn='mysql',host='120.25.97.247',port=3306,user='username',pw='password',db='ruijie',charset='utf8')

class index:
    def GET(self):        #函数名 ,为web的请求方式: get
        #return open('index.html','r').read()
        #return open('index.html', 'r')
        #return render.index()
        data = db.query("select * from auth_data limit 1;")
        return data[0]['mac']
        #return render.movie('你好')

    def POST(self):       #函数名 ,为web的请求方式: post
        pass

if __name__ == "__main__":
    web.application(urls,globals()).run()
