from fdp import *
from random import random
import sys

#Hacemos que la simulación empiece un lunes y ya se tiene los stock disponibles
#Simulamos por cant. de semanas
#Simulamos 522 semanas (aprox. 10 años)
def simular(cantidades_compra_semanal, frecuencia_compra_dias):
    CANT_SEMANAS = 522

    productos = [
        {
            'precio_venta' : 120,
            'precio_compra' : 70
        },
        {
            'precio_venta' : 300,
            'precio_compra' : 130
        },
    ]

    if(len(productos) != len(cantidades_compra_semanal)):
        print("ERROR")

    #Variables para calcular resultados
    sumatoria_costo_oportunidad = 0
    #Inicio las variables
    stock_actual = [0] * len(productos)
    ganancia = 0
    for i in range(len(productos)):
        stock_actual[i] = cantidades_compra_semanal[i]
        ganancia -= cantidades_compra_semanal[i]*productos[i]['precio_compra'] #Simulo una compra hecha al proveedor al principio de la simulación (y de la 1er semana)

    tiempo = 0
    tiempo_final = __from_semanas_to_minutos(CANT_SEMANAS)

    tiempo_prox_venta = tiempo + get_intervalo_ventas()
    tiempo_prox_compra = tiempo + __from_semanas_to_minutos(1)

    compras_realizadas = 1 #La compra simulada

    sumatoria_stock_sobrante = [0] * len(productos)
    for i in range(len(productos)):
        sumatoria_stock_sobrante[i] = 0

    pedidos_totales = 0
    pedidos_insatisfechos = 0

    print('Simulating...')

    while(tiempo < tiempo_final):
        if(tiempo_prox_compra <= tiempo_prox_venta):
            #Compra a proveedor
            tiempo = tiempo_prox_compra
            tiempo_prox_compra = tiempo + (frecuencia_compra_dias * 24 * 60)

            for i in range(len(productos)):
                sumatoria_stock_sobrante[i] += stock_actual[i]
                stock_actual[i] += cantidades_compra_semanal[i]
                ganancia -= cantidades_compra_semanal[i]*productos[i]['precio_compra']

            compras_realizadas += 1
        else:
            #venta de un producto a un cliente
            tiempo = tiempo_prox_venta
            tiempo_prox_venta = tiempo + get_intervalo_ventas()
            r = random()
            pedidos_totales += 1

            estuvo_insatisfecho = False

            for i in range(len(productos)):
                #Intento vender todos los productos porque el intervalo entre arribos ya contempla la selección ??
                cant_a_vender = get_cant_a_vender_prod(i)
                if(stock_actual[i] >= cant_a_vender):
                    #Hay stock
                    stock_actual[i] -= cant_a_vender
                    ganancia += cant_a_vender*productos[i]['precio_venta']
                else:
                    #No hay stock
                    #Si no hay stock suficiente suponemos que se cancela toda la venta (podría venderse el stock disponible - ¡VER!)
                    sumatoria_costo_oportunidad += cant_a_vender*productos[i]['precio_venta']
                    if not estuvo_insatisfecho:
                        pedidos_insatisfechos += 1
                    estuvo_insatisfecho = True

    promedio_stock_sobrante = [0] * len(productos)
    for i in range(len(sumatoria_stock_sobrante)):
        promedio_stock_sobrante[i] = sumatoria_stock_sobrante[i] / compras_realizadas

    #Retornar un hash/objecto/'loquesea' de resultados
    return {
        'ganancia': ganancia,
        'costo_oportunidad_promedio': int(sumatoria_costo_oportunidad / CANT_SEMANAS),
        'promedio_stock_sobrante' : promedio_stock_sobrante,
        'porcentaje_insatisfechos' : 100 * pedidos_insatisfechos / pedidos_totales
    }
    
def __from_semanas_to_minutos(cant_semanas):
    return cant_semanas * 60 * 24 * 7