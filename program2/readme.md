#About programs


##What

- Getting Sentences  
  - File ('connect_twtl.py') is required.  
  - It gets tweet of users who you want to read by using tweepy. Please write names of users on the file ('userlist.txt'). When you write names of useers, please write each of them from '@' and begin a new line to write each of them.  
  - It remove the characters of user name and address which is written from 'http://', from sentences that is from tweets.  
  - The sentences that is read by this program are written on the file ('test.txt').  

- Analyses
  - File ('file_to_db.py') is required.  
  - It reads sentences in the text file ('test.txt') and analyzes them by using MeCab. Then it makes sentences with the rules of Japanese grammar.  
  - It puts the results of analyses in MySQL database.The table in newworldhoge database is as follow.  

  |wordname|parts|
  |:-------|-----|
  |みかん  |名詞 |
  |食べる  |動詞 |
  |...     |...  |


##Required

- To run these programs, following things are required.  
  1. Python  
  1. MeCab  
  1. codecs
  1. tweepy
  1. MySQL  
  1. MySQL-Python  
  1. file named 'test.txt 'which has Japanese sentence to input  
  1. database and table(You can create them if you execute commands on 'commands.sql'. If you create them by using that file, please change username and password as you like.)  
