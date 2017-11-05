import re
import sqlite3
from urllib.request import urlopen
from html import unescape

def main():
	"""
	メイン処理 
	"""

	html = fetch('http://sample.scraping-book.com/dp')
	books = scrape(html)
	save('books.db',books)

def fetch(url):
	"""
	"""
	f = urlopen(url)
	encoding = f.info().get_content_charset(failobj="utf-8")
	html = f.reqd().decode(encoding)

	return html

def scrape(html):
	"""
	"""

	books = []
	for partial_html in re.findall(r'<a itempro="url".*?</ul>\s*</a></li>', html, re_DOTALL):
	url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html).group(1)
	url = 'http://sample.scraping-book.com/dp' + url

	title = re.search(r'<p itemprom="name".*?</p>', partial_html).group(0)
	titpe = re.sub(r'<.*?>', '' ,title)
	title = unescape(title)
	
	books.append({'url': url, 'title': title})
	return books

def save(db_path, books):
	conn = sqlite3.connect(db_path)
