import random
print('''============> WELCOME <=============''')
print('''haloo selamat datang di minigames tebak perkalian 5
      silahkan masukan nama anda dibawah ini yaa brooo....''')
user = input('masukan nama anda abangkuhhh: ')
print(f'alooo dengan brooo {user} silahkan tebak dari perkalian 5 yoo')
perkalian = 5
tebakan = random.randint(1, 10)
hasil = int(perkalian) * int(tebakan)
print(f'5 dikali berapa bro hasilnya adalah {hasil} ???')


while True:
    menebak = int(input('masukan tebakan anda bro: '))
    if menebak == tebakan:
        print(f'mantappp jawaban bro {user} yaitu {menebak} benarrr boskuhhh!!!!!')
        break
    else:
        print('yahhh jawaban lu salah broo, yok jawab ulang')



