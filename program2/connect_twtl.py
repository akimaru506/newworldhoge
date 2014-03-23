# coding: UTF-8

import tweepy
import codecs

api_key=''
api_secret=''
access_token=''
access_token_secret=''

connect=tweepy.OAuthHandler(api_key,api_secret)
connect.set_access_token(access_token,access_token_secret)
t=tweepy.API(connect)

f=open('userlist.txt','r')
fo=codecs.open('test.txt','a','utf8')
chardata=f.read()+'\\'
#char_list=list(chardata)
print chardata
print '\n'
#print char_list
chardata=chardata.replace("@","")
i=0
username=''
while chardata[i]!='\\':
  username=''
  while chardata[i]!='\n':
    username+=chardata[i]
    i+=1

  print username
  user_tl=t.user_timeline(username)
  for j in user_tl:
    print j.text
    char_list=list(j.text)
    print char_list
    while u'@' in char_list:
      un_num=char_list.index(u'@')
      h=un_num
      print un_num
#例えば、この2行後の部分でindex is out of rangeとなった場合、user名の終わりがwhile文の条件に指定している文字でない可能性がある。
      print h
      while char_list[h]!=u' ' and char_list[h]!=u')' and char_list[h]!=u':':
        char_list[h]=u'\\'
        h+=1
        print h
      char_list[h]=u'\\'

    while u'h' in char_list:
      ht_num=char_list.index(u'h')
      h=ht_num
      if char_list[h+1]==u't' and char_list[h+2]==u't' and char_list[h+3]==u'p' and char_list[h+4]==u':' :
        while char_list[h]!=u' ' and char_list[h]!=u')'  and char_list[h]!=u'#':
          char_list[h]=u'\\'
          print '**'
          print h
          print '**'
          print len(char_list)
          print '**'
#URLの終端文字検索で最後の要素数に来た場合、ループから外れる
          if (h+1)==len(char_list):
            break
          h+=1
          print h
          print '**'
        char_list[h]=u'\\'
      else :
        break

    delchar_pre=str(list(char_list)).decode('unicode-escape')
    str_main1=delchar_pre.replace("'","")
    str_main2=str_main1.replace("u","")
    str_main3=str_main2.replace(",","")
    str_main4=str_main3.replace("[","")
    str_main5=str_main4.replace("]","")
    str_main7=str_main5.replace(" ","")
    delchar=str_main7.replace("\\","")
    delchar=delchar.replace("EOS","\\")

    print delchar
    fo.write(delchar)
  i+=1
