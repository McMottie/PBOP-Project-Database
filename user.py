from query import Query

database = Query()
database.connection('localhost', 'root', '', '5220411458')

class User:
    def __init__(self):
        self.id = None
        self.username = None
        self.__password = None
        self.listMenu = []
        
    def login(self):
      username = str(input("Username : "))
      password = str(input("Password : "))
      data = database.login(username, password)
      return data
      
    def pilihMenu(self):
      menuBreakfast = database.menuBreakfast()
      print("=================================")
      print("=========== BREAKFAST ===========")
      for i in menuBreakfast:
        print(f'{i[1]} [{i[0]}]')
      breakfast = int(input("Masukkan ID Menu Breakfast : "))
      data = database.pilihMenu(breakfast)
      self.listMenu.append(data)
        
      menuLunch = database.menuLunch()
      print("=================================")
      print("============= LUNCH =============")
      for i in menuLunch:
        print(f'{i[1]} [{i[0]}]')
        # print(f'{i[2]}, {i[3]}, {i[4]}')
      lunch = int(input("Masukkan ID Menu Lunch : "))
      data = database.pilihMenu(lunch)
      self.listMenu.append(data)
      
      menuDinner = database.menuDinner()
      print("=================================")
      print("============ DINNER =============")
      for i in menuDinner:
        print(f'{i[1]} [{i[0]}]')
      dinner = int(input("Masukkan ID Menu Dinner : "))
      data = database.pilihMenu(dinner)
      self.listMenu.append(data)
      
    def lihatMenu(self):
      print('\n  _________________________________')
      print('| DAFTAR MENU YANG ANDA PILIH     ')
      print(f'| Breakfast (Sarapan) : {self.listMenu[0][1]}          ')
      print(f'| Karbohidrat : {self.listMenu[0][2]}                  ')
      print(f'| Protein : {self.listMenu[0][3]}                      ')
      print(f'| Lemak : {self.listMenu[0][4]}                        ')
      print(f' _________________________________')
      print(f'| Lunch (Makan Siang) : {self.listMenu[1][1]}          ')
      print(f'| Karbohidrat : {self.listMenu[1][2]}                  ')
      print(f'| Protein : {self.listMenu[1][3]}                      ')
      print(f'| Lemak : {self.listMenu[1][4]}                        ')
      print(f' _________________________________')
      print(f'| Dinner (Makan Malam) : {self.listMenu[2][1]}         ')
      print(f'| Karbohidrat : {self.listMenu[2][2]}                  ')
      print(f'| Protein : {self.listMenu[2][3]}                      ')
      print(f'| Lemak : {self.listMenu[2][4]}                        ')
      print(f' _________________________________')
      
