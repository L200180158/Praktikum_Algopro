#Menulis berkas teks
berkas = open ("L200180158.txt","w")
berkas.write("NIM=L200180158.\n")
berkas.write("TL=12-09-2000.\n")
berkas.write("Nama=Sevtika Ichitia.\n")
berkas.write("KotaLahir=Cilegon")
berkas.close()
x = open ("L200180158.txt","r")
NIM = x.readline()
TL = x.readline()
Nama = x.readline()
KotaLahir = x.readline()
print Nama
print KotaLahir, TL
print NIM

#Membaca data dari berkas teks dan menyimpan ke Shelve
import shelve
x = open ("L200180158.txt","r")
NIM = x.readline()
TL = x.readline()
Nama = x.readline()
KotaLahir = x.readline()
x.close()

x = shelve.open("ichi")
x['b'] = [NIM, TL, Nama, KotaLahir]
x.close()

#Membaca Shelve
x = shelve.open("ichi")
print x['b']
print x['b'][0]
print x['b'][1]
print x['b'][2]
