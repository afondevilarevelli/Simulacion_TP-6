from fdp import *
from random import random
import sys

#Hacemos que la simulación empiece un lunes y ya se tiene los stock disponibles
#Simulamos por cant. de semanas
#Simulamos 522 semanas (aprox. 10 años)
def simulate(var_control_1, var_control_2):
    CANT_SEMANAS = 522
    PRECIO_VENTA_1 = 123
    PRECIO_VENTA_2 = 123
    PRECIO_COMPRA_1 = 100
    PRECIO_COMPRA_2 = 100

    #Variables para calcular resultados
    sumatoria_costo_oportunidad = 0
    #Inicio las variables
    stock_1 = var_control_1
    stock_2 = var_control_2
    ganancia = - var_control_1*PRECIO_COMPRA_1 - var_control_2*PRECIO_COMPRA_2 #Simulo una compra hecha al proveedor al principio de la simulación (y de la 1er semana)
    tiempo = 0
    tiempo_final = __from_semanas_to_minutos(CANT_SEMANAS)
    tiempo_prox_venta = tiempo + get_intervalo_ventas()
    tiempo_prox_compra = tiempo + __from_semanas_to_minutos(1)
    print('Simulating...')

    while(tiempo < tiempo_final):
        if(tiempo_prox_compra <= tiempo_prox_venta):
            #Compra a proveedor
            tiempo = tiempo_prox_compra
            tiempo_prox_compra = tiempo + __from_semanas_to_minutos(1)
            stock_1 += var_control_1
            stock_2 += var_control_2
            ganancia -= var_control_1*PRECIO_COMPRA_1 + var_control_2*PRECIO_COMPRA_2
        else:
            #venta de un producto a un cliente
            tiempo = tiempo_prox_venta
            tiempo_prox_venta = tiempo + get_intervalo_ventas()
            r = random()
            if(r <= 0.6): #Tiré una prob. fruta
                #Venta de producto 1
                cant_a_vender = get_cant_a_vender_prod_1()
                if(stock_1 >= cant_a_vender):
                    #Hay stock
                    stock_1 -= cant_a_vender
                    ganancia += cant_a_vender*PRECIO_VENTA_1
                else:
                    #No hay stock
                    #Si no hay stock suficiente suponemos que se cancela toda la venta (podría venderse el stock disponible - ¡VER!)
                    sumatoria_costo_oportunidad += cant_a_vender*PRECIO_VENTA_1
            else:
                #Venta de producto 2
                cant_a_vender = get_cant_a_vender_prod_2()
                if(stock_2 >= cant_a_vender):
                    #Hay stock
                    stock_2 -= cant_a_vender
                    ganancia += cant_a_vender*PRECIO_VENTA_2
                else:
                    #No hay stock
                    #Si no hay stock suficiente suponemos que se cancela toda la venta (podría venderse el stock disponible - ¡VER!)
                    sumatoria_costo_oportunidad += cant_a_vender*PRECIO_VENTA_2

    #Retornar un hash/objecto/'loquesea' de resultados
    return {
        'ganancia': ganancia,
        'costo_oportunidad_promedio': int(sumatoria_costo_oportunidad / CANT_SEMANAS)
    }
    
def __from_semanas_to_minutos(cant_semanas):
    return cant_semanas * 60 * 24 * 7