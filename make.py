#!/usr/bin/env python3.5
import sys
import markdown2
from models.db import Article

filename = sys.argv[1]
f = open(filename,"r")
title = f.name.split('.')[0]
print(title)
temp = f.read()
#print(temp)
print("转换之前:",temp)
temp = markdown2.markdown(temp, extras=["smarty-pants","fenced-code-blocks"])
print("转换之后:",temp)
#temp = temp.replace("<blockquote>",">")
#temp = temp.replace("<code>",'<code class="discode">')
#print(title)
#temp = temp.replace("<code>","<code><pre>")
#temp = temp.replace("</code>","</pre></code>")
#print(temp)
Article.addArticle(title,temp)
