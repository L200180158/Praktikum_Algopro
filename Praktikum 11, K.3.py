from Tkinter import *
pro = Tk (className = ' Ichi Ocha')
pro.geometry('500x250')

##(s*s) ##Rumus Luas Permukaan Persegi

def jumlah ():
    s=float(kolom1.get())
    hasil=(s*s)
    ending2.config (text="Luas = {}".format(hasil), font=('Arial 12 bold'))

judul = Label (pro, text="Bangun Geometri", font=('Arial 27 bold'))
judul.place(x=10, y=0)

label1 = Label (pro, text="Menghitung Luas Permukaan Persegi", font=('Arial 12 bold'))
label1.place(x=10, y=50)
label2 = Label (pro, text="Rumus: (s*s) ", font=('Arial 12 bold'))
label2.place(x=10, y=75)

data2 = Label (pro, text="Parameter Sisi:")
data2.place(x=10, y=110)
kolom1= Entry (pro)
kolom1.place(x=120, y=110)


tombol1 = Button (pro, text="Hitung Luas Permukaan", command=jumlah)
tombol1.place (x=10, y=180)

ending2 = Label (pro, text='')
ending2.place(x=160, y=180)

pro.mainloop()
