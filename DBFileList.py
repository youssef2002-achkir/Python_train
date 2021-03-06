from tkinter import *
from tkinter import ttk
from DbConnect import DBConnect
dbconnect=DBConnect()


class ListMe:
    def __init__(self):
        self._root = Tk()
        self._dbconnect = DBConnect()
        tv = ttk.Treeview(self._root)
        tv.pack()
        tv.heading('#0', text='ID')
        tv.configure(column=('#FullName', '#Gender', '#CNI'))
        tv.heading('#FullName', text='FullName')
        tv.heading('#Gender', text='Gender')
        tv.heading('#CNI', text='CNI')
        cursor=self._dbconnect.Listrequest()
        for row in cursor:
            tv.insert('', 'end', '#{}'.format(row['ID']), text=row['ID'])
            tv.set('#{}'.format(row['ID']), '#FullName', row['FullName'])
            tv.set('#{}'.format(row['ID']), '#Gender', row['Gender'])
            tv.set('#{}'.format(row['ID']), '#CNI', row['CNI'])
        fr=ttk.Frame(self._root)
        fr.pack()
        fr.config(width=30, height=40)
        b1=ttk.Button(fr, text='delete')
        b1.grid(row=0, column=1)
        b2=ttk.Button(fr, text='update')
        b2.grid(row=0, column=3)
        b1.config(command=DBConnect.DeleteRecord(''))
        #b2.config(command=DBConnect.UpdateRecord(12345, 1))
        self._root.mainloop()
class ListMother:
    def __init__(self):
        self._root = Tk()
        self._dbconnect = DBConnect()
        tvm = ttk.Treeview(self._root)
        tvm.pack()
        tvm.heading('#0', text='ID')
        tvm.configure(column=('#MotherName', '#MotherJob', '#MotherAge'))
        tvm.heading('#MotherName', text='MotherName')
        tvm.heading('#MotherJob', text='MotherJob')
        tvm.heading('#MotherAge', text='MotherAge')
        cursor = self._dbconnect.ListrequestM()
        for row in cursor:
            tvm.insert('', 'end', '#{}'.format(row['ID']), text=row['ID'])
            tvm.set('#{}'.format(row['ID']), '#MotherName', row['MotherName'])
            tvm.set('#{}'.format(row['ID']), '#MotherJob', row['MotherJob'])
            tvm.set('#{}'.format(row['ID']), '#MotherAge', row['MotherAge'])
        frm = ttk.Frame(self._root)
        frm.pack()
        frm.config(width=30, height=40)
        b1m = ttk.Button(frm, text='delete')
        b1m.grid(row=0, column=1)
        b2m = ttk.Button(frm, text='update')
        b2m.grid(row=0, column=3)

        b2m.config(command=DBConnect.UpdateRecord)
        self._root.mainloop()

class ListFather:
    def __init__(self):
     self._root = Tk()
     self._dbconnect = DBConnect()
     tvf = ttk.Treeview(self._root)
     tvf.pack()
     tvf.heading('#0', text='ID')
     tvf.configure(column=('#FatherName', '#FatherJob', '#FatherAge'))
     tvf.heading('#FatherName', text='FatherName')
     tvf.heading('#FatherJob', text='FatherJob')
     tvf.heading('#FatherAge', text='FatherAge')
     cursor = self._dbconnect.ListrequestF()
     for row in cursor:
         tvf.insert('', 'end', '#{}'.format(row['ID']), text=row['ID'])
         tvf.set('#{}'.format(row['ID']), '#FatherName', row['FatherName'])
         tvf.set('#{}'.format(row['ID']), '#FatherJob', row['FatherJob'])
         tvf.set('#{}'.format(row['ID']), '#FatherAge', row['FatherAge'])
     frf = ttk.Frame(self._root)
     frf.pack()
     frf.config(width=30, height=40)
     b1f = ttk.Button(frf, text='delete')
     b1f.grid(row=0, column=1)
     b2f= ttk.Button(frf, text='update')
     b2f.grid(row=0, column=3)
     b2f.config(command=DBConnect.UpdateRecord)
     self._root.mainloop()
