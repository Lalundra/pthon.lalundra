def dosen_kece():
    print('berikut adalah profil beliau')
    print(30*'=')
    name = 'eddy'
    asal = 'jakarta'
    umur = 'masih muda'

    print(f'''profil beliau adalah\nnama = {name}\nasal = {asal}\numur = {umur}''')


nama = input('masukan nama eddy: ')
print(f'hallo dengan kak {nama} selamat datang')
print(30*'=')

if nama == 'eddy':
    print(f'pak {nama} dosen mengkecee')
    dosen_kece()
    print(30*'=')
else:
    print('dihh bukan lu yeee')
    
def kalkulator_pertambahan():
    print(50*'=')
    print('pertambahan readyy banhh!!!!!')
    angka_pertama = int(input('masukan angka pertama: '))
    angka_kedua = int(input('masukan angka kedua: '))
    hasil = angka_pertama + angka_kedua
    print('hasilnya adalah', float(hasil))
    

def kalkulator_perkalian():
    print(50*'=')
    print('perkalian readyy banhh!!!!!')
    angka_pertama = int(input('masukan angka pertama: '))
    angka_kedua = int(input('masukan angka kedua: '))
    print(50*'=')
    hasil = angka_pertama * angka_kedua
    print('hasilnya adalah', float(hasil))
    print(50*'=')

def kalkulator_pengurangan():
    print(50*'=')
    print('pengurangan readyy banhh!!!!!')
    angka_pertama = int(input('masukan angka pertama: '))
    angka_kedua = int(input('masukan angka kedua: '))
    print(50*'=')
    hasil = angka_pertama - angka_kedua
    print('hasilnya adalah', float(hasil))
    

def kalkulator_pembagian():
    print(50*'=')
    print('pembagian readyy banhh!!!!!')
    angka_pertama = int(input('masukan angka pertama: '))
    angka_kedua = int(input('masukan angka kedua: '))
    print(50*'=')
    hasil = angka_pertama / angka_kedua
    print('hasilnya adalah', float(hasil))
    

while True:
    print(f'hallo dengan pak {nama} apakah anda mau mencoba kalkulator manual?')
    jawab = int(input('pilih program yang anda mau\n1.perjumlahan\n2.pengurangan\n3.perkalian\n4.pembagian\n0.untuk keluar dari program\nsilahkan memilih: '))
    print(50*'=')
    if jawab == 1:
        kalkulator_pertambahan()
        print(50*'=')
    elif jawab == 2:
        kalkulator_pengurangan()
        print(50*'=')
    elif jawab == 3:
        kalkulator_perkalian()
        print(50*'=')
    elif jawab == 4:
        kalkulator_pembagian()
        print(50*'=')
    else:
        print('program keluar')
        break
    
    

