#!/usr/bin/evn python
#coding:utf-8
import web

urls = (
    '/','Index',



)
class Index:
    def GET(self):
        return 'Index.'
    def POST(self):
        return 'Post.'

if __name__ == "__main__":
    web.application(urls,globals()).run()