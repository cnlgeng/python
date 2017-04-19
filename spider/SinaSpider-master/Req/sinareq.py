# -*- coding: utf-8 -*-

'封装Http请求'

__author__='litterzhang'

import requests
from requests.auth import AuthBase

from bs4 import BeautifulSoup

from sinaset import *
from sinautil import *

class SAuth(AuthBase):
	def __init__(self, ua=UserAgent, rf=Referer):
		self.ua = ua
		self.rf = rf
		pass

	def __call__(self, r):
		r.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
		r.headers['Accept-Encoding'] = 'gzip, deflate, sdch'
		r.headers['Accept-Language'] = 'zh-CN,zh;q=0.8'
		r.headers['Cache-Control'] = 'max-age=0'
		r.headers['Connection'] = 'keep-alive'
		r.headers['Referer'] = self.ua
		r.headers['Upgrade-Insecure-Requests'] = '1'
		r.headers['User-Agent'] = self.rf
		return r

class SReq:
	def __init__(self, ua=UserAgent, ss=None):
		self._last = None
		self._auth = SAuth(ua=ua)

		if not ss:
			self._session = requests.session()
		else:
			self._session = ss

	def get(self, url, data={}):
		if self._last:
			self._auth.rf = self._last
		r = self._session.get(url, params=data, auth=self._auth)
		self._last = url
		return SRep(r)

	def post(self, url, data={}):
		if self._last:
			self._auth.rf = self._last
		r = self._session.post(url, data=data, auth=self._auth)
		self._last = url
		return SRep(r)

class SRep:
	def __init__(self, r):
		if not r:
			raise 'Response Can Not Be None !'
		self._rep = r

	@property
	def content_type(self):
		ct = self._rep.headers.get('Content-Type', None)
		return ct

	@property
	def encoding(self):
		enc = 'utf-8'

		if self._rep.encoding:
			enc = self._rep.encoding
		return enc

	@property
	def doc_type(self):
		dt = 'text/html'

		if self.content_type:
			try: dt = self.content_type.split(';')[0].strip()
			except: pass
		return dt

	@property
	def text(self):
		self._rep.encoding = self.encoding
		return self._rep.text

	@property
	def status_code(self):
		sc = self._rep.status_code
		return sc

	@property
	def headers(self):
		return self._rep.headers

	@property
	def reason(self):
		return self._rep.reason

	@property
	def cookies(self):
		return self._rep.cookies

	@property
	def elapsed(self):
		return self._rep.elapsed

	@property
	def request(self):
		return self._rep.request

	@property
	def history(self):
		return self._rep.history

	@property
	def url(self):
		return self._rep.url

class SDoc:
	def __init__(self, doc, url):
		self._soup =  BeautifulSoup(doc, 'html.parser')
		self._url = url

		for tag in BlockTag:
			while getattr(self._soup, tag)!=None:
				getattr(self._soup, tag).decompose()

class SUDoc(SDoc):
	def __init__(self, doc, url):
		super(SUDoc, self).__init__(doc, url)

		# 尝试提取用户信息
		self.info = False
		try:
			udiv = self._soup.find('div', class_='u')
			uidiv = udiv.find('div', class_='ut')
			utdiv = udiv.find('div', class_='tip2')

			self.uid = udiv.a.get('href').split('/')[1]
			self.nickname = uidiv.select('span.ctt')[0].text.split()[0]
			self.locandsex = uidiv.select('span.ctt')[0].text.split()[1]
			self.gmsg = uidiv.select('span.ctt')[1].text.split()[0]
			self.sign = uidiv.select('span.ctt')[2].text.split()[0]

			self.blognum = int(utdiv.text.split()[0].split('[')[1].split(']')[0])
			self.follownum = int(utdiv.text.split()[1].split('[')[1].split(']')[0])
			self.fansnum = int(utdiv.text.split()[2].split('[')[1].split(']')[0])

			self.info = True
		except:
			pass

	@property
	def uinfo(self):
		uinfo = dict()

		if self.info:
			uinfo['id'] = self.uid
			uinfo['nickname'] = self.nickname
			uinfo['locandsex'] = self.locandsex
			uinfo['gmsg'] = self.gmsg
			uinfo['sign'] = self.sign
			uinfo['blognum'] = self.blognum
			uinfo['follownum'] = self.follownum
			uinfo['fansnum'] = self.fansnum
		return uinfo

	@property
	def ublog(self):
		ublog = list()
		# 提取用户微博信息
		for t in self._soup.find_all('div', class_='c'):
			if t.get('id'):
				blog_c = t.find('span', class_='ctt').text
				blog_t = t.find('span', class_='ct').text.split(' ')

				ublog.append({'text': blog_c, 'time': time_format(blog_t[0]), 'client': blog_t[1][2:]})
		return ublog

	def links(self, stype=-1):
		links = list()

		tags = self._soup.find_all('a')
		for t in tags:
			if t.get('href'):
				url_to = t.get('href')
				url = url_join(self._url, url_to)

				if stype==-1 or url_type(url)==stype:
					if (url_format(url) not in links) and (url_format(url)!=self._url):
						links.append(url_format(url))
		return links

if __name__=='__main__':
	req = SReq()
	rep = req.get('http://weibo.cn/n/eStar王者荣耀')

	print(rep.url)
	print(rep.text)

	soup = SUDoc(rep.text, rep.url)
	print(soup.links(stype=0))


	# with open('html.txt', 'r', encoding='utf-8') as fr:
	# 	html = ''
	# 	for line in fr:
	# 		html += line

	# 	soup = SUDoc(html, 'http://weibo.cn/iamamycheung')

	# 	print(soup.links(stype=0))
	# 	# 	fw.write(str(soup._soup))		

