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

connector = MySQLdb.connect(host="localhost", db="newworldhoge", user="newsekaim", passwd="iq1nS1euaw", charset="utf8")
cursor = connector.cursor()

wordlist=[]
worddic={}
i=0
part_speech=""
wordname=""
part_more=""
#print char_list_new[1]
fo=codecs.open("output.txt","a","utf-8")
print str_main6
while str_main6[i]!="\\":

  while str_main6[i]!="\t":
    print str_main6[i]
    wordname+=str_main6[i]
    fo.write(str_main6[i])
    i+=1

  #fo.write("/")
  i+=1
  while str_main6[i]!="/":
    print str_main6[i]
    part_speech+=str_main6[i]
    fo.write(str_main6[i])
    i+=1
  i+=1
  while str_main6[i]!="/":
    print str_main6[i]
    part_more+=str_main6[i]
    fo.write(str_main6[i])
    i+=1

  fo.write("\n")

  while str_main6[i]!="\n":
    i+=1

  i+=1
  worddic['name']=wordname
  worddic['part']=part_speech
  worddic['pmore']=part_more
  worddic['gram']=''
#actionはその語がされること。
  worddic['action']=''
  wordlist.append(worddic)
  wordname=""
  part_speech=""
  part_more=""
  worddic={}

x=0
while x+1<len(wordlist):
  if wordlist[x]['part']==u'名詞' and  (wordlist[x+1]['name']==u'を' and wordlist[x+1]['part']==u'助詞'):
    wordlist[x]['gram']='o'
    print '目的語TRUE'
    y=x
    while y<len(wordlist):
      if wordlist[y]['part']==u'動詞':
        wordlist[x]['action']=wordlist[y]['name']
        break
      y+=1
  if wordlist[x]['part']==u'名詞' and ((wordlist[x+1]['name']==u'が' and  wordlist[x+1]['pmore']==u'格助詞') or (wordlist[x+1]['name']==u'は' and wordlist[x+1]['pmore']==u'係助詞')):
    wordlist[x]['gram']='s'
    print '主語TRUE'

  x+=1


for n in wordlist:
 #文字はすでに読める状態なので、１行下の文で文字の変換は不要。エラー原因はプレースホルダを使おうとして文法間違いしたものによるらしい
  sql = u"insert into words (wordname,part,part_more,gram,action) values('"+n['name']+"','"+n['part']+"','"+n['pmore']+"','"+n['gram']+"','"+n['action']+"')"
  cursor.execute(sql)
  connector.commit()
cursor.close()
connector.close()


fo.close()

