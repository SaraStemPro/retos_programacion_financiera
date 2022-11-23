p_fresco = int(input('Escribe los kg de pescado fresco: '))
p_nofresco = int(input('Escribe los kg de pescado no fresco: '))
precio_fresco = 4.3
dto_nofresco = 0.6
precio_nofresco = precio_fresco*(1-dto_nofresco)
coste_total = p_fresco*precio_fresco+p_nofresco*precio_nofresco
print('El coste total a pagar es: ', round(coste_total, 2))

# Plus: Hazlo con una función
precio_fresco = 4.3
dto_nofresco = 0.6

def coste_pescado(p_fresco, p_nofresco):
    coste_total = round(p_fresco*precio_fresco + \
        p_nofresco*(precio_fresco*(1-dto_nofresco)),2)
    return coste_total
print('El coste del pescado es:',str(coste_pescado(4,1))+'€')


