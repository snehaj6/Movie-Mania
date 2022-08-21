from tkinter import *
import movie_mania
from tkinter import messagebox
def mode():
   #Creating window
   window=Tk()
   window.title('Select Mode')
   window.configure(bg='black')

   #Adding text
   lbl1=Label(window,text='Welcome to MOVIE MANIA',font=('Algerian','30'),bg='black',fg='blue')
   lbl1.grid(row=0,column=5)
   lbl2=Label(window,text="Please select the mode you want to enter",font=('Times New Roman','25'),bg='black',fg='dodger blue')
   lbl2.grid(row=1,column=5)
   lbl3=Label(window,text= "1.User ",font=('Times New Roman','25'),bg='black',fg='skyblue')
   lbl3.grid(row=2,column=5)
   lbl4=Label(window,text="2.Admin",font=('Times New Roman','25'),bg='black',fg='skyblue')
   lbl4.grid(row=3,column=5)
   btnu=Button(window,text='User',font=('Times New Roman','15'),command=lambda:[movie_mania.game(),window.destroy()],bg='azure4',borderwidth=15)
   btnu.grid(row=4,column=5)
   btna=Button(window,text='Admin',font=('Times New Roman','15'),command=lambda:[admin(),window.destroy()],borderwidth=15,bg='azure4')
   btna.grid(row=5,column=5)
    
mode()
def admin():
   start=Tk()
   start.title('Admin')
   start.configure(bg='black')
   lbl2=Label(start,text="What would you like to do?",font=('Times New Roman','25'),bg='black',fg='blue')
   lbl2.grid(row=1,column=5)
   lbl3=Label(start,text= "1.Add Movie ",font=('Times New Roman','25'),bg='black',fg='dodger blue')
   lbl3.grid(row=2,column=5)
   lbl4=Label(start,text="2.Delete Movie",font=('Times New Roman','25'),bg='black',fg='dodger blue')
   lbl4.grid(row=3,column=5)
   btnu=Button(start,text='Add Movie',font=('Times New Roman','15'),command=lambda:[choice('add'),start.destroy()],bg='azure4',borderwidth=15)
   btnu.grid(row=4,column=5)
   btna=Button(start,text='Delete Movie',font=('Times New Roman','15'),command=lambda:[choice('delete'),start.destroy()],borderwidth=15,bg='azure4')
   btna.grid(row=5,column=5)
   
def choice(ans):
    if (ans=='delete'):
            global movie
            entry=Tk()
            entry.configure(bg='black')
            l_name=Label(entry,text='Enter movie you want to delete',font=('Times New Roman','25'),bg='black',fg='SteelBlue3').grid(row=1,column=1)
            movie=Entry(entry,borderwidth=15)
            movie.grid(row=1,column=2)
            Button(entry,text='Submit',command=lambda:[delete(),entry.destroy()],font=('Times New Roman','15'),borderwidth=15,bg='azure4',fg='black').grid(row=3,column=2)
            
    if (ans=='add'):
            global m_ovie,year,Type,actor,actress
            entry=Tk()
            entry.configure(bg='black')
            l_movie=Label(entry,text='Enter movie you want to add',font=('Times New Roman','25'),bg='black',fg='SteelBlue3').grid(row=1,column=1)
            m_ovie=Entry(entry,borderwidth=15)
            m_ovie.grid(row=1,column=2)
            l_year=Label(entry,text='Enter year of the movie',font=('Times New Roman','25'),bg='black',fg='SteelBlue3').grid(row=2,column=1)
            year=Entry(entry,borderwidth=15)
            year.grid(row=2,column=2)
            l_type=Label(entry,text='Enter type of the movie',font=('Times New Roman','25'),bg='black',fg='SteelBlue3').grid(row=3,column=1)
            Type=Entry(entry,borderwidth=15)
            Type.grid(row=3,column=2)
            l_actor=Label(entry,text='Enter actor of the movie',font=('Times New Roman','25'),bg='black',fg='SteelBlue3').grid(row=4,column=1)
            actor=Entry(entry,borderwidth=15)
            actor.grid(row=4,column=2)
            l_actress=Label(entry,text='Enter actress of the movie',font=('Times New Roman','25'),bg='black',fg='SteelBlue3').grid(row=5,column=1)
            actress=Entry(entry,borderwidth=15)
            actress.grid(row=5,column=2)
            Button(entry,text='Submit',command=lambda:[add(),entry.destroy()],font=('Times New Roman','15'),borderwidth=15,bg='azure4',fg='black').grid(row=6,column=2)
            
        

def delete():
    import mysql.connector as c
    m=c.connect(host="localhost",user="root",passwd="1234",database="movie_mania")
    my=m.cursor()
    m_g=movie.get()
    m_get=m_g.upper()
    my.execute("select * from m_movie where Movie=%s" %("'"+m_get+"'"))
    p=my.fetchone()
    if p!=None:
        my.execute("delete from m_movie where Movie=%s" %("'"+m_get+"'"))
        m.commit()
        messagebox.showinfo('Admin','Movie successfully deleted')
        mode()
    else:
        messagebox.showwarning('Admin','No such movie found')
        admin()


def add():
    import mysql.connector as c
    m=c.connect(host="localhost",user="root",passwd="1234",database="movie_mania")
    my=m.cursor()
    mov=m_ovie.get()
    mo=mov.upper()
    y=int(year.get())
    t=Type.get()
    ac=actor.get()
    act=actress.get()
    my.execute("select * from m_movie where Movie=%s" %("'"+mo+"'"))
    p=my.fetchone()
    if p!=None:
       messagebox.showwarning('Admin','Movie already there')
       admin()
    else:
      my.execute("insert into m_movie values(%s,%d,%s,%s,%s)" %("'"+mo+"'",y,"'"+t+"'","'"+ac+"'","'"+act+"'"))
      m.commit()
      messagebox.showinfo('Admin','Movie successfully added')
      mode()
