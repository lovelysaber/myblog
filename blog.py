#!/usr/bin/env python3
#-*-coding:utf-8-*-
import tornado.ioloop
import tornado.options
import tornado.httpserver
from tornado.options import define, options
from app import app

define("port", default = 8000, help = "run on the given port", type = int)

def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)

	print("This Server Running At http://127.0.0.1:%s" % options.port)
	print("Quit This SerVer With Ctrl+C")
	
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()
