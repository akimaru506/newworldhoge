#About this program

- It reads sentences in the text file and analyzes them by using MeCab. Then it makes sentences with the rules of Japanese grammar.  
- It puts the results of analyses in MySQL database.The table in newworldhoge database is as follow.  

|wordname|parts|
|:-------|-----|
|みかん  |名詞 |
|食べる  |動詞 |
|...     |...  |

- To run this program, following things are required.  
  1. Python  
  1. MeCab  
  1. MySQL  
  1. MySQL-Python  
  1. file named 'test.txt 'which has Japanese sentence to input  
  1. database and table(You can create them if you execute commands on 'commands.sql'. If you create them by using that file, please change username and password as you like.)  
