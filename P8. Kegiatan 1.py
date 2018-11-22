D = {'NIM':'L200180158','nama':'Sevtika Ichitia','alamat':'jln.Garuda Mas','prodi':'Informatika','fakultas':'FKI','hobi':'membaca','nampang':'ichi'}
print "pilihan yang tersedia:"
print "N menampilkan nama"
print "n menampilkan NIM"
print "l menampilkan alamat"
print "p menampilkan nampang"
print "t menampilkan prodi"
print "f menampilkan fakultas"
print "i menampilkan hobi"

def nama():
    "menampilkan nama"
    print 'nama:' + D['nama']
def NIM():
    "menampilkan NIM"
    print 'NIM:' + D['NIM']
def alamat():
    "menampilkan alamat"
    print 'alamat' + D['alamat']
def nampang():
    "menampilkan nampang"
    print 'nampang' + D['nampang']
def prodi():
    "menampilkan prodi"
    print 'prodi' + D['prodi']
def fakultas():
    "menampilkan fakultas"
    print 'fakultas' + D['fakultas']
def hobi():
    "menampilkan hobi"
    print 'hobi' + D['hobi']

repeat = True
while repeat :
    x = raw_input("pilihan saudara:")
    if x == "N":
        nama()
    elif x == "n":
        NIM()
    elif x == "l":
        alamat()
    elif x == "p":
        nampang()
    elif x == "t":
        prodi()
    elif x == "f":
        fakultas()
    elif x == "i":
        hobi()
    elif x == "k":
        print "Terima Kasih."
        repeat = False
        
