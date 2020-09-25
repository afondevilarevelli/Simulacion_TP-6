from simulacion import simular

def main():
    #Hacer varias simulaciones con distintos valores y ver los resultados... blablabla
    result = simular(3,3)
    print('Ganancia: $' + str(result['ganancia']))
    print('Costo de oportunidad promedio por semana: $' + str(result['costo_oportunidad_promedio']))

if __name__ == "__main__" :
    main()