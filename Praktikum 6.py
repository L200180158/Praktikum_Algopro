Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ## Program identitas diri. dibuat oleh Sevtika L200180158
>>> Nama
'Sevtika Ichitia'
>>> Alamat
'Jln. Garuda Mas'
>>> Tgllahir
'12 september 2000'
>>> Prodi
'Informatika'
>>> Tempatlahir
'Cilegon'
>>> NIM
'L200180158'
>>> Fakultas
'Komunikasi dan informatika'
>>> Hoby
'ketawa'
>>> Tgljadian
'24-08-14'
>>> Namaadik
'Kirana, Kirani, Asih'
>>> #Program Akun
>>> ##dibuat oleh Sevtika L200180158
>>> nama
'sevtika ichitia'
>>> tgllahir
'12 september 2000'
>>> NIM
'L200180158'
>>> namasingkat
's.i'
>>> username
's12000'
>>> passward
'sev158'
>>> #Program Operator
>>> ##dibuat oleh Sevtika L200180158
>>> Nama = 'Sevtika Ichitia'
>>> NIM = 'L200180158'
>>> X = '1' + NIM[7:] # didalam string, digunakan angka 1 dengan slicing yang dimulai dari angka/huruf ke tujuh dari variabel NIM sampai selesai
>>> print (X) # menampilkan variabel X
1158
>>> a = int(X) # menampilkan string ke integer
>>> print(a) # menampilkan variabel a
1158
>>> b = len(Nama) # konversi string dalam variabel Nama ke dalam angka
>>> print(b) # menampilkan variabel b
15
>>> type(a) # menampilkan type data dari variabel a
<type 'int'>
>>> type(b) # menampilkan type data dari variabel b
<type 'int'>
>>> a / b # operasi pembagian antara bilangan dari variabel a dengan b. type data yang bisa untuk membagi bilangan hanya bila data tersebut bertype integer
77
>>> a // b # operasi pembagian antar bilangan dengan pembulatan kebawah. type data yang bisa untuk membagi bilangan hanya bila data bertype integer/ float
77
>>> 10 * (a - 999) # operasi perkalian ini dapat digunakan untuk mengalikan data dengan type integer maupun float.
1590
>>> b ** 2 # operasi ini digunakan untuk perpangkatan, type data yang dapat digunakan dalam operasi ini diantaranya integer dan float 
225
>>> a % b # operasi ini digunakan untuk memunculkan sisa hasil bagi
3
>>> c = 12.5 # variabel c berupa angka yang terdapat koma berarti type data pada variabel c yaitu float
>>> type(c) # menampilkan type data dari variabel c
<type 'float'>
>>> a / c # operasi pembagian antara bilangan dari variabel a dengan c, type data yang bisa untuk membagi bilangan hanya bila data tersebut bertype integer
92.64
>>> a // c # operasi pembagian antar bilangan dengan pembulatan ke bawah. type data yang bisa untuk membagi bilangan hanya bila data bertype integer/float
92.0
>>> a % c # operasi ini digunakan untuk memunculkan sisa hasil bagi
8.0
>>> c > b # operasi ini digunakan untuk menampilkan perbandingan lebih dari. type data ini adalah boolean
False
>>> type (c > b) # menampilkan type data dari (c > b)
<type 'bool'>
>>> a > b and b > c # pada data terdapat dua pernyataan 1158 > 15 dan 15 > 12.5
True
>>> a > 1100 or b < 10 # pada data terdapat dua pernyataan 1158 > 1100 atau 15 < 10
True
>>>#Program Tipe data
>>>##dibuat oleh Sevtika L200180158
>>> nama = 'sevtika ichitia'
>>> nim = 158
>>> tinggi = 1.58
>>> berat = 51
>>> tahunlahir = 2000
>>> aku = (tahunlahir, berat, tinggi, nim, nama) #sebuah tuple
>>> data = [tahunlahir, berat, tinggi, nim, nama] #sebuah tuple
>>> type(aku) #menampilkan type data variabel aku
<type 'tuple'>
>>> aku[0] #menampilkan eleman tuple indeks 0
2000
>>> a = nim % 4; aku[a] #nim 158 dibagi 4 sisa hasil bagi adalah 39.5 . lalu indeks dimasukkan kedalam variabel aku
1.58
>>> type(aku[a])#menampilkan type data dari eleman tuple indeks a
<type 'float'>
>>> aku[a:4]#slicing dimulai indeks ke 2 sampai indeks ke 3
(1.58, 158)
>>> type(aku[4]) #menampilkan type data dari eleman tuple indeks 4
<type 'str'>
>>> aku[0]='ok'#hasilnya ERROR karena eleman sebuah tuple tidak dapat diubah 

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    aku[0]='ok'
TypeError: 'tuple' object does not support item assignment
>>> type(data) #menampilkan type data dari variabel data 
<type 'list'>
>>> type(data[4]) #menampilkan type data dari eleman list 4
<type 'str'>
>>> data[4][5]#menampilkan list indeks 5 pada list 4
'k'
>>> data[4][a:6]#menampilkan list indeks 2 sampai 6 dari list 4
'vtik'
>>> data[0] = 'ok'; data#mengubah eleman list pada indeks 0 menjadi ok
['ok', 51, 1.58, 158, 'sevtika ichitia']
>>> data[-a]#menampilkan huruf atau angka terakhir pada indeks akhir ke 3 dari list
158
>>> range(a)#menampilkan semacam daftar atau koleksi dari indeks


