# coding: UTF-8
import MeCab
import codecs
import MySQLdb

f=open("test.txt","r")
chardata=f.read()
print chardata
print '\n'

tagger=MeCab.Tagger('mecabrc')
result=tagger.parse(chardata)

print result
result=result.replace(",","/")
result=unicode(result,"utf-8")
char_list=list(result)
#print str(char_list).decode("unicode-escape")

char_list_str=str(char_list).decode("unicode-escape")

str_main1=char_list_str.replace("'","")
str_main2=str_main1.replace("u","")
str_main3=str_main2.replace(",","")
str_main4=str_main3.replace("[","")
str_main5=str_main4.replace("]","")
str_main7=str_main5.replace(" ","")
str_main6=str_main7.replace("EOS","\\")
print str_main6

#print char_list_new

connector = MySQLdb.connect(host="localhost", db="newworldhoge", user="username", passwd="password", charset="utf8")
cursor = connector.cursor()

i=0
part_speech=""
wordname=""

#print char_list_new[1]
fo=codecs.open("output.txt","a","utf-8")

while str_main6[i]!="\\":

  while str_main6[i]!="\t":
    print str_main6[i]
    wordname+=str_main6[i]
    fo.write(str_main6[i])
    i+=1

  #fo.write("/")

  while str_main6[i]!="/":
    print str_main6[i]
    part_speech+=str_main6[i]
    fo.write(str_main6[i])
    i+=1

  fo.write("\n")

  while str_main6[i]!="\n":
    i+=1

  i+=1
#文字はすでに読める状態なので、１行下の文で文字の変換は不要。エラー原因はプレースホルダを使おうとして文法間違いしたものによるらしい
  sql = u"insert into words (wordname,part) values('"+wordname+"','"+part_speech+"')"
  cursor.execute(sql)
  connector.commit()

  wordname=""
  part_speech=""

cursor.close()
connector.close()


fo.close()

