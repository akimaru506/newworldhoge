# coding:UTF-8

'''newworldhogeプログラムに必要な処理をまとめたモジュールです。'''

import tweepy
import MySQLdb
import codecs
import MeCab


class twittercn (object):
  '''Twitter処理関係の関数をまとめています。'''
  def get_apifn(self):
    '''APIキー、アクセストークンの設定をしたクラスを返します。引数不要'''
    api_key='UP9jACCD0cNYWjdNgH8XHQ'
    api_secret='IFugBoNp7JyWxR1iXKWSBf0Wegz9IifToEFBMzkkg4'
    access_token='1688027426-8jGmf0n4LXTfztgjvpzy8ixIR98I80pVdq6nG2s'
    access_token_secret='vEkcby4OBa82OUgrw6vdV7yJfPt6y2aRSNr6BcMh347GB'

    connect=tweepy.OAuthHandler(api_key,api_secret)
    connect.set_access_token(access_token,access_token_secret)
    t=tweepy.API(connect)
    return t

def mecabact(chardata):
  '''MeCabで品詞分解し、単語と品詞をディクショナリにまとめたリストを返します。引数には処理したい文字列を指定します。'''
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
    worddic['nature']=''
    wordlist.append(worddic)
    wordname=""
    part_speech=""
    part_more=""
    worddic={}


  return wordlist


class searchsentence(object):
  '''文の上での単語の役割の判定等をする関数をまとめています。'''
  def grammer(self,wordlist):
    '''hogefn.mecabact()で作られたリストから目的語、動詞、主語の判定をし、その結果をhogefn.mecabact()で返されたリストにディクショナリとして追加します。引数にはhogefn.mecabact()で渡されたリストを指定します。'''
    x=0
    keiyousi=''
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
      if wordlist[x]['part']==u'形容詞':
        keiyousi+=wordlist[x]['name']+'/'
      if wordlist[x]['part']==u'名詞':
        wordlist[x]['nature']=keiyousi
        keiyousi=''
      x+=1
    return wordlist

class mydb (object):
  '''MySQLへの接続等の処理の関数をまとめています。引数不要'''
  def __init__(self):
    '''MySQLのカーソルを作成します。'''
    self.connector = MySQLdb.connect(host="localhost", db="newworldhoge", user="newsekaim", passwd="iq1nS1euaw", charset="utf8")
    self.cursor = self.connector.cursor()

  def addwords(self,wordlist):
    '''hogefn.searchsentence().grammer()で返されたリストをデータベースに登録します。引数にはhogefn.searchsentence().grammer()で渡されたリストを指定'''
    for n in wordlist:
     #文字はすでに読める状態なので、１行下の文で文字の変換は不要。エラー原因はプレースホルダを使おうとして文法間違いしたものによるらしい
      sql = u"insert into words (wordname,part,part_more,gram,action,nature) values('"+n['name']+"','"+n['part']+"','"+n['pmore']+"','"+n['gram']+"','"+n['action']+"','"+n['nature']+"')"
      self.cursor.execute(sql)
      self.connector.commit()

  def closedb(self):
    '''データベースへの接続を閉じます。引数不要。'''
    self.cursor.close()
    self.connector.close()



class deal_strs (object):
  '''特定種類の文字列を取り除く関数を集めています。引数には処理したい文字列を指定。'''
  def __init__(self,s):
    print s
    self.strs=s
  def rem_uname(self):
    '''Twitterのツイートなどから@で始まるユーザーネームを取り除きます。引数不要。'''
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
    '''http://などから始まるアドレスを取り除きます。引数不要。'''
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
    '''文字列をリストにした時に不要になる文字を取り除きます。引数不要。'''
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
    '''ツイート取得時にユーザーリストファイルから取り出すユーザ名から@を取り除きます。インスタンス生成時の引数にユーザーリストファイル名を指定。'''
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
