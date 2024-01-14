import mysql.connector

class Query():
    def __init__(self):
      self.host = None
      self.user = None
      self.password = None
      self.database = None
      self.connect = None
      self.cursor = None
    
    def connection(self, host, user, password, database):
      self.host = host
      self.user = user
      self.password = password
      self.database = database
      self.connect = mysql.connector.connect(host = host, user = user, passwd = password, database = database)
      self.cursor = self.connect.cursor()
      return True

    def login(self, username, password):
      self.cursor.execute(f'SELECT * FROM user WHERE username="{username}" and password="{password}"')
      return self.cursor.fetchone()
      
    def menu(self):
      self.cursor.execute(f"SELECT * FROM menu")
      return self.cursor.fetchall()
    def menuBreakfast(self):
      self.cursor.execute(f"SELECT * FROM menu WHERE kategori = 'breakfast' ")
      return self.cursor.fetchall()
    def menuLunch(self):
      self.cursor.execute(f"SELECT * FROM menu WHERE kategori = 'lunch' ")
      return self.cursor.fetchall()
    def menuDinner(self):
      self.cursor.execute(f"SELECT * FROM menu WHERE kategori = 'dinner' ")
      return self.cursor.fetchall()
    
    def pilihMenu(self, id):
      self.cursor.execute (f'SELECT * FROM menu WHERE id = "{id}" ' )
      return self.cursor.fetchone()
    
    def tambahMenu(self, data):
      self.cursor.execute(f"INSERT INTO menu (id, makanan, karbohidrat, protein, lemak, kategori) VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}')")
      self.connect.commit()
    
    def ubahMenu(self, id, data):
      self.cursor.execute(f"UPDATE menu SET karbohidrat='{data[0]}', protein='{data[1]}', lemak='{data[2]}' WHERE id='{id}'")
      self.connect.commit()
      
    def dataUser(self):
      self.cursor.execute(f'SELECT * FROM user')
      return self.cursor.fetchall()
    
    def hapusUser(self, id):
      self.cursor.execute(f'DELETE FROM user WHERE id="{id}"')
      self.connect.commit()