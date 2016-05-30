#!/usr/bin/env python3
#-*-coding:utf-8-*-

import tornado.web
from models.db import Article

class GetMoreHandler(tornado.web.RequestHandler):
	#def get(self):
		#articles = Article.getAllArticle()
		#print type(articles)
		#for i in articles:
		#	print type(i)
		#	self.render("more.html",a=art)
		#	self.render("more.html",a=i)

	def get(self,url):
		print("URL:%s"%url)
		article = Article.getMore(url)
		self.render("more.html",article=article)
