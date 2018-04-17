def kalkulator():
 def tambah
 print'1.Penjumlahan'
a=input('Masukkan nilai x=')
b=input('Masukkan nilai y=')
c=a+b
print'x=y=',c
print(' ')
tanya()


def kurang():
print'2.Pengurangan'
a=input('Masukkan nilai x=')
b=input('Masukkan nilai y=')
c=a-b
print'x-y=',c
print(' ')
tanya()

def kali():
print'3.Perkalian'
a=input('Masukkan nilai x=')
b=input('Masukkan nilai y=')
c=a*b
print'x.y=',c
print(' ')
tanya()

def bagi:
print'4.Pembagian'
a=input('Masukkan nilai x=')
b=input('Masukkan nilai y=')
c=a+b
print'x/y=',c
print(' ')
tanya()

def tanya():
choose=raw_input('Apakah anda ingin mengulang(Y/T)?')
if choose=='Y' or choose'y':
kalkulator()
elif choose=='T' or choose't':
print'Terimakasih Sudah Menggunakan Program Ini^_^'
else:
print'Maaf,input yang anda masukkan salah'
print'Silahkan masukkan Y atau T'
tanya()
print('Program kalkulator sederhana')
print('#############################')
print('1.Penjumlahan')
print('2.Pengurangan')
print('Perkalian')
print('Pembagian')
print('#############################')
print('silahkan pilih 1-4')
print(' ')

pil=raw_input('Masukkan Pilihan:')
if pil == '1':
tamba()
elif pil == '2':
kurang()
elif pil == '3':
kali()
elif pil == '4':
bagi()
else:
print('Maaf,input yang anda masukkan salah')
print('coba ulang lagi')
tanya()
kalkulator()
