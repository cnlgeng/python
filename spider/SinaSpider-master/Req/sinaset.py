# -*- coding: utf-8 -*-

'Http请求参数'

__author__='litterzhang'

import re

UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36'

Referer = 'http://weibo.cn/'

SinaUserUrl = re.compile(r'^(http://)?(weibo.cn/)([^/\?#]+|n/[^/\?#]+|u/\d+)(\?[^/\?]+)?(#[^/\?#]+)?/?$')

BlockTag = ['style', 'link', 'meta', 'img']

if __name__=='__main__':
	m = SinaUserUrl.match('http://weibo.cn/p?tf=7_011')
	print(m)
