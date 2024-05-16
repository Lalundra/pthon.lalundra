#perbandingan >,<,>=,==,!=, is, isnot


#salah
x = 3
y = 4
hasil = y < x
print(f'{x} lebih besar dari {y} itu adalah', hasil)



#is not
x = 3
hasil = x is not  6
print(x, 'is not', 6, '=', hasil)



#benar
x = 4
y = 3
hasil = x > y
print(f'{x} lebih besar dari {y} itu adalah', hasil)

#besar sama dengan
x = 10
pengguna = int(input('masukan nilai: '))
if pengguna >= x:
     print('TRUE')
else:
     print('FALSE')


# sama dengan (==)
x = 15
hasil = x == int(15)
print( x, '==','15',hasil)

#tidak sama (==)
hasil = x == int(10)
print( x, '==', 10 , hasil)

#!=
x = 10
hasil = x != int(15)
print(x, '!=', 15, hasil )
