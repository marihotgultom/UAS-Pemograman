i=0
nama=[]
nim=[]
tugas=[]
uts=[]
uas=[]
total=[]

while True:
    s_nama=raw_input('\nNama          : ')
    nama.append(s_nama)
    s_nim=raw_input('NIM           : ')
    nim.append(s_nim)
    i_tugas=input('Nilai Tugas   : ')
    tugas.append(i_tugas)
    i_uts=input('Nilai UTS     : ')
    uts.append(i_uts)
    i_uas=input('Nilai UAS     : ')
    uas.append(i_uas)

    rata=(i_tugas+i_uts+i_uas)/3
    total.append(rata)

    tambah=''
    while tambah!='y' and tambah!='t':
        tambah=raw_input('\nTambah Data [y/t] : ')
    i+=1
    if tambah=='t':
        break

print '\n                   Daftar Mahasiswa'
print '========================================================='
print '| No |    Nama    |    NIM    |Tugas| UTS | UAS | Akhir |'
print '========================================================='
for n in range(i):
    #print ' ',n+1,'|\t',nama[n],'   |   ',nim[n],'   |   ',tugas[n],'   |   ',uts[n],'   |   ',uas[n],'    |    ',total[n], '   |'
    #print '| %-2d | %-10s | %-10s | %-2d | %-2d | %-2d | %-4f' % (n, nama[n], nim[n], tugas[n], uts[n], uas[n], rata[n])
    print '| {n:2d} | {nama:10s} | {nim:9s} | {tugas:3d} | {uts:3d} | {uas:3d} | {total:5.2f} |'.format(nama=nama[n], n=n+1, nim=nim[n], tugas=tugas[n], uts=uts[n], uas=uas[n], total=total[n])
print '========================================================='
