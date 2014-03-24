# coding:UTF-8
import tweepy

class twittercn (object):
  def get_apifn(self):
    api_key=''
    api_secret=''
    access_token=''
    access_token_secret=''

    connect=tweepy.OAuthHandler(api_key,api_secret)
    connect.set_access_token(access_token,access_token_secret)
    t=tweepy.API(connect)
    return t

class deal_strs (object):
  def __init__(self,s):
    self.strs=s
  def rem_uname(self):
    char_list=list(self.strs)
    print char_list
    while u'@' in char_list:
      un_num=char_list.index(u'@')
      h=un_num
      print un_num
#例えば、この2行後の部分でindex is out of rangeとなった場合、user名の終わりがwhile文の条件に指定している文字でない可能性がある。
      print h
      while char_list[h]!=u' ' and char_list[h]!=u')' and char_list[h]!=u':':
        char_list[h]=u'\\'
        if (h+1)==len(char_list):
          break
        h+=1
        print h
      char_list[h]=u'\\'
    return char_list

  def rem_address(self):
    char_list=list(self.strs)
    while u'h' in char_list:
      ht_num=char_list.index(u'h')
      h=ht_num
      if char_list[h+1]==u't' and char_list[h+2]==u't' and char_list[h+3]==u'p' and (char_list[h+4]==u':' or char_list[h+4]==u's') :
        while char_list[h]!=u' ' and char_list[h]!=u')'  and char_list[h]!=u'#':
          char_list[h]=u'\\'
          print '**'
          print h
          print '**'
          print len(char_list)
          print '**'
          if (h+1)==len(char_list):
            break
          h+=1
          print h
          print '**'
        char_list[h]=u'\\'
      else :
        break
    return char_list
  def rem_unneed(self):
    delchar_pre=self.strs
    str_main1=delchar_pre.replace("'","")
    str_main2=str_main1.replace("u","")
    str_main3=str_main2.replace(",","")
    str_main4=str_main3.replace("[","")
    str_main5=str_main4.replace("]","")
    str_main7=str_main5.replace(" ","")
    delchar=str_main7.replace("\\","")
    delchar=delchar.replace("EOS","\\")
    return delchar

  def give_uname(self):
    fname=self.strs
    f=open(fname,'r')
    chardata=f.read()+'\\'
    #char_list=list(chardata)
    print chardata
    print '\n'
    #print char_list
    chardata=chardata.replace("@","")
    i=0
    username=''
    userlist=[]
    while chardata[i]!='\\':
      username=''
      while chardata[i]!='\n':
        username+=chardata[i]
        i+=1
      userlist.append(username)
      i+=1
    return userlist
