from tkinter import *
import random
import mysql_cs_1
import mysql.connector as c
from tkinter import messagebox 

def hollywood():
    global points
    points=0

    #creating window 
    holly=Tk()
    holly.title('hollywood')
    holly.configure(bg='LightBlue2')

    #inserting data in playerdata table
    def f3(a_get,n_get,final):
           m=c.connect(host="localhost",user="root",passwd="1234",database="player_data")
           my=m.cursor()
           my.execute("insert into playerdata values(%d,%s,%d)" %(a_get,"'"+n_get+"'",final))
           m.commit()

    #fetching data for leaderbaord
    def f4():
          global p
          m=c.connect(host="localhost",user="root",passwd="1234",database="player_data")
          my=m.cursor()
          my.execute("select Name,Score from playerdata order by Score desc" ) 
          p=my.fetchall()

    #updating score of old player         
    def f5(marks,n_get,a_get):
          m=c.connect(host="localhost",user="root",passwd="1234",database="player_data")
          my=m.cursor()
          my.execute("Update playerdata set Score=%d where Name=%s and Age=%d" %(marks,"'"+n_get+"'",a_get) )
          m.commit()

    #checking if player is new or old            
    def f6(lst):
          global q
          m=c.connect(host="localhost",user="root",passwd="1234",database="player_data")
          my=m.cursor()
          my.execute("select Age,Name from playerdata " ) 
          q=my.fetchall()
          if lst not in q:
              f3(a_get,n_get,final)
          else:
              f9(final)
              f5(marks,n_get,a_get)

    #adding new score in old score of old player
    def f9(final):
          global marks
          m=c.connect(host="localhost",user="root",passwd="1234",database="player_data")
          my=m.cursor()
          my.execute("select Score from playerdata where Name=%s and Age=%d" %("'"+n_get+"'",a_get) )
          a=my.fetchone()
          for i in a:
              marks=i+final
              
    #fetching data from table m_movie        
    def f7():
       global h,Year,Actor,Actress
       my=c.connect(host="localhost",user="root",passwd="1234",database="movie_mania")
       choose=my.cursor()
       choose.execute("select * from m_movie where Type='hollywood' order by rand()limit 1;")
       p=choose.fetchall()
       for i in p:
        l=list(i)
        h=l[0]
        Year=l[1]
        Actor=l[3]
        Actress=l[4]

    f7()

    #creating question to guess
    def create_question():
            global ques,s
            s=''
            ques=[]
            for i in range(len(h)):
                   if (h[i] == " "):
                         ques.append(" ")
                   else:
                         ques.append("*")
             
            s=''.join(ques)
            Label(holly,text=s,font=('Times New Roman', 30),fg='white',bg='LightBlue2').grid(row=0,column=0,columnspan=13,pady=20)
    create_question()   

    #creating colorful keyboard 
    n=0
    alp=[('A','#FF6663'),('B','#FEB144'),('C','#FDFD97'),('D','#9EE09E'),('E','#9EC1CF'),('F','#D1C2FF'),('G','#CC99C9'),('H','#D1C2FF'),('I','#9EC1CF'),
         ('J','#9EE09E'),('K','#FDFD97'),('L','#FEB144'),('M','#FF6663'),
         ('N','#FF6663'),('O','#FEB144'),('P','#FDFD97'),('Q','#9EE09E'),('R','#9EC1CF'),('S','#D1C2FF'),('T','#CC99C9'),('U','#D1C2FF'),('V','#9EC1CF'),
         ('W','#9EE09E'),('X','#FDFD97'),('Y','#FEB144'),('Z','#FF6663')]

    for j,k in alp:
         
         Button(holly,text=j,command=lambda j=j:guess(j),font=('Times New Roman',18),width=4,bg=k,fg='White',borderwidth=10).grid(row=1+n//13,column=n%13)
         n+=1
    
    
    
    global chance
    chance=s.count('*')
    status=Label(holly,text='Chances Remaining: '+str(chance),font=('Times New Roman',18),bd=1,relief='sunken',anchor=E)
    status.grid(row=8,column=0,columnspan=13,sticky=W+E)   #displaying remaining chances
    already=[]
    
    def guess(j):       # checking if the guessed letter is in movie or not
        global chance,points,final
        s=''
        if (j not in already):
             if j in h:         #if guessed letter is in the movie
                    for i in range(len(h)):
                              if (h[i]==j):
                               ques[i]=j    #updating the question with guessed letter
                        
                    already.append(j)
                    s=''.join(ques)
                    points+=1
                    
                  
                    if (s!=h):    #if movie is not guessed completely
                       Label(holly,text=s,font=('Times New Roman', 30),bg='LightBlue2',fg='White').grid(row=0,column=0,columnspan=13,pady=20)
                       
                    
                    
                    elif(s==h):    #if movie is guessed completely
                        Label(holly,text=s,font=('Times New Roman', 30),bg='LightBlue2',fg='White').grid(row=0,column=0,columnspan=13,pady=20)
                        final=points+chance
                        messagebox.showinfo('Movie Mania','Congratulations! You won! \n Your score is '+str(final))
                        messagebox.showinfo('Movie Mania','Thank You for playing')
                        check=Button(holly,text='Check Leaderboard',command=lambda:[leaderboard(),holly.destroy()],font=('Times New Roman', 23),borderwidth=10,bg='brown',fg='white')
                        check.grid(row=7,column=0,columnspan=13)            
                      
                        
             
             elif(j not in h):        #if guessed letter is not in the movie
                messagebox.showwarning('Movie Mania','Sorry ' + j + ' is not in the movie')
                already.append(j)
                points-=1
                chance-=1
                if (chance==0):
                        status=Label(holly,text='Chances Remaining: '+str(chance),font=('Times New Roman',18),bd=1,relief='sunken',anchor=E)
                        status.grid(row=8,column=0,columnspan=13,sticky=W+E)
                        end()                      #game ends if chance=0
                else:
                        status=Label(holly,text='Chances Remaining: '+str(chance),font=('Times New Roman',18),bd=1,relief='sunken',anchor=E)
                        status.grid(row=8,column=0,columnspan=13,sticky=W+E)              #updating remaining chances
                
        else:
                messagebox.showwarning('Movie Mania',"DON'T CHEAT! You have already guessed "+j) #displaying message if user guesses the same letter again


    #creating hint and end button           
    f=1
    bend=Button(holly,text='END',command=lambda:end(),font=('Times New Roman', 17),borderwidth=10,bg='Red',fg='White')
    bend.grid(row=6,column=12,pady=20)
    bhint=Button(holly,text='HINT',command=lambda:hint(f),font=('Times New Roman', 16),borderwidth=10,bg='green2',fg='White')
    bhint.grid(row=6,column=0,pady=20)

    #displaying hints
    def hint(f):
            
            if(f==1):
                messagebox.showinfo('Movie Mania','This movie is from '+str(Year))
                f+=1
                bhint=Button(holly,text='HINT',command=lambda:hint(f),font=('Times New Roman', 16),borderwidth=10,bg='green2',fg='White').grid(row=6,column=0,pady=20)
            elif(f==2 ):
                messagebox.showinfo('Movie Mania','This movie is of '+Actor)
                f+=1
                bhint=Button(holly,text='HINT',command=lambda:hint(f),font=('Times New Roman', 16),borderwidth=10,bg='green2',fg='White').grid(row=6,column=0,pady=20)
            elif(f==3 ):
                messagebox.showinfo('Movie Mania','This movie is of '+Actress)
                f+=1
                bhint=Button(holly,text='HINT',command=lambda:hint(f),font=('Times New Roman', 16),borderwidth=10,bg='green2',fg='White').grid(row=6,column=0,pady=20)
            elif(f>=4 ):
                messagebox.showwarning('Movie Mania','Oops! No more hints are available')
                f+=1
                bhint=Button(holly,text='HINT',command=lambda:hint(f),font=('Times New Roman', 16),borderwidth=10,bg='green2',fg='White').grid(row=6,column=0,pady=20)

    #ending the game if user clicks end button
    def end():
            global final
            final=points+chance
            messagebox.showwarning('Movie Mania', "Sorry you weren't able to guess the movie \n "+h+' is the movie \n Your score is '+str(final))
            messagebox.showinfo('Movie Mania','Thank You for playing')
            check=Button(holly,text='Check Leaderboard',command=lambda:[leaderboard(),holly.destroy()],font=('Times New Roman', 23),borderwidth=10,bg='brown',fg='white')
            check.grid(row=7,column=0,columnspan=13)

    #creating leaderbaord to display score of all the players
    def leaderboard():
            global name,age,l_name,l_age,btn
            entry=Tk()
            entry.configure(bg='black')
            l_name=Label(entry,text='Enter your name  ',font=('Times New Roman','25'),bg='black',fg='SteelBlue3').grid(row=1,column=1)
            name=Entry(entry,borderwidth=15)
            name.grid(row=1,column=2)
            l_age=Label(entry,text='Enter your age  ',font=('Times New Roman','25'),bg='black',fg='SteelBlue3').grid(row=2,column=1)
            age=Entry(entry,borderwidth=15)
            age.grid(row=2,column=2)
            Button(entry,text='Submit',command=lambda:[submit(),entry.destroy()],font=('Times New Roman','15'),borderwidth=15,bg='azure4',fg='black').grid(row=3,column=2)

    def submit():
            global lst,a_get,n_get
            a_get=int(age.get())
            n_get=name.get()
            lst=(a_get,n_get)
            f6(lst)
            f4()
            leaderboard=Tk()
            leaderboard.title('Leaderboard')
            leaderboard.configure(bg='black')
            Label(leaderboard,text='SNO.',font=('Times New Roman','25'),bg='black',fg='SteelBlue3').grid(row=0,column=0)
            Label(leaderboard,text='NAME',font=('Times New Roman','25'),bg='black',fg='SteelBlue3').grid(row=0,column=1)
            Label(leaderboard,text='SCORE',font=('Times New Roman','25'),bg='black',fg='SteelBlue3').grid(row=0,column=2)
            c=1
            for i in p:
                    Label(leaderboard,text=c,font=('Times New Roman','25'),bg='black',fg='SteelBlue3').grid(row=c,column=0)
                    Label(leaderboard,text=i[0],font=('Times New Roman','25'),bg='black',fg='SteelBlue3').grid(row=c,column=1)
                    Label(leaderboard,text=i[1],font=('Times New Roman','25'),bg='black',fg='SteelBlue3').grid(row=c,column=2)
                    c+=1
        
