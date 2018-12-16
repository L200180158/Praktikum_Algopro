from Tkinter import *
pro = Tk (className = 'Ichi Ocha Calculator')
pro.geometry('350x150')

def tambah ():
    hasil=(float(kolom1.get())+float(kolom2.get()))
    ending2.config (text=hasil, font=("Arial 12 bold"))
def kurang ():
    hasil=(float(kolom1.get())-float(kolom2.get()))
    ending2.config (text=hasil, font=("Arial 12 bold"))
def kali ():
    hasil=(float(kolom1.get())*float(kolom2.get()))
    ending2.config (text=hasil, font=("Arial 12 bold"))
def bagi ():
    hasil=(float(kolom1.get())/float(kolom2.get()))
    ending2.config (text=hasil, font=("Arial 12 bold"))

data1 = Label (pro, text="Angka 1")
data1.grid(row=1, column=0, sticky='w')
kolom1= Entry (pro)
kolom1.grid(row=1, column=1, sticky='w')

data2 = Label (pro, text="Angka 2")
data2.grid(row=2, column=0, sticky='w')
kolom2 = Entry (pro)
kolom2.grid(row=2, column=1, sticky='w')

tombol1 = Button (pro, text="+", command=tambah)
tombol1.place (x=10, y=60)
tombol2 = Button (pro, text="-", command=kurang)
tombol2.place (x=50, y=60)
tombol3 = Button (pro, text="x", command=kali)
tombol3.place (x=90, y=60)
tombol4 = Button (pro, text=":", command=bagi)
tombol4.place (x=130, y=60)

ending1 = Label (pro, text="Hasil:", font=("Arial 12 bold"))
ending1.place(x=10, y=100)

ending2 = Label (pro, text='')
ending2.place(x=60, y=100)





pro.mainloop()
