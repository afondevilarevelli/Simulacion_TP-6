from simulacion import simular

def main():
    #Hacer varias simulaciones con distintos valores y ver los resultados... blablabla
    result = simular(3, 3, 7)
    print('Ganancia: $' + str(result['ganancia']))
    print('Costo de oportunidad promedio por semana: $' + str(result['costo_oportunidad_promedio']))
    print('Promedio de Sobrantes al momento de Comprar (A): ' + str(result['promedio_stock_sobrante_1']))
    print('Promedio de Sobrantes al momento de Comprar (B): ' + str(result['promedio_stock_sobrante_2']))
    print('Pedidos Insatisfechos: ' + str(result['porcentaje_insatisfechos']))

if __name__ == "__main__" :
    main()