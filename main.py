from replit import clear as cls
from time import sleep as slp
import sys
import base64

choice = input("[SYSTEM] Would you like to create (c) an account login (l)?\n> ")
cls()

choices = ["c", "l"]

if choice in choices:
  if choice == "c":
    taken = False
    valid = True
    print("[SYSTEM] Account creation detected")
    slp(0.1)
    cls()
    username = input("[SYSTEM] Please input an username\n> ")
    specialChar = ["`", "~", "!", "@", "#", "", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", "|", "\\", ":", ";", "'", "\"", ",", "<", ".", ">", "/", "?"]
    cls()
    for char in username:
      if char in specialChar:
        valid = False

    if valid == True:
      dataBase = open('data.txt', 'r')
      lines = dataBase.readlines()
  
      for line in lines:
        try:
          data = base64.b64decode(line)
          data = data.decode("ascii")
          if data.split(",")[0] == username:
            taken = True
        except:
          pass
  
      dataBase.close()
  
      if taken == False:     
        password = input("[SYSTEM] Please input an password\n> ")
        userData = f"{username},{password}"
        dataBytes = userData.encode("ascii")
        base64_bytes = base64.b64encode(dataBytes)
        base64_message = base64_bytes.decode('ascii')
        database = open("data.txt", "a")
        database.write(base64_message+"\n")
        database.close()
        cls()
        print(f"[SYSTEM] Account creation success! Username: {username}, Password: {password}")
      else:
        print("[SYSTEM] Username already taken")
    else:
      print("[SYSTEM] Username cannot have special characters")
  if choice == "l":
    valid = True
    login = False
    print("[SYSTEM] Account login detected")
    slp(0.1)
    cls()
    username = input("[SYSTEM] Please input an username\n> ")
    specialChar = ["`", "~", "!", "@", "#", "", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", "|", "\\", ":", ";", "'", "\"", ",", "<", ".", ">", "/", "?"]
    cls()
    for char in username:
      if char in specialChar:
        valid = False

    if valid == True:
      password = input("[SYSTEM] Please input an password\n> ")
      cls()
  
      dataBase = open('data.txt', 'r')
      lines = dataBase.readlines()
  
      for line in lines:
        try:
          data = base64.b64decode(line)
          data = data.decode("ascii")
          if data.split(",")[0] == username:
            if password == data.split(",")[1]:
              login = True
        except:
          pass
  
      dataBase.close()
      if login == True:
        print(f"[SYSTEM] Successfully logged in as {username}")
      else:
        print(f"[SYSTEM] Invalid username or password")
    else:
      print("[SYSTEM] Username cannot have special characters")
    
else:
  print("[SYSYTEM] Invalid selection")
