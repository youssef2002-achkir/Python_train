from tkinter import *
from tkinter import ttk
root = Tk()
style = ttk.Style()
style.theme_use('classic')
ttk.Label(root, background='grey',  text='0').grid(row=0, column=0, sticky='snew', ipadx=10, ipady=10, padx=15, pady=15)
ttk.Label(root, background='red',  text='1').grid(row=0, column=1, sticky='snew', ipadx=10, ipady=10, padx=15, pady=15)
ttk.Label(root, background='green',  text='2').grid(row=0, column=2, sticky='snew', ipadx=10, ipady=10, padx=15, pady=15)
ttk.Label(root, background='grey',  text='3').grid(row=1, column=0, sticky='snew', ipadx=10, ipady=10, padx=15, pady=15)
ttk.Label(root, background='red',  text='4').grid(row=1, column=1, sticky='snew', ipadx=10, ipady=10, padx=15, pady=15)
ttk.Label(root, background='green',  text='5').grid(row=1, column=2, sticky='snew', ipadx=10, ipady=10, padx=15, pady=15)
ttk.Label(root, background='grey',  text='6').grid(row=2, column=0, sticky='snew', ipadx=10, ipady=10, padx=15, pady=15)
ttk.Label(root, background='red',  text='7').grid(row=2, column=1, sticky='snew', ipadx=10, ipady=10, padx=15, pady=15)
ttk.Label(root, background='green',  text='8').grid(row=2, column=2, sticky='snew', ipadx=10, ipady=10, padx=15, pady=15)
ttk.Label(root, background='grey',  text='9').grid(row=3, column=0, sticky='snew', ipadx=10, ipady=10, padx=15, pady=15)
ttk.Label(root, background='red',  text='+').grid(row=3, column=1, sticky='snew', ipadx=10, ipady=10, padx=15, pady=15)
ttk.Label(root, background='green',  text='-').grid(row=3, column=2, sticky='snew', ipadx=10, ipady=10, padx=15, pady=15)
ttk.Label(root, background='grey',  text='*').grid(row=4, column=0, sticky='snew', ipadx=10, ipady=10, padx=15, pady=15)
ttk.Label(root, background='red',  text='/').grid(row=4, column=1, sticky='snew', ipadx=10, ipady=10, padx=15, pady=15)
ttk.Label(root, background='green',  text='e').grid(row=4, column=2, sticky='snew', ipadx=10, ipady=10, padx=15, pady=15)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=2)
root.rowconfigure(2, weight=3)
root.rowconfigure(3, weight=4)
root.rowconfigure(4, weight=5)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=4)


root.mainloop()









