import os
from user import User
from admin import Admin
dataUser = User()
dataAdmin = Admin()

def menu():
  while True:
    running = True
    print("Selamat Datang di Rencana Makanan")
    data = dataUser.login()
    if data[3] == 11111:
      while running:
        if len(dataUser.listMenu) != 0:
          dataUser.lihatMenu()
          os.system('pause')
          break
        else:
          print("=================================")
          print("Anda ingin makan apa hari ini?")
          dataUser.pilihMenu()
    elif data[3] == 22222:
      while running:
        print('Menu Admin : ')
        print('1. Daftar Makanan')
        print('2. Daftar User')
        print('0. Logout')
        pilih = int(input('Masukkan pilihan anda : '))
        if pilih == 1:
          dataAdmin.menu()
        elif pilih == 2:
          dataAdmin.hapusUser()
        elif pilih == 0:
          running = False 
menu()
