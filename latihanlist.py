# MMBUAT, MENGUBAH, MENAMBAH, DAN MENGGABUNGKAN ELEMEN LIST


a = [1, 2, 3, 4, 5]                                                 #buat list
print("a = [1, 2, 3, 4, 5]\n")

print(3*'=','akses',3*'=')                                               
print('elemen ke 3 adalah', a[2])                                   #tampilkan elemen ke 3  
del a[1:4]                                                          #ambil elemen ke 2 sampai 4
print('setelah elemen 2 sampai 4 diambil maka menjadi',a)           
del a[1]                                                            #ambil elemen terakhir
print('setelah elemen terakhir diambil maka menjadi',a,"\n")

print(3*'=','ubah',3*'=')
a = [1, 2, 3, 4, 5]
a [3] = 6                                                           #ubah elemen ke 4 dengan nilainya
print('setelah merubah elemen ke-4 maka menjadi', a)
a [3:5] = 7, 8                                                     #ubah elemen ke 4 sampai terakhir
print('setelah merubah elemen ke-4 sampai terakhir maka menjadi', a,'\n')

print(3*'=','tambah',3*'=')
a = [1, 2, 3, 4, 5]
b = []
b.extend (a[0:2])                                                   #ambil 2 bagian dari list 1(a) dan jadikan list 2(b)
print('hasil setelah mengambil 2 bagian elemen a maka b=', b)
b.append('tiga')                                                    #tambah list b dengan nilai string
print('setelah menambah string pada elemen b hasilnya', b)
b.extend([4, 5, 6])                                                 # tambah list b dengan 3 nilai
print('setelah menambah 3 nilai menjadi', b)
c=a+b                                                               #gabungkan list b dan list a
print('hasil penggabungan list a dan b hasilnya', c)









