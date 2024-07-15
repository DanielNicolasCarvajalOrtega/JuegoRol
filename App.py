import os
from DataBase.DBConnection import Connection
from Clases import *
from Clases import Usuario
from DataBase.Razas.clasesRazas import Razas,Barbaro,GuerreroDivino,CazadorDeDemonios,Monje,Nigromante,Santero,Arcanista

while True:
    os.system("cls")
    dao = Connection()
    print("------------------  LOGIN  --------------------------")
    print("{'1'} - Crear usuario -  {'2'} - Iniciar sesion")
    opcion = input("Seleccione una opcion: ")


    if(opcion == "1"):
        print("\n INGRESE SUS DATOS \n")
        nombreUsuario = input("Ingrese su nombre completo: ")
        contrasenaUsuario = input("Ingrese una contraseña: ")
        User = Usuario(0,nombreUsuario,contrasenaUsuario)
        dao.Registro(User)
        

    elif(opcion == "2"):
        print("\n INGRESE SUS DATOS \n")
        nomUsuario = input("Ingrese su nombre de usuario: ")
        contraUsuario = input("Ingrese su contraseña: ")
        print("--------------------------------\n")
        print("PROCESO DE VERIFICACION\n")
        if dao.Verificacion(nomUsuario,contraUsuario):
            os.system("cls")
            while True:
                print(f"Bienvenido:") # PONER EL NOMBRE DEL USUARIO, DEL QUE INICIO SESION 
                print("--------------------------------\n")
                print("{'1'} Crear Personaje {'2'} Ver personajes {'3'} Ver perfil {'4'} salir" )
                opcion = input("Seleccione una opcion: ")
                if opcion == '1':
                    os.system("cls")
                    while True:
                        print("\n Sistema creacion de personaje \n")
                        print("--------------------------------\n")
                        print("Elije la raza de tu personaje\n")
                        print("1-[Barbaro]\n2-[Guerrero Divino]\n3-[Cazador de demonios]\n"
                            "4-[Monje]\n5-[Nigromante]\n6-[Santero]\n7-[Arcanista]\n")
                    
                        razaPersonaje = input("Seleccione una raza para tu personaje: \n")
                        if razaPersonaje == "1": # Barbaro
                            os.system("cls")
                            print("------ HAS ELEGIDO AL BARBARO ------\n")
                            print(Barbaro().obtenerBarbaro())
                            print("\n[1] PARA ELEGIR PERSONAJE\n[2] PARA SALIR")
                            opcion = input(" >>>>>   ")
                            if opcion == "1":
                                os.system("cls")
                                print(f"DALE UN NOMBRE A {Barbaro().getNombreBarbaro()}")
                                nomPersonaje = input('>>>>>> ')
                                barba = Barbaro(nomPersonaje)
                                

                            if opcion == "2": 
                                continue
                            else:
                                print("DEBES ELEGIR UNA OPCION")
                                continue
                        elif razaPersonaje == "2": # GuerreroDivino
                            os.system("cls")
                            print("------ HAS ELEGIDO AL GUERRERO DIVINO ------\n")
                            print(GuerreroDivino().obtenerGuerreroDivino())
                            print("\n[1] PARA ELEGIR PERSONAJE\n[2] PARA SALIR")
                            opcion = input(" >>>>>   ")
                            if opcion == "1":
                                os.system("cls")
            
                            if opcion == "2":
                                continue
                            else:
                                print("DEBES ELEGIR UNA OPCION")
                                continue

                        elif razaPersonaje == "3": # CazadorDeDemonios
                            os.system("cls")
                            print("------ HAS ELEGIDO AL CAZADOR DE DEMONIOS ------\n")
                            print(CazadorDeDemonios().obtenerCazadorDeDemonios())
                            print("\n[1] PARA ELEGIR PERSONAJE\n[2] PARA SALIR")
                            opcion = input(" >>>>>   ")
                            if opcion == "1":
                                os.system("cls")
                            if opcion == "2":
                                continue
                            else:
                                print("DEBES ELEGIR UNA OPCION")
                                continue
                            
                        elif razaPersonaje == "4": # Monje
                            os.system("cls")
                            print("------ HAS ELEGIDO AL MONJE ------\n")
                            print(Monje().obtenerMonje())
                            print("\n[1] PARA ELEGIR PERSONAJE\n[2] PARA SALIR")
                            opcion = input(" >>>>>   ")
                            if opcion == "1":
                                os.system("cls")
                            if opcion == "2":
                                continue
                            else:
                                print("DEBES ELEGIR UNA OPCION")
                                continue

                        elif razaPersonaje == "5": # Nigromante
                            os.system("cls")
                            print("------ HAS ELEGIDO AL NIGROMANTE ------\n")
                            print(Nigromante().obtenerNigromante())
                            print("\n[1] PARA ELEGIR PERSONAJE\n[2] PARA SALIR")
                            opcion = input(" >>>>>   ")
                            if opcion == "1":
                                os.system("cls")
                            if opcion == "2":
                                continue
                            else:
                                print("DEBES ELEGIR UNA OPCION")
                                continue

                        elif razaPersonaje == "6": # Sartero
                            os.system("cls")
                            print("------ HAS ELEGIDO AL SANTERO ------\n")
                            print(Santero().obtenerSantero())
                            print("\n[1] PARA ELEGIR PERSONAJE\n[2] PARA SALIR")
                            opcion = input(" >>>>>   ")
                            if opcion == "1":
                                os.system("cls")
                            if opcion == "2":
                                continue
                            else:
                                print("DEBES ELEGIR UNA OPCION")
                                continue
                        
                        elif razaPersonaje == "7": # Arcanista
                            os.system("cls")
                            print("------ HAS ELEGIDO AL ARCANISTA ------\n")
                            print(Arcanista().obtenerArcanista())
                            print("\n[1] PARA ELEGIR PERSONAJE\n[2] PARA SALIR")
                            opcion = input(" >>>>>   ")
                            if opcion == "1":
                                os.system("cls")
            
                            if opcion == "2":
                                continue
                            else:
                                print("DEBES ELEGIR UNA OPCION")
                                continue

                elif opcion == "2":
                    input("\n Tus personajes \n")
                    os.system("cls")
                    for per in dao.VerPersonajes():
                        print(f"")

                elif opcion == "3":
                    input("\n Perfil \n")
                    
                    pass

                elif opcion == "4":
                    pass
                    
        else:
            print("vuelve a intentarlo")
            continue
        

        



""" Agregar a Base de Datos en (HABILIDADES) y (PODERES) el estado (Desbloqueadas o Bloquedas)
"""