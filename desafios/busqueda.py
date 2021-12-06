import sys
ventas = {
    'Enero':15000, 
    'Febrero': 22000, 
    'Marzo': 12000, 
    'Abril':17000, 
    'Mayo':81000, 
    'Junio':13000, 
    'Julio':21000, 
    'Agosto':41200, 
    'Septiembre': 25000, 
    "Octubre":21500, 
    "Noviembre": 91000, 
    "Diciembre": 21000
    }

lista_busqueda = (sys.argv[1:])
lista_busqueda = [int(numero) for numero in lista_busqueda]
ventas_inv = {value:key for (key, value) in ventas.items()}


for busqueda in lista_busqueda:
    if busqueda in ventas_inv:
        print(ventas_inv[busqueda])
    else:
        print("no encontrado")