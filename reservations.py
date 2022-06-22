from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DbConnect import DBConnect
from DBFileList import ListMe

dbconnet=DBConnect()
#title=
root=Tk()
root.title("reservation sheet client")
root.configure(background='grey')
#style=
style = ttk.Style()
style.theme_use("classic")
style.configure('TLabel', background='grey')
style.configure('TButton', background='grey')
style.configure('TRadiobutton', background='grey')

#FullName=
ttk.Label(root,text="FullName:").grid(row=0, column=0, padx=10, pady=10)
EntryFullName=ttk.Entry(root,width=20, font=("Arial", 16))
EntryFullName.grid(row=0, column=1,columnspan=2, padx=10, pady=10)

#Gender=
ttk.Label(root,text="Gender:").grid(row=1, column=0, padx=10, pady=10)
gender = StringVar()
ttk.Radiobutton(root, text="Male", variable=gender, value="Male").grid(row=1, column=1)
ttk.Radiobutton(root, text="Female", variable=gender, value="Female").grid(row=1, column=2)

#Comment=
ttk.Label(root,text="Comments:").grid(row=2, column=0)
txtcomment=Text(root, width=40, height=20, font=('Arial', 16))
txtcomment.grid(row=2, column=1, columnspan=2)

#Buttons=
busumbit=ttk.Button(root,text='Sumbit')
busumbit.grid(row=3, column=2)
bulist=ttk.Button(root, text='List Res')
bulist.grid(row=3, column=1)


#Commands=
def Sumbitdata():
    #print('FullName:{}'.format(EntryFullName.get()))
    #print('Gender:{}'.format(gender.get()))
    #print('FullName:{}'.format(txtcomment.get(1.0, 'end')))
    msg=dbconnet.Add(EntryFullName.get(), gender.get(), txtcomment.get(1.0, 'end'))
    messagebox.showinfo(title='hello!', message=msg)
    EntryFullName.delete(0, 'end')
    txtcomment.delete(1.0, 'end')

def listdata():
    #print('not implimented yet')
    listrequest=ListMe()



busumbit.config(command=Sumbitdata)
bulist.config(command=listdata)




root.mainloop()