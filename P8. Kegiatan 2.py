x = int(input('masukkan angka suhu: '))
y = str(input('jenis suhunya: '))

cel = ['Celcius', 'celcius', 'C']
fah = ['Fahtenheit', 'F', 'farenheit']

if y in cel:
    ub =  str(input ('ingin mengubah ke bentuk fahrenheit? '))
    uby = ['Ya', 'ya']
    if ub in uby:
        d = x + 32
        print('suhunya adalah', d, 'Fahrenheit')
    else :
        print('suhunya adalah', x, 'Celcius')
else:
    ug = str(input('ingin mengubah ke bentuk celcius? '))
    ugy = ['Ya', 'ya']
    if ug in ugy:
        g = x - 32
        print('suhunya adalah', g, 'Celcius')
    else:
        print('suhunya adalah', x, 'Fahrenheit')
