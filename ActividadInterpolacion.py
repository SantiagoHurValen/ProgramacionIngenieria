#Importación de librerías a usar dentro del código
from scipy.interpolate import lagrange
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.interpolate import barycentric_interpolate
import numpy as np 
import matplotlib.pyplot as plt 

#Variables de x a usar dentro del código (estos datos son de la tabla)
x1 = [20, 40, 60, 80, 100, 120, 140, 160, 180] #Delta de betha (Giro de la manivela)

#Variables de y a usar dentro del código (datos tomados de la tabla)
##Razón de cambio para tener rectitud
y1 = [0.601, 1.193, 1.763, 2.299, 2.790, 3.238, 3.623, 3.933, 4.181] #dx/L2
y2 = [3.963, 3.925, 3.850, 3.738, 3.588, 3.438, 3.250, 3.025, 2.800] #L3/L2
y3 = [2.975, 2.950, 2.900, 2.825, 2.725, 2.625, 2.500, 2.350, 2.200] #L1/L2
##Razón de cambio para tener velocidad constante
v1 = [0.480, 0.950, 1.411, 1.845, 2.237, 2.600, 2.932, 3.232, 3.456] #dx/L2
v2 = [2.613, 2.575, 2.538, 2.463, 2.350, 2.238, 2.125, 2.013, 1.863] #L3/L2
v3 = [2.075, 2.050, 2.025, 1.975, 1.900, 1.825, 1.750, 1.675, 1.575] #L1/L2

#Segmento rectilineo (variable a usar dentro del código, sacada del problema)
dx = 20

#LaGrange
#Uso de las funciones para interpolación de Lagrange para el giro de la manivela por medio de la rectitud
pglgr1 = lagrange(x1,y1)
pglgr2 = lagrange(x1,y2)
pglgr3 = lagrange(x1,y3)

#Uso de las funciones para interpolación de Lagrange para el giro de la manivela por medio de la velocidad
pglgv1 = lagrange(x1,v1)
pglgv2 = lagrange(x1,v2)
pglgv3 = lagrange(x1,v3)

#Despejes para encontrar los valores de L1, L2 y L3 con el criterio de rectitud
L2_1 = dx/pglgr1(30)
L1_1 = L2_1*pglgr3(30)
L3_1 = L2_1*pglgr2(30)

#Se imprimen los valores hallados por la interpolación, en este caso para los 30° en su criterio de rectitud
print('\n***RAZONES DE CAMBIO Y VALORES DE LAS DIMENSIONES PARA UN RANGO ANGULAR DE 30° CON RESPECTO A LA RECTITUD***\n')
print('\ndx/L2(30): ', pglgr1(30))
print('\nL3/L2(30): ', pglgr2(30))
print('\nL1/L2(30): ', pglgr3(30))
print('\nL1(30): ', L1_1)
print('\nL2(30): ', L2_1)
print('\nL3(30): ', L3_1)

#Despejes para encontrar los valores de L1, L2 y L3 con el criterio de velocidad
L2_2 = dx/pglgv1(30)
L1_2 = L2_2*pglgv3(30)
L3_2 = L2_2*pglgv2(30)

#Se imprimen los valores hallados por la interpolación, en este caso para los 30° en su criterio de velocidad
print('\n***RAZONES DE CAMBIO Y VALORES DE LAS DIMENSIONES PARA UN RANGO ANGULAR DE 30° CON RESPECTO A LA VELOCIDAD***\n')
print('\ndx/L2(30): ', pglgv1(30))
print('\nL3/L2(30): ', pglgv2(30))
print('\nL1/L2(30): ', pglgv3(30))
print('\nL1(30): ', L1_2)
print('\nL2(30): ', L2_2)
print('\nL3(30): ', L3_2)

#Despejes para encontrar los valores de L1, L2 y L3 con el criterio de rectitud
L2_1 = dx/pglgr1(55)
L1_1 = L2_1*pglgr3(55)
L3_1 = L2_1*pglgr2(55)

#Se imprimen los valores hallados por la interpolación, en este caso para los 55° en su criterio de rectitud
print('\n***RAZONES DE CAMBIO Y VALORES DE LAS DIMENSIONES PARA UN RANGO ANGULAR DE 55° CON RESPECTO A LA RECTITUD***\n')
print('\ndx/L2(55): ', pglgr1(55))
print('\nL3/L2(55): ', pglgr2(55))
print('\nL1/L2(55): ', pglgr3(55))
print('\nL1(55): ', L1_1)
print('\nL2(55): ', L2_1)
print('\nL3(55): ', L3_1)

#Despejes para encontrar los valores de L1, L2 y L3 con el criterio de velocidad
L2_2 = dx/pglgv1(55)
L1_2 = L2_2*pglgv3(55)
L3_2 = L2_2*pglgv2(55)

