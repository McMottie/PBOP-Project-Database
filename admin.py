from user import User, database

class Admin(User):
  def __init__(self):
    super().__init__()
    
  def inputMenu(self):
    idMenu = int(input('Id Menu : '))
    namaMenu = str(input("Nama Menu : "))
    karbo  = int(input('Jumlah Karbohidrat : '))
    protein  = int(input('Jumlah Protein : '))
    lemak  = int(input('Jumlah Lemak : '))
    kategori = str(input('Kategori Menu : '))
    return [idMenu, namaMenu, karbo, protein, lemak, kategori]
    
  def ubahMenu(self): 
    karbo  = int(input('Jumlah Karbohidrat : '))
    protein  = int(input('Jumlah Protein : '))
    lemak  = int(input('Jumlah Lemak : '))
    return [karbo, protein, lemak]
    
    
  def menu(self):
    data = database.menu()
    print('=====================================')
    for menu in data:
      print(f'{menu[1]} [{menu[0]}]')
    print('=====================================')
    print('1. Tambah Menu')
    print('2. Ubah Menu')
    pilihan = int(input('Masukkan pilihan anda : '))
    if pilihan == 1:
      database.tambahMenu(self.inputMenu())
    if pilihan == 2:
      id = int(input('Masukkan Id menu yang ingin diubah : '))
      database.ubahMenu(id, self.ubahMenu())
    
  def hapusUser(self):
    user = database.dataUser()
    print('=====================================')
    for i in user:
      print(f'{i[1]} [{i[0]}]')
    print('=====================================')
    id = int(input('Masukkan Id yang ingin dihapus : '))
    database.hapusUser(id)
      