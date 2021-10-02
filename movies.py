# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 19:43:27 2021

@author: Admin
"""

from tkinter import *
import sqlite3
top=Tk()
top.title("contact book")
conn=sqlite3.connect("mov.db")
c=conn.cursor()
#c.execute("""create table movies(
 #         name text,
  #        actor varchar,
   #       actress integer,
    #      director varchar,
     #     year_of_release integer)
      #    """)

def save():
    conn=sqlite3.connect("mov.db")
    c=conn.cursor()
    c.execute("insert into movies values(:name,:actor,:actress,:director,:year_of_release)",
              {"name":name.get(),
              "actor":actor.get(),
              "actress":actress.get(),
              "director":director.get(),
              "year_of_release":year_of_release.get()
              })
    conn.commit()
    conn.close()
    name.delete(0,END)
    actor.delete(0,END)
    actress.delete(0,END)
    director.delete(0,END)
    year_of_release.delete(0,END)
def show():
    conn=sqlite3.connect("mov.db")
    c=conn.cursor()
    c.execute("select * from movies")
    records=c.fetchall()
    for rec in records:
        Label(top,text=rec).grid(row=8,column=0)
    conn.commit()
    conn.close()
name_l=Label(top,text="Enter name")
name_l.grid(row=0,column=0)
actor_l=Label(top,text="Enter address")
actor_l.grid(row=1,column=0)
actress_l=Label(top,text="Enter phoneno")
actress_l.grid(row=2,column=0)
director_l=Label(top,text="Enter email")
director_l.grid(row=3,column=0)
year_of_release=Label(top,text="enter year")
year_of_release.grid(row=4,column=0)
#entries
name=Entry(top,width=50)
name.grid(row=0,column=1)
actor=Entry(top,width=50)
actor.grid(row=1,column=1)
actress=Entry(top,width=50)
actress.grid(row=2,column=1)
director=Entry(top,width=50)
director.grid(row=3,column=1)
year_of_release=Entry(top,width=50)
year_of_release.grid(row=4,column=1)
save=Button(top,text="save",command=save,width=100)
save.grid(row=5,column=0)
show=Button(top,text="show",command=show,width=100)
show.grid(row=5,column=1)
conn.commit()
conn.close()
top.mainloop()