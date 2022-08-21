from tkinter import *
from bollywood1 import *
from hollywood1 import *

def game():
   #Creating window
   window=Tk()
   window.title('Movie Mania')
   window.configure(bg='black')

   #Adding text
   lbl1=Label(window,text='Welcome to MOVIE MANIA',font=('Algerian','50'),bg='black',fg='deep pink')
   lbl1.grid(row=0,column=5)
   lbl2=Label(window,text='Rules of the games are as follows:',font=('Times New Roman','35'),bg='black',fg='Red')
   lbl2.grid(row=1,column=5)
   lbl3=Label(window,text='1.You will get a chance to choose the type of movie you want to guess.',font=('Times New Roman','25'),bg='black',fg='Orange')
   lbl3.grid(row=2,column=5)
   lbl4=Label(window,text='2.You will get a movie to guess.',font=('Times New Roman','25'),bg='black',fg='Yellow')
   lbl4.grid(row=3,column=5)
   lbl5=Label(window,text='3.You can get 3 hints.',font=('Times New Roman','25'),bg='black',fg='SpringGreen4')
   lbl5.grid(row=4,column=5)
   lbl6=Label(window,text='4.You get a point every time you guess a correct letter.',font=('Times New Roman','25'),bg='black',fg='dodger blue')
   lbl6.grid(row=5,column=5)
   lbl7=Label(window,text='5.You lose a point every time you guess a wrong letter. ',font=('Times New Roman','25'),bg='black',fg='blue')
   lbl7.grid(row=6,column=5)
   lbl8=Label(window,text='6.Remaining chances will be added to your final score ',font=('Times New Roman','25'),bg='black',fg='darkviolet')
   lbl8.grid(row=7,column=5)
   lbl9=Label(window,text='ALL THE BEST!! ',font=('Times New Roman','25'),bg='black',fg='white')
   lbl9.grid(row=8,column=5)
   
   btn=Button(window,text='Click Here',font=('Times New Roman','15'),command=lambda:[fun(),window.destroy()],borderwidth=15,bg='azure4')
   btn.grid(row=9,column=5)

   
def fun():
    start=Tk()
    start.configure(bg='black')
    start.title("Let's start")
    
    lbl11=Label(start,text="Let's start the game",font=('Times New Roman','45'),bg='black',fg='Blue')
    lbl11.grid(row=0,column=5)
    lbl12=Label(start,text="Which type of movie would you like to guess?",font=('Times New Roman','25'),bg='black',fg='dodger blue')
    lbl12.grid(row=1,column=5)
    lbl13=Label(start,text= "1.Bollywood ",font=('Times New Roman','25'),bg='black',fg='deep pink')
    lbl13.grid(row=2,column=5)
    lbl14=Label(start,text="2.Hollywood",font=('Times New Roman','25'),bg='black',fg='deep pink')
    lbl14.grid(row=3,column=5)
    btnb=Button(start,text='Bollywood',font=('Times New Roman','15'),command=lambda:[bollywood(),start.destroy()],bg='azure4',borderwidth=15)
    btnb.grid(row=4,column=5)
    btnh=Button(start,text='Hollywood',font=('Times New Roman','15'),command=lambda:[hollywood(),start.destroy()],borderwidth=15,bg='azure4')
    btnh.grid(row=5,column=5)
    


    
   











