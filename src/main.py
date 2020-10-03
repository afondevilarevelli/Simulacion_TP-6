from simulacion import simular

def main():
    #Hacer varias simulaciones con distintos valores y ver los resultados... blablabla
    result = simular([20, 20], 7)
    print('Ganancia: $' + str(result['ganancia']))
    print('Costo de oportunidad promedio por semana: $' + str(result['costo_oportunidad_promedio']))

    for i in range(len(result['promedio_stock_sobrante'])):
        print('Promedio de Sobrantes al momento de Comprar (' + str(i) + '): ' + str(result['promedio_stock_sobrante'][0]))

    print('Pedidos Insatisfechos: ' + str(result['porcentaje_insatisfechos']))

if __name__ == "__main__" :
    main()