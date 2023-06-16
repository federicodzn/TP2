FD = "peaje25.txt"

# Consigna 1
def idioma_esp_por(linea):
    if "PT" in linea:
        idioma = "Portugués"
    else:
        idioma = "Español"

    return idioma

# Consigna 2
def veh_proc(patente):
    carg, cbol, cbra, cchi, cpar, curu, cotr = 0, 0, 0, 0, 0, 0, 0
    
    if len(patente) == 7:
        if patente[:2].isalpha() and patente[2:5].isdigit() and patente[5:].isalpha():
            carg = 1
        elif patente[:3].isalpha() and patente[3:].isdigit():
            curu = 1
        elif patente[:2].isalpha() and patente[2:].isdigit():
            cbol = 1
        elif patente[:4].isalpha() and patente[4:].isdigit():
            cpar = 1
        elif patente[:3].isalpha() and patente[3:4].isdigit() and patente[4:5].isalpha() and patente[5:].isdigit():
            cbra = 1
        elif patente[0:1] == " " and patente[1:5].isalpha() and patente[5:].isdigit():
            cchi = 1
        else:
            cotr = 1
            
    return carg, cbol, cbra, cchi, cpar, curu, cotr

# Consigna 3
def imp_tot(pais, tipo, pago):
    importe_final = 0
    # Pais de la cabina de peaje
    if pais == 2:
        importe_base = 400
    elif pais == 1:
        importe_base = 200
    else:
        importe_base = 300
    # Tipo de vehiculo
    if tipo == 0:
        importe_base *= 0.5
    elif tipo == 2:
        importe_base *= 1.6

    # Aplicación del descuento por telepeaje
    if pago == 2:
        importe_final = int(importe_base * 0.9)
    else:
        importe_final = int(importe_base)

    return importe_final

# Consigna 4
def cant_patente(patente_primera, patente):
    cpp = 0
    if patente == patente_primera:
        cpp += 1
    
    return cpp
        

# Consigna 5
def may_import(mayimp, imp_final):
    
    if mayimp == 0 or mayimp < imp_final:
        mayimp = imp_final

    return mayimp

# Consigna 6
def porcentaje(otro_pais, total):

    porc = round((otro_pais * 100) / total, 2)

    return porc

# Consigna 7
def dist_prom(patente, distancia):
    carg = 0
    distancia = int(linea[10:13])
    if patente == carg:
        carg += 1
        distancia += 1

    '''if pais == 2:
        carg += 1
        km_recorridos = kmacabina'''
    return carg, distancia

# Programa principal
def test():
    # Aqui se muestran los resultados y prints del script

    # Se abre el archivo
    arch = open(FD, "r")
    linea = arch.readline()

    # Punto 1
    idioma = idioma_esp_por(linea)

    # Punto 2
    linea = arch.readline() # Leemos de la segunda linea para adelante
    primera_patente = linea[0:7]
    carg, cbol, cbra, cchi, cpar, curu, cotr = 0, 0, 0, 0, 0, 0, 0
    imp_acu_total = 0 
    primera = None
    cpp = 0
    mayimp = 0
    maypat = ""
    bandera = False
    cont_total_pant = 0
    cont_otro_pais = 0


    while linea != "":
        patente = linea[0:7]
        resultado = veh_proc(patente)
        carg += resultado[0]
        cbol += resultado[1]
        cbra += resultado[2]
        cchi += resultado[3]
        cpar += resultado[4]
        curu += resultado[5]
        cotr += resultado[6]
        
    # Punto 3   
        tipo = int(linea[7])
        forma_pago = int(linea[8])
        pais = int(linea[9])
        imp_final = imp_tot(pais, tipo, forma_pago)
        imp_acu_total += imp_final

        if bandera and imp_final > mayimp:
            bandera = False
        
    # Punto 4
        primera = primera_patente[0:7]
        resultado2 = cant_patente(primera, patente)
        cpp += int(resultado2)
        
    # Punto 5
        mayimp = may_import(mayimp, imp_final)

        if mayimp == imp_final and not bandera:
            bandera = True
            maypat = patente

    # Punto 6
        cont_total_pant += 1
        
        if cotr != 0:
            porc = porcentaje(cotr, cont_total_pant)
        
    # Punto 7
        distancia = int(linea[10:13])
        prom = distancia/carg



        linea = arch.readline() # Leemos la siguiente linea hasta el final

    # Se cierra el archivo
    arch.close()

    # Visualizacion de resultados...
    print('(r1) - Idioma a usar en los informes: ', idioma)

    print()
    print('(r2) - Cantidad de patentes de Argentina:', carg)
    print('(r2) - Cantidad de patentes de Bolivia:', cbol)
    print('(r2) - Cantidad de patentes de Brasil:', cbra)
    print('(r2) - Cantidad de patentes de Chile:', cchi)
    print('(r2) - Cantidad de patentes de Paraguay:', cpar)
    print('(r2) - Cantidad de patentes de Uruguay:', curu)
    print('(r2) - Cantidad de patentes de otro pais:', cotr)

    print()
    print('(r3) - Importe acumulado total de importes finales: ', imp_acu_total)

    print()
    print('(r4) - Primera patente del archivo: ', primera, '- Frecuencia de aparicion: ', cpp)

    print()
    print('(r5) - Mayor importe final cobrado:', mayimp, ' - Patente a la que se cobró ese importe:', maypat)

    print()
    print('(r6) - Porcentaje de patentes de otros países:', porc, '\b%')

    print()
    #print('(r7) - Distancia promedio recorrida por vehículos argentinos pasando por cabinas brasileñas:', prom, '\bkm')

if __name__ == "__main__":
    test()