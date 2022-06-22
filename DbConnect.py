import sqlite3
class DBConnect:
    def __init__(self):
        self._db=sqlite3.connect("Reservation.db")
        self._db.row_factory=sqlite3.Row
        self._db.execute("create table if not exists Me(ID integer primary key autoincrement, FullName text, Gender text, CNI integer)")
        self._db.execute("create table if not exists Mother (ID integer primary key autoincrement, MotherName text, MotherJob text, MotherAge integer )")
        self._db.execute("create table if not exists Father (ID integer primary key autoincrement, FatherName text, FatherJob text, FatherAge integer )")
        self._db.commit()
    def Add(self, Name, Gender, CNI):
        self._db.execute("insert into Me(FullName, Gender, CNI) values(?, ?, ?)", (Name, Gender, CNI))
        self._db.commit()
        return "requirement is submited"
    def AddF(self, FName, FJob, FAge):
        self._db.execute("insert into Father(FatherName, FatherJob, FatherAge) values(?, ?, ?)", (FName, FJob, FAge))
        self._db.commit()
        return "requirement is submited"
    def AddM(self, MName, MJob, MAge):
        self._db.execute("insert into Mother(MotherName, MotherJob, MotherAge) values(?, ?, ?)", (MName, MJob, MAge))
        self._db.commit()
        return "requirement is submited"
    def Listrequest(self):
        cursor=self._db.execute("Select * from Me")
        return cursor

    def ListrequestM(self):
        cursorm = self._db.execute("Select * from Mother")
        return cursorm

    def ListrequestF(self):
        cursorf = self._db.execute("Select * from Father")
        return cursorf


    def DeleteRecord(self,ID):
        self._db.execute('delete from Me where ID={}'.format(ID))
        self._db.commit()
        return 'Record is deleted'
    def UpdateRecord(self,ID, CNI):
        self._db.execute('update Me set CNI=? where ID=?',(CNI, ID))
        self._db.commit()
        return 'Record is updated'