#Se imprimen los valores hallados por la interpolación, en este caso para los 55° en su criterio de velocidad
print('\n***RAZONES DE CAMBIO Y VALORES DE LAS DIMENSIONES PARA UN RANGO ANGULAR DE 55° CON RESPECTO A LA VELOCIDAD***\n')
print('\ndx/L2(55): ', pglgv1(55))
print('\nL3/L2(55): ', pglgv2(55))
print('\nL1/L2(55): ', pglgv3(55))
print('\nL1(55): ', L1_2)
print('\nL2(55): ', L2_2)
print('\nL3(55): ', L3_2)

##Splines
#Uso de las funciones para interpolación de Splines para el giro de la manivela por medio de la rectitud
pgspr1 = InterpolatedUnivariateSpline(x1,y1)
pgspr2 = InterpolatedUnivariateSpline(x1,y2)
pgspr3 = InterpolatedUnivariateSpline(x1,y3)

#Uso de las funciones para interpolación de Splines para el giro de la manivela por medio de la velocidad
pgspv1 = InterpolatedUnivariateSpline(x1,v1)
pgspv2 = InterpolatedUnivariateSpline(x1,v2)
pgspv3 = InterpolatedUnivariateSpline(x1,v3)

#Despejes para encontrar los valores de L1, L2 y L3 con el criterio de rectitud
L2_1 = dx/pgspr1(30)
L1_1 = L2_1*pgspr3(30)
L3_1 = L2_1*pgspr2(30)

#Se imprimen los valores hallados por la interpolación, en este caso para los 30° en su criterio de rectitud
print('\n***RAZONES DE CAMBIO Y VALORES DE LAS DIMENSIONES PARA UN RANGO ANGULAR DE 30° CON RESPECTO A LA RECTITUD***\n')
print('\ndx/L2(30): ', pgspr1(30))
print('\nL3/L2(30): ', pgspr2(30))
print('\nL1/L2(30): ', pgspr3(30))
print('\nL1(30): ', L1_1)
print('\nL2(30): ', L2_1)
print('\nL3(30): ', L3_1)

#Despejes para encontrar los valores de L1, L2 y L3 con el criterio de velocidad
L2_2 = dx/pgspv1(30)
L1_2 = L2_2*pgspv3(30)
L3_2 = L2_2*pgspv2(30)

#Se imprimen los valores hallados por la interpolación, en este caso para los 30° en su criterio de velocidad
print('\n***RAZONES DE CAMBIO Y VALORES DE LAS DIMENSIONES PARA UN RANGO ANGULAR DE 30° CON RESPECTO A LA VELOCIDAD***\n')
print('\ndx/L2(30): ', pgspv1(30))
print('\nL3/L2(30): ', pgspv2(30))
print('\nL1/L2(30): ', pgspv3(30))
print('\nL1(30): ', L1_2)
print('\nL2(30): ', L2_2)
print('\nL3(30): ', L3_2)

#Despejes para encontrar los valores de L1, L2 y L3 con el criterio de rectitud
L2_1 = dx/pgspr1(55)
L1_1 = L2_1*pgspr3(55)
L3_1 = L2_1*pgspr2(55)

#Se imprimen los valores hallados por la interpolación, en este caso para los 55° en su criterio de rectitud
print('\n***RAZONES DE CAMBIO Y VALORES DE LAS DIMENSIONES PARA UN RANGO ANGULAR DE 55° CON RESPECTO A LA RECTITUD***\n')
print('\ndx/L2(55): ', pgspr1(55))
print('\nL3/L2(55): ', pgspr2(55))
print('\nL1/L2(55): ', pgspr3(55))
print('\nL1(55): ', L1_1)
print('\nL2(55): ', L2_1)
print('\nL3(55): ', L3_1)

#Despejes para encontrar los valores de L1, L2 y L3 con el criterio de velocidad
L2_2 = dx/pgspv1(55)
L1_2 = L2_2*pgspv3(55)
L3_2 = L2_2*pgspv2(55)

#Se imprimen los valores hallados por la interpolación, en este caso para los 55° en su criterio de velocidad
print('\n***RAZONES DE CAMBIO Y VALORES DE LAS DIMENSIONES PARA UN RANGO ANGULAR DE 55° CON RESPECTO A LA VELOCIDAD***\n')
print('\ndx/L2(55): ', pgspv1(55))
print('\nL3/L2(55): ', pgspv2(55))
print('\nL1/L2(55): ', pgspv3(55))
print('\nL1(55): ', L1_2)
print('\nL2(55): ', L2_2)
print('\nL3(55): ', L3_2)