import random
import datetime
from customer import Customer

atm = Customer(id)
while True:
    
    id = int(input('Masukkan pin anda: '))
    trial = 0
    
    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input('Pin anda salah. Silahkan masukkan lagi: '))
        
        trial += 1
        
        if trial == 3:
            print('Error.Silahkan ambil kartu dan coba lagi..')
            exit()
    
    while True:
        print('Selamat datang di ATM Progate..')
        print('\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - keluar')
        
        selectmenu = int(input('\nSilahkan Pilih Menu: '))

        if selectmenu == 1:
            print('\n Saldo anda sekarang: Rp. ' + str(atm.checkBalance()) + '\n')
            
        elif selectmenu == 2:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_withdraw = input('Konfirmasi: Anda akan mealkukan debet dengan nominal berikut ? y/n ' + str(nominal) + ' ')
            if verify_withdraw == 'y':
                print('Saldo awal anda adalah ' + str(atm.checkBalance()) + ' ')
            else:
                print('Maaf saldo anda tidak cukup untuk melakukan debet!')
                print('Silahkan lakukan penambahan nominal saldo')

        elif selectmenu == 3:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_deposit = input('Konfirmasi: Anda akan mealkukan penyimpanan dengan nominal berikut ? y/n ' + str(nominal) + ' ')
            if verify_deposit == 'y':
                atm.depositBalance(nominal)
                print('Saldo anda sekarang adalah: Rp.' + str(atm.checkBalance()) + '\n')
            else:
                break
            
        elif selectmenu == 4:
            verify_pin = int(input('Masukkan pin anda: '))

            while verify_pin != int(atm.checkPin()):
                print('Pin anda salah silahkan masukkan pin: ')

            updated_pin = int(input('Silahkan masukkan pin baru: '))
            print('pin anda berhasil diganti')

            verify_newpin = int(input('Coba masukkan pin baru: '))

            if verify_newpin == updated_pin:
                print('pin baru anda sukses')
            else:
                print('Maaf pin anda salah! ')

        elif selectmenu == 5:
            print('Resi tercetak otomatis saat anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.')
            print('No. Rekord: ', random.randint(100000, 1000000))
            print('Tanggal: ', datetime.datetime.now())
            print('Saldo akhir: ', atm.checkBalance())
            print('Terima kasih telah menggunakan ATM Progate! ')
            exit()
        else:
            print('Error. Maaf, menu tidak tersedia')


