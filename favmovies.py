import sqlite3
conn=sqlite3.connect("movies.db")
c=conn.cursor()
c.execute("""create table favmovies(name text,actor text,actress text,director text,year_of_release integer)""")
rows=[('Thimmarusu','Satyadev kancharana','Priyanka Jawalkar','Sharan koppisetty',2021),
('Narappa','Venkatesh','Priyamani','Srikanth addala',2021),
('Paagal','Vishwak Sen','Nivetha Pethuraj','Naresh Kuppili',2021),
('Jaanu','Sharwanand','Samantha Akkineni','C.Prem Kumar',2020),
('Hit','Vishwak Sen','Ruhani Sharma','Sailesh Kolanu',2020),
('V','Nani','Nivetha Thomas','Mohana Krishna',2020)]
c.executemany('insert into favmovies values(?,?,?,?,?)',rows)
c.execute("select * from favmovies")
rec=c.fetchall()
print(rec)
conn.commit()
conn.close()
