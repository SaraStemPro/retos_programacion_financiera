cantidad = input('Escribe la cantidad a invertir: ')
while not isinstance (cantidad, (int,float)):
    try:
        cantidad = float(cantidad)
    except ValueError:
        print('La cantidad debe ser un número')
        cantidad = input('Escribe la cantidad a invertir: ')

interes = float(input('Escribe el tipo de interés: '))
años = int(input('Escribe el número de años: '))

print('capital final: '+ str(round(cantidad*(1+(interes/100))**años,2)))

# Solución con una función (aportada por Gsnchz)

def Inversion(I, n, r): 
    for i in range(1,n+1): 
        print("Año " + str(i) + " " + str(round(I*(1+r/100)**i, 2))) 

Inversion(100000, 10, 5)

