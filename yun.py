
import sys

class wangjing:
	def __init__(self,name):
		self.name = name
		print "init的name"+self.name
	def wocao(self):
		print 'wocao'
		
	def wokao():
		print 'wokao'
		
wang = wangjing("wangjing")

callable(wang.wocao())



# -*- coding:utf-8 -*-
#import re
import os
import sys
import re
text ='''| column-0 | column-1 | column-2 | column-3 | sum |
|        5 |        3 |        4 |        5 |  17 |
|        2 |        4 |  $0 + $1 |        4 |  16 |
|        2 |        1 |        3 |  $1 + $2 |  10 |'''

tables = [[],[],[],[],[],[]]
head = []
body1 = []
body2 = []
body3 = []
#tlen = len(tables)
#a = len(text.splitlines())
for line in text.splitlines():
    words = line.split('|')
    for i in range(6):
        tables[i].append(words[i+1])

tables.pop()#删除最后一个空的列表

for i in range(4):
	head.append(tables[i][0])
	body1.append(tables[i][1])
	body2.append(tables[i][2])
	body3.append(tables[i][3])
a = '<tr>\n<td>'+'</td><td>'.join(head)+'</td>'
b = '<tr>\n<td>'+'</td><td>'.join(body1)+'</td>'
c = '<tr>\n<td>'+'</td><td>'.join(body2)+'</td>'
d = '<tr>\n<td>'+'</td><td>'.join(body3)+'</td>\n</tr>'
ss = a+b+c+d
print '<table>'

os.chdir("C:\Program Files (x86)\Google\Chrome\Application")
print os.getcwd()
os.system('chrome.exe',ss)

print '</table>'
