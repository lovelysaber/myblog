#!/usr/bin/env python3
#-*-coding:utf-8-*-
import os
import base64
import uuid
import tornado.web
from url import url

settings = dict(
	template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "statics"),
	cookie_secret = base64.b64encode(uuid.uuid4().bytes),
	debug = True,
	autoescape=None
)

app = tornado.web.Application(handlers = url, **settings)
