#!/usr/bin/env python3
#-*-coding:utf-8-*-
import tornado.web
from models.db import Article

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		articles = Article.getAllArticle()
		self.render("index.html",title="index",articles=articles)
