# -*- coding: utf-8 -*-

'Http辅助函数'

__author__='litterzhang'

import time
import datetime
import urllib.parse

from sinaset import SinaUserUrl

def url_type(url):
	if SinaUserUrl.match(url) != None:
		return 0
	else:
		return -1

def url_decode(url):
	url = urllib.parse.unquote(url)
	return url

def url_join(url_base, url_to):
	url = urllib.parse.urljoin(url_base, url_to)
	return url_decode(url)

def url_format(url):
	if not url.startswith('http://'):
		url = 'http://' + url
	url = url.split('?')[0]
	url = url.split('#')[0]
	if url.endswith('/'):
		url = url[:-1]
	return url

def time_format(t_str):
	try:
		t_d = t_str.split()[0].strip()
		t_t = t_str.split()[1].strip()

		t = dict()

		if t_d=='今天':
			d = datetime.date.today()
			t['y'] = int(str(d).split('-')[0])
			t['m'] = int(str(d).split('-')[1])
			t['d'] = int(str(d).split('-')[2])
		elif t_d=='昨天':
			d = datetime.date.today() - datetime.timedelta(days=1)
			t['y'] = int(str(d).split('-')[0])
			t['m'] = int(str(d).split('-')[1])
			t['d'] = int(str(d).split('-')[2])
		else:
			if len(t_d.split('年'))>=2:
				t['y'] = int(t_d.split('年')[0])
				t_d = t_d.split('年')[1]
			else:
				t['y'] = int(str(datetime.date.today()).split('-')[0])
			
			t['m'] = int(t_d.split('月')[0])
			t_d = t_d.split('月')[1]
			t['d'] = int(t_d.split('日')[0])
			
		t['h'] = int(t_t.split(':')[0])
		t['M'] = int(t_t.split(':')[1])

		return '%04d-%02d-%02d %02d:%02d' % (t['y'], t['m'], t['d'], t['h'], t['M'])
	except:
		return ''