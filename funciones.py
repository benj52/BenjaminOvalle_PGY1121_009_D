import os
import time
import msvcrt
import numpy as np

teatro = np.zeros((10,10), int)

#acumuladores:
acum_entradas_vip = 0
acum_entradas_gold = 0
acum_entradas_silver = 0

#contadores
cont_entradas_vip = 0
cont_entradas_gold = 0
cont_entradas_silver = 0

#listas:
lista_ruts=[]
lista_filas=[]
lista_columnas=[]
lista_entradas=[]

#precios de las entradas:
precio_vip= 120000
precio_gold= 80000
precio_silver= 50000

def mostrar_teatro():
    print("       |     ESCENARIO      |")
    print("       |____________________|")
    for x in range(10):
        print("fila ",x+1, end=" ")
        for y in range(10):
            print(teatro[x][y], end=" ")
        print()
    print("        1 2 3 4 5 6 7 8 9 10")
    print("              COLUMNAS")

def mostrar_menu():
    print("""MENÚ TEATRO:
    1-COMPRAR ENTRADAS
    2-MOSTRAR UBICACIONES DISPONIBLES
    3-VER LISTADO DE ASISTENTES
    4-MOSTRAR GANANCIAS TOTALES
    5-SALIR""")

def mostrar_precios():
    print(f"""PRECIOS DE ENTRADAS:
    VIP = ${precio_vip} (asientos filas 1 y 2)
    GOLD = ${precio_gold} (asientos filas 3, 4 y 5)
    SILVER = ${precio_silver}(asientos filas 6, 7, 8, 9 y 10""")

def validar_opcion():
    while True:
        opcion= int(input("ingrese su opción: "))
        try:
            if opcion in(1,2,3,4,5):
                return opcion
            else:
                print("ERROR! opción inválida!")
                time.sleep(1)
                os.system("cls")
        except:
            print("ERROR! ingrese un número entero")
            time.sleep(1)
            os.system("cls")

def validar_entradas():
    while True:
        entradas= int(input("ingrese cantidad entradas(solo se permite 3 entradas por compra): "))
        try:
            if entradas >= 1 and entradas <=3:
                return entradas
            else:
                print("ERROR! NO PUEDE COMPRAR ESTA CANTIDAD DE ENTRADAS!")
                time.sleep(1)
                os.system("cls")
        except:
            print(" ERROR! INGRESE UN NÚMERO ENTERO! ")
            time.sleep(1)
            os.system("cls")

def validar_rut():
    while True:
        rut= int(input("ingrese el rut: "))
        try: 
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! rut inválido")
             
        except:
            print("ERROR! ingrese un número entero!")

def validar_nombre():
    while True:
        nombre= input("ingrese el nombre")
        if len(nombre.strip()) >=3 and nombre.isalpha(): 
            return nombre
        else:
            print("ERROR! NOMBRE INVÁLIDO")    

def validar_apellido():
    while True:
        apellido= input("ingrese el apellido")
        if len(apellido.strip()) >=3 and apellido.isalpha(): 
            return apellido
        else:
            print("ERROR! APELLIDO INVÁLIDO")

def validar_fila():
    while True:
        fila= int(input("ingrese la fila deseada"))
        try:
            if fila in(1,2,3,4,5,6,7,8,9,10):
                return fila
            else:
                print("FILA INVÁLIDA!!")
                time.sleep(1)
                os.system("cls")
        except:
            print("ERROR! INGRESE UN NÚMRO ENTERO! ")
            time.sleep(1)
            os.system("cls")

def validar_columna():
    while True:
        columna= int(input("ingrese la columna deseada"))
        try:
            if columna in(1,2,3,4,5,6,7,8,9,10):
                return columna
            else:
                print("COLUMNA INVÁLIDA!!")
                time.sleep(1)
                os.system("cls")
        except:
            print("ERROR! INGRESE UN NÚMERO ENTERO! ")
            time.sleep(1)
            os.system("cls")


#opción 1: comprar entradas
def comprar_entradas():
    if "x"  in teatro:
        print("NO HAY ASIENTOS DISPONIBLES😢, LO SIENTO!")
    
    entradas= validar_entradas()
    
    for x in range(entradas):
        
        mostrar_teatro()
        mostrar_precios()
        print(f"ingrese el rut y las coordenadas del asiento de la persona {x+1}: ")
        rut = validar_rut()
        fila= validar_fila()
        columna= validar_columna()
        if teatro[fila-1][columna-1] == 0:
            if fila >=1 and fila <=2:
                teatro[fila-1][columna-1]==1
                cont_entradas_vip =+ 1
                acum_entradas_vip =+ precio_vip
                lista_ruts.append(rut)
                lista_filas.append(fila-1)
                lista_columnas.append(columna-1)
                print("asiento tipo VIP")               
            elif fila >=3 and fila <=5:
                teatro[fila-1][columna-1]==1
                cont_entradas_gold =+  1
                acum_entradas_gold =+ precio_gold
                lista_ruts.append(rut)
                lista_filas.append(fila-1)
                lista_columnas.append(columna-1)
                print("asiento tipo GOLD")
            elif fila >=6 and fila <=10:
                teatro[fila-1][columna-1]==1
                cont_entradas_silver =+ +  1
                acum_entradas_silver =+ precio_silver
                lista_ruts.append(rut)
                lista_filas.append(fila-1)
                lista_columnas.append(columna-1)  
                print("asiento tipo SILVER")
        else:
            print("el asiento escogido no está disponible")
            time.sleep(1)
            os.system("cls")  
    print("OPERACION REALIZADA CON ÉXITO, UN ASISTENTE LO VA GUIAR A SU ASIENTO, GRACIAS POR SU COMPRA!")
    time.sleep(1.5)
    os.system("cls")
    return


#opción 2: ver ubicaciones disponibles
def mostrar_ubicaciones_disponibles():
    os.system("cls")
    mostrar_teatro()
    print("los asientos disponibles son los que están con 0")
    print("los asientos que no están disponibles son representados por un 1")
    print("")
    print("precione una tecla para volver al menú...")
    msvcrt.getch()
    os.system("cls")

#opcion 3: ver listado de asistentes

def lista_asistentes():
    print("LISTA DE ASISTENTES POR RUT:")
    for x in range(lista_ruts.sort()):
        print(lista_ruts(x),end="\n")
    print("presione una tecla para volver al menú...")
    msvcrt.getch()
    os.system("cls")

#opcion 4: total ganancias

def total_ganancias():
    cantidad_total = cont_entradas_gold + cont_entradas_silver + cont_entradas_vip
    total= acum_entradas_gold+ acum_entradas_silver + acum_entradas_vip
    print(F"""    tipo entrada   cantidad   total 
    VIP    ${precio_vip} | {cont_entradas_vip} | {acum_entradas_vip}
    ----------------------------------------------------------------
    GOLD   ${precio_gold} | {cont_entradas_gold} | {acum_entradas_gold}
    ----------------------------------------------------------------
    SILVER ${precio_silver} | {cont_entradas_silver} | {acum_entradas_silver}
    ________________________________________________________________
    TOTAL                | {cantidad_total} | {total}   """)
    print("")
    print("presione un tecla para volver al menú...")
    msvcrt.getch()
    os.system("cls")


#opcion 5: salir
def salir():
   print(" NOMBRE= BENJAMIN OVALLE")
   print(" FECHA: 06/07/2023")
