#!/usr/bin/env python3
#-*-coding:utf-8-*-
from sqlalchemy import create_engine
from sqlalchemy import MetaData,Table
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from markdown2 import markdown

DB_CONNECT_STRING = "mysql+pymysql://root:123456@localhost:3306/blog?charset=utf8"
engine = create_engine(DB_CONNECT_STRING, echo = True)

Base = declarative_base()
DBSession = sessionmaker(bind = engine)
session = DBSession()

class User(Base):
	__tablename__ = "user"
	id = Column(Integer, primary_key = True)
	name = Column(String(50))
	password = Column(String(50))
	
	@classmethod
	def getUser(self, username):
		return session.query(User).filter(User.name == username).first()

class Article(Base):
	__tablename__ = "article"
	id = Column(Integer, primary_key = True)
	title =	Column(String(20))
	content = Column(String(200))
	create_time = Column(DateTime, default = datetime.now)
	url = Column(String(200))

	@classmethod
	def addArticle(self,title,content):
		article = Article()
		article.title = title
		temp = content
		temp = markdown(temp, extras=["smarty-pants","fenced-code-blocks"])
		article.content = temp
		article.url = title
		session.add(article)
		session.commit()
	
	@classmethod
	def delArticle(self,id):
		article = session.query(Article).filter(Article.id == id).one()
		session.delete(article)
		session.commit()

	@classmethod
	def getAllArticle(self):
		articles = session.query(Article).all()
		return articles

	@classmethod
	def getMore(self,url):
		article = session.query(Article).filter(Article.url == url).one()
		return article

