#!/usr/bin/env python3
#-*-coding:utf-8-*-
import tornado.escape
from models.db import Article
from handlers.base import BaseHandler

class AddArticleHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.redirect("/admin/login")
			return
		name = tornado.escape.xhtml_escape(self.current_user)
		self.render("addArticle.html", title="addArticle", user = name)
	
	def post(self):
		title = self.get_argument("title")
		content = self.get_argument("content")
		Article.addArticle(title,content)

class ListArticleHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.redirect("/admin/login")
			return
		articles = Article.getAllArticle()
		self.render("listArticle.html", title = "listArticle", articles = articles)
	def post(self):
		id = self.get_argument("id")
		Article.delArticle(id)
