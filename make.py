#!/usr/bin/env python3.5
import sys
import markdown2
from models.db import Article

filename = sys.argv[1]
f = open(filename,"r")
title = f.name.split('.')[0]
content = f.read()
content = markdown2.markdown(temp, extras=["smarty-pants","fenced-code-blocks"])
Article.addArticle(title,content)
