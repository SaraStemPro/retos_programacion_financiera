precios = {
    'Manzana': 0.7,
    'Plátano': 1.2,
    'Kiwi': 2.3,
    'Fresa': 0.55,
}

fruta = input('¿Fruta? ')

def precio_total(kg):
    precio = kg*precios[fruta]
    return precio

while fruta not in precios.keys():
    for i in precios.keys():
        if fruta[1:] == i[1:]:
            fruta = fruta.capitalize()
            break
    else:
        print('Esa fruta no está en nuestro catálogo')
        fruta = input('Indica otra fruta ')

kilos = int(input('¿Kilos? '))
print(f'A pagar {round(precio_total(kilos),2)}')




