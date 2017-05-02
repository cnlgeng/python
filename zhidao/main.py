#!/usr/bin/env python
#coding:utf-8
import web
urls=(
    '/','Index',
    '/user','User',
    '/reg','Reg',
    '/post','Post',
    '/login','Login',
    '/logout','Logout',
    '/put','Put',

)
web.config.debug = False
app = web.application(urls,globals())
session = web.session.Session(app,web.session.DiskStore('sessions'))
render = web.template.render('templates')
class Login:
    def GET(self):
        if not session.get('login', False):
            return render.login(render.head())
        return render.head('亲，您已经登录了')

    def POST(self):
        i = web.input()
        username,passwd = i.get('username'),i.get('passwd')
        #print username,passwd
        if username == 'admin' and passwd == 'admin':
            session.login = True
            return render.head2(',登录成功')
        return render.head('登录失败')
        #raise web.seeother('/login')

class Logout:
    def GET(self):
        if session.get('login'):
            session.login = False
            return render.head(' 注销成功 ')
        return render.head('亲，您还未登录呢')
        #raise web.seeother('/')

class Index:
    def GET(self):
        if session.get('login'):
            return render.head2("," )
        return render.head(",")

#个人中心
class User:
    def GET(self):
        if session.get('login'):
            return render.index2(render.head2('1234'))
        return render.index2(render.head('1234'))


#注册
class Reg:
    def GET(self):
        if session.get('login'):
            return render.reg(render.head2())
        return render.reg(render.head())

    def POST(self):
        i = web.input()
        #i = web.data()
        return render.head('%s,%s,%s,%s' % (i.get('username'),i.get('passwd'),i.get('tel'),i.get('passwd1')))

class Post:
    def GET(self):
        #print session.get('login')
        if not session.get('login',False):
            return render.head('亲，要登录后才能发表哦!')
        return render.put(render.head2())

class Put:
    def POST(self):
        #写入数据库
        i = web.input()
        return render.head2(i)

if __name__ == '__main__':
    app.run()
