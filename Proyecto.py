import webbrowser
import time

urlBuy ='https://drive.google.com/file/d/1_GZjW-PdWYtrHbYXrKctI6NHowElm7_B/view?usp=sharing'
urlSell = 'https://drive.google.com/file/d/11UbTEXjYVNTn_IJlASCHX9D8R7L-IqIc/view?usp=sharing'

def PrintInterface():
    print("   ◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇")  ##Interfaz de usuario
    print("           ╔═══════════════════════════════════╗")        
    print("           |   Bienvenido a nuestro sistema    |")       
    print("           ╚═══════════════════════════════════╝")        
    print("   ◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇")     
    print(" __________________________________________________") 
    print("|             ┏━━━━━━━━━━━━━━━━━━┓                 |")
    print("|                     MENÚ                         |")
    print("|             ┗━━━━━━━━━━━━━━━━━━┛                 |")
    print("|    1) Comprar               2) Vender/Donar      |")
    print("|    3) Log-Out                                    |")
    print(" __________________________________________________") ##Interfaz de usuario
    print("")


def UserInput():
    PrintInterface()
    opt = input()
    
    if opt == str(1):
        webbrowser.open(urlBuy)
        time.sleep(2)
    elif opt == str(2):
        webbrowser.open(urlSell)
        time.sleep(2)
    elif opt == str(3):
        return
    else:
        print("\nOpción Inválida!!! Intente nuevamente ")
    
    UserInput()

import json
import os

def load_users():
    if not os.path.exists('users.json'):
        return {}
    try:
        with open('users.json') as file:
            users_data = json.load(file)
            return users_data
    except FileNotFoundError:
        return {}

def save_users(users_data):
    with open('users.json', 'w') as file:
        json.dump(users_data, file)

def register_user():
    username, password = AskForInfo()
    users = load_users()
    if username in users:
        print("\nEl usuario ya existe, por favor intente nuevamente.")
    else:
        users[username] = password
        save_users(users)
        print("\nUsuario registrado satisfactoriamente.")
        login(username, password)
        

def login(username, password):
    users = load_users()
    if username not in users or users[username] != password:
        print("\nUsuario o contraseña inválidos")
    else:
        print("\nLogin Exitoso")
        UserInput()

def AskForInfo():
    username = input("Introduzca su nombre de usuario: ")
    password = input("Introdduzca su contraseña:  ")
    return username, password
    
def PrintMainMenu():
	print("")
	print(" __________________________________________________") ##Interfaz de usuario
	print("|             ┏━━━━━━━━━━━━━━━━━━┓                 |")
	print("|                MENÚ PRINCIPAL                    |")
	print("|             ┗━━━━━━━━━━━━━━━━━━┛                 |")
	print("|    1) Registro               2) Log-In           |")
	print("|    3) Cerrar                                     |")
	print(" __________________________________________________") ##Interfaz de usuario
	print("")    

def main():
    if not os.path.exists('users.json'):
        with open('users.json', 'w') as file:
            file.write('{}')
    while True:
        PrintMainMenu()
        choice = input()
        if choice == str(1):
            register_user()
        elif choice == str(2):
            login(*AskForInfo())
        elif choice == str(3):
            break
        else:
            print("\nOpción Inválida!!! Intente nuevamente")

if __name__ == "__main__":
    main()
