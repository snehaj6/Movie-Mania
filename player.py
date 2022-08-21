import mysql.connector as c

def f():
 m=c.connect(host="localhost",user="root",passwd="1234",database="player_data")
 my=m.cursor()
 my.execute("create table playerdata (Age int ,Name varchar(30),primary key(Age,Name))")
def f1():
 m=c.connect(host="localhost",user="root",passwd="1234",database="player_data")
 my=m.cursor()
 my.execute("show tables")
 for i in my:
  print(i)
def f2():
 m=c.connect(host="localhost",user="root",passwd="1234",database="player_data")
 my=m.cursor()
 my.execute("desc playerdata")
 for i in my:
  print(i)

def f3():
 m=c.connect(host="localhost",user="root",passwd="1234",database="player_data")
 my=m.cursor()
 my.execute("select * from playerdata")
 p=my.fetchall()
 for i in p:
  print(i)

