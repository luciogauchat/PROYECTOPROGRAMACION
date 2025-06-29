lista_ingresos = [] 
lista_egresos = []
print("------Bienvenido al Sistema Simple Contable SSC------")
from bilbioteca import menu_opciones, cargar_ingreso, cargar_egreso, enlistar_egresos, enlistar_ingresos, balance, porcentaje_ingreso_egreso, mov_mayor
menu_opciones()
while True: 
    try:
        opcion= int(input("Escribe solo el número correspondiente (del 1 al 7):"))
        
    except ValueError:   
        print("Error, por favor solo ingrese números válidos de 1 al 7.")
    if opcion == 1:
            cargar_ingreso()
    elif opcion == 2:
            cargar_egreso()
    elif opcion == 3:
            print(f"Lista de Ingresos: {enlistar_ingresos()}")
            print(f"Lista de Egresos:{enlistar_egresos()}")
    elif opcion == 4:
            print(f"El Balance total es de: ${balance()}")
    elif opcion == 5:
            porcentaje_ingreso_egreso()
    elif opcion == 6:
            mov_mayor()
    if opcion == 7: 
        print(f"------Gracias por utilizar el Sistema Simple Contable SSC------")
        break

  
        

  







