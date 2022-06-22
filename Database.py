import sqlite3
db = sqlite3.connect("information.db")
db.row_factory=sqlite3.Row
db.execute("create table if not exists Youssef(Name text, Age int)")
db.execute("insert into Youssef (Name , Age ) values (?, ?)", ("joseph", 20))
db.commit()
cursor=db.execute("select * from Youssef")
for row in cursor :
    print("Name:{},Age:{}".format(row["Name"], row["Age"]))

