#Importación de librerías a usar dentro del código
from scipy.interpolate import lagrange
import numpy as np 
import matplotlib.pyplot as plt 

#Variables de x a usar dentro del código (estos datos son de la tabla)
x1 = [20, 40, 60, 80, 100, 120, 140, 160, 180] #Delta de betha (Giro de la manivela)
x2 = [170, 160, 150, 140, 130, 120, 110, 100, 90] #Tetha (Rango angular)

#Variables de y a usar dentro del código (datos tomados de la tabla)
##Razón de cambio para tener rectitud
y1 = [0.601, 1.193, 1.763, 2.299, 2.790, 3.238, 3.623, 3.933, 4.181] #dx/L2
y2 = [3.963, 3.925, 3.850, 3.738, 3.588, 3.438, 3.250, 3.025, 2.800] #L3/L2
y3 = [2.975, 2.950, 2.900, 2.825, 2.725, 2.625, 2.500, 2.350, 2.200] #L1/L2
##Razón de cambio para tener velocidad constante
v1 = [0.480, 0.950, 1.411, 1.845, 2.237, 2.600, 2.932, 3.232, 3.456] #dx/L2
v2 = [2.613, 2.575, 2.538, 2.463, 2.350, 2.238, 2.125, 2.013, 1.863] #L3/L2
v3 = [2.075, 2.050, 2.025, 1.975, 1.900, 1.825, 1.750, 1.675, 1.575] #L1/L2

#Segmento rectilineo (variable a usar dentro del código, sacada del problema), junto al espacio de tiempo que vamos a usar
dx = 20
t = np.linspace(0,200,200)

#Uso de las funciones para interpolación de Lagrange para el giro de la manivela por medio de la rectitud
pglgr1 = lagrange(x1,y1)
pglgr2 = lagrange(x1,y2)
pglgr3 = lagrange(x1,y3)

#Uso de las funciones para interpolación de Lagrange para el rango angular por medio de la rectitud
palgr1 = lagrange(x2,y1)
palgr2 = lagrange(x2,y2)
palgr3 = lagrange(x2,y3)

#Uso de las funciones para interpolación de Lagrange para el giro de la manivela por medio de la velocidad
pglgv1 = lagrange(x1,v1)
pglgv2 = lagrange(x1,v2)
pglgv3 = lagrange(x1,v3)

#Uso de las funciones para interpolación de Lagrange para el rango angular por medio de la velocidad
palgv1 = lagrange(x2,v1)
palgv2 = lagrange(x2,v2)
palgv3 = lagrange(x2,v3)


f1 = p1(t)
f2 = p2(t)
f3 = p3(t)

L2_1 = dx/p1(30)
L1_1 = L2_1*p3(30)
L3_1 = L2_1*p2(30)

print('dx/L2(30): ', p1(30))
print('\nL3/L2(30): ', p2(30))
print('\nL1/L2(30): ', p3(30))
print('\nL1(30): ', L1_1)
print('\nL2(30): ', L2_1)
print('\nL3(30): ', L3_1)

L2_2 = dx/p1(55)
L1_2 = L2_2*p3(55)
L3_2 = L2_2*p2(55)

print('\ndx/L2(55): ', p1(55))
print('\nL3/L2(55): ', p2(55))
print('\nL1/L2(55): ', p3(55))
print('\nL1(55): ', L1_2)
print('\nL2(55): ', L2_2)
print('\nL3(55): ', L3_2)

plt.figure('2')
plt.plot(t, f1, label='interpolacion')
plt.plot(x, y1, 'x', mew=2, label='Datos')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
plt.figure('2')
plt.plot(t, f2, label='interpolacion')
plt.plot(x, y2, 'x', mew=2, label='Datos')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
plt.figure('2')
plt.plot(t, f3, label='interpolacion')
plt.plot(x, y3, 'x', mew=2, label='Datos')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()