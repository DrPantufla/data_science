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


lista_q1 = [ventas[key] for key in ventas if key in ['Enero', 'Febrero', 'Marzo']]
lista_q2 = [ventas[key] for key in ventas if key in ['Abril', 'Mayo', 'Junio']]
lista_q3 = [ventas[key] for key in ventas if key in ['Julio', 'Agosto', 'Septiembre']]
lista_q4 = [ventas[key] for key in ventas if key in ['Octubre', 'Noviembre', 'Diciembre']]

quarters = {'Q1':lista_q1, 'Q2':lista_q2, 'Q3':lista_q3, 'Q4':lista_q4} 
   

print(quarters)

