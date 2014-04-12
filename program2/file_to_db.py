#coding:UTF-8

import MeCab
import codecs
import MySQLdb
import hogefn

dbh=hogefn.mydb()
ss=hogefn.searchsentence()

f=open("test.txt","r")
fdata=f.read()

mecabresult=hogefn.mecabact(fdata)
wordsdetail=ss.grammer(mecabresult)

dbh.addwords(wordsdetail)
dbh.closedb()
f.close()
