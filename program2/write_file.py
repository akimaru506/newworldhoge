# coding:UTF-8
import hogefn
import codecs
t=hogefn.twittercn().get_apifn()


#f=open('userlist.txt','r')
fo=codecs.open('test.txt','a','utf8')

userlist=hogefn.deal_strs('userlist.txt').give_uname()
for g in userlist:
  user_tl=t.user_timeline(g)
  for j in user_tl:
    c=hogefn.deal_strs(j.text).rem_uname()
    c2=hogefn.deal_strs(c).rem_address()
    delchar_pre=str(list(c2)).decode('unicode-escape')
    c3=hogefn.deal_strs(delchar_pre).rem_unneed()
    fo.write(c3)

