# coding:UTF-8
import tweepy

class twittercn (object):
  def get_apifn(self):
    api_key='UP9jACCD0cNYWjdNgH8XHQ'
    api_secret='IFugBoNp7JyWxR1iXKWSBf0Wegz9IifToEFBMzkkg4'
    access_token='1688027426-8jGmf0n4LXTfztgjvpzy8ixIR98I80pVdq6nG2s'
    access_token_secret='vEkcby4OBa82OUgrw6vdV7yJfPt6y2aRSNr6BcMh347GB'

    connect=tweepy.OAuthHandler(api_key,api_secret)
    connect.set_access_token(access_token,access_token_secret)
    t=tweepy.API(connect)
    return t

class deal_strs (object):
  def __init__(self,s):
    print s
    self.strs=s
  def rem_uname(self):
    char_list=list(self.strs)
    while u'@' in char_list:
      un_num=char_list.index(u'@')
      h=un_num
#例えば、この2行後の部分でindex is out of rangeとなった場合、user名の終わりがwhile文の条件に指定している文字でない可能性がある。
      while char_list[h]!=u' ' and char_list[h]!=u')' and char_list[h]!=u':':
        char_list[h]=u'\\'
        if (h+1)==len(char_list):
          break
        h+=1
      char_list[h]=u'\\'
    return char_list

  def rem_address(self):
    char_list=list(self.strs)
    while u'h' in char_list:
      print 'yes!'
      ht_num=char_list.index(u'h')
      h=ht_num
      if char_list[h+1]==u't' and char_list[h+2]==u't' and char_list[h+3]==u'p' :
        while char_list[h]!=u' ' and char_list[h]!=u')'  and char_list[h]!=u'#':
          char_list[h]=u'\\'
          print h
          print '**'
          print len(char_list)
          print '**'
          if (h+1)==len(char_list):
            break
          h+=1
        char_list[h]=u'\\'
      else :
        char_list[h]=u'\\'
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
