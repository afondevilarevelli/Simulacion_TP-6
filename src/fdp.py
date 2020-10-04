from random import random
import math

#Una función por cada f.d.p

def get_intervalo_ventas():
    return get_by_reject(1, 0, 11428320, fdp_pareto_iv)

def get_cant_a_vender_prod(prod):
    if prod == 0:
        return get_cant_a_vender_prod_1()
    return get_cant_a_vender_prod_2()

def get_cant_a_vender_prod_1():
    return round(get_by_reject(1, 0, 3, fdp_log_prod_1)) + 1

def get_cant_a_vender_prod_2():
    return round(get_by_reject(1, 0, 4, fdp_log_prod_2)) + 1

#Funciones

def fdp_log_prod_1(x):
    o = 0.38856
    return (-pow(o, x)) / (x * math.log(1-o))

def fdp_log_prod_2(x):
    o = 0.20635
    return (-pow(o, x)) / (x * math.log(1-o))

def fdp_pareto_iv(x):
    k = 0.75615
    o = 3562.6
    u = -794.25
    return (1/o) * pow((1 + k * ((x-u) / o)), -1-(1/k))

def get_by_reject(m, a, b, fdp):
    done = False
    tita1 = random()
    tita2 = random()
    while not done:
        x = a + (b - a) * tita1
        y = fdp(x)
        if(tita2 <= y / m):
            return x
        else:            
            tita1 = random()
            tita2 = random()