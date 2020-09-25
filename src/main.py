from simulation import simulate

def main():
    #Hacer varias simulaciones con distintos valores y ver los resultados... blablabla
    result = simulate(3,3)
    print('Ganancia: $' + str(result['ganancia']))
    print('Costo de oportunidad promedio por semana: $' + str(result['costo_oportunidad_promedio']))

if __name__ == "__main__" :
    main()