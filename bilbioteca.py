lista_ingresos = [] 
lista_egresos = []
def menu_opciones():
    print("---------------------------------------------------")
    print("Seleccione un número según lo que desée realizar")
    print("1) para cargar un Ingreso (con un máximo de 20 ingresos)")
    print("2) para cargar un Egreso (con un máximo de 20 egresos)")
    print("3) para ver todos los movimientos")
    print("4) para calcular el Balance total")
    print("5) para ver el porcentaje de ingresos y egresos")
    print("6) para ver el movimiento de mayor monto")
    print("7) para salir")
    print("---------------------------------------------------")
 
def cargar_ingreso():
    global lista_ingresos
    while True:
        usuario_ingreso = input(f"A continuación cargue el ingreso número {len(lista_ingresos) + 1} o escriba 'fin'(sin comillas) para terminar: ").strip()
        if usuario_ingreso.lower() == "fin":
            break
        try:
            monto_ingreso = float(usuario_ingreso)
            if monto_ingreso < 0:
                print("El monto ingresado no puede ser negativo, vuelva a intentar")
                continue
            lista_ingresos.append(monto_ingreso)
            if len(lista_ingresos) >= 20:
                print("alcanzo el límite de ingresos!")
                break
        except ValueError:
            print("Entrada inválida, ingrese solo números o escriba 'fin' sin comillas para volver al menu")


def cargar_egreso():
    global lista_egresos
    while True:
        usuario_egreso = input(f"Cargue el egreso número {len(lista_egresos) + 1 } o escriba 'fin'(sin comillas) para terminar: ").strip()
        if usuario_egreso.lower() == "fin":
            break
        try:
             monto_egreso = float(usuario_egreso)
             if monto_egreso < 0:
                print("El monto ingresado no puede ser negativo, vuelva a intentar")
                continue
             lista_egresos.append(monto_egreso)
             if len(lista_egresos) >= 20:
                 print("Límite de Egresos superado")
                 break   
        except ValueError:
            print("Entrada inválida, ingrese solo números o escriba 'fin' sin comillas para volver al menu")


def enlistar_ingresos():
     global lista_ingresos
     ingresos_a_mostrar = lista_ingresos
     for numero_ingreso, monto_ingreso in enumerate(ingresos_a_mostrar, start=1):
         print(f"Ingreso n* {numero_ingreso}: ${monto_ingreso}")


def enlistar_egresos():
     global lista_egresos
     egresos_a_mostrar = lista_egresos
     for numero_egreso, monto_egreso in enumerate(egresos_a_mostrar,start=1):
         print(f"Egreso n* {numero_egreso}: ${monto_egreso}")     


def balance():
    global lista_ingresos, lista_egresos
    suma_total_ingresos = sum(lista_ingresos)
    suma_total_egresos = sum(lista_egresos)
    balance_total = suma_total_ingresos - suma_total_egresos
    return balance_total


def porcentaje_ingreso_egreso():
     global lista_ingresos, lista_egresos
     suma_total_ingresos = sum(lista_ingresos) 
     suma_total_egresos = sum(lista_egresos)
     total_movimientos = suma_total_egresos + suma_total_ingresos
     porcentaje_ingreso = (suma_total_ingresos / total_movimientos) * 100
     porcentaje_egreso = (suma_total_egresos / total_movimientos) * 100
     print(f"El total de ingresos es de: ${suma_total_ingresos}")
     print(f"El total de egresos es de: ${suma_total_egresos}")
     print(f"El total de movimientos es de:{total_movimientos}")
     print(f"El Porcentaje de Ingresos sobre el total es de: {porcentaje_ingreso} %")
     print(f"El Porcentaje de Egresos sobre el total es de: {porcentaje_egreso} %")



def mov_mayor():
     global lista_egresos, lista_ingresos
     total_movimientos = lista_egresos + lista_ingresos
     monto_maximo = max(total_movimientos)
     print(f"El monto de movimiento más alto registrado es: ${monto_maximo}")
     return monto_maximo


    