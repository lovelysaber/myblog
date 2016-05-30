#!/usr/bin/env python3
#-*-coding:utf-8-*-
from handlers.index import IndexHandler
from handlers.adminArticle import AddArticleHandler
from handlers.adminArticle import ListArticleHandler
from handlers.more import GetMoreHandler
from handlers.login import LoginHandler

url = [
    (r"/", IndexHandler),
	(r"/admin/add", AddArticleHandler),
	(r"/admin/list",ListArticleHandler),
	(r"/more/(\w+)", GetMoreHandler),
	(r"/admin/login", LoginHandler)
]
