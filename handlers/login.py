#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#import tornado.web
from models.db import User
from handlers.base import BaseHandler
#BaseHandler = base.BaseHandler

class LoginHandler(BaseHandler):
	def get(self):
		self.render("login.html", title="login")
	
	def post(self):
		username = self.get_argument("username")
		user = User.getUser(username)
		if user:
			password = self.get_argument("password")
			if user.password == password:
				self.set_secure_cookie("name",username)
				self.finish("0")	#匹配成功
				#self.redirect("/")
				#return 
			else:
				self.finish("-1")	#密码错误
		else:
			self.finish("1")	#用户名错误
