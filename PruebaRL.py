import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

a1n = 1
a2n = 1.5
data = loadmat('Datos_robot_2gdl_error_P') 
Theta = data['Theta'] # primera columna es $theta_1$, segunda columna es $theta_2$
P = data['P'] # primera columna es $x$, segunda columna es $y$

theta1 = Theta[:, 0]
theta2 = Theta[:, 1]
theta12 = theta1 + theta2

x = P[:, 0]
y = P[:, 1]

# instrucción: Construir el regresor y almacenarlo en la variable A
A = np.column_stack((np.cos([theta1, theta12]),np.sin([theta1, theta12]))).T

# Instrucciones: Realizar la regresión, almancenar la variable phi, extraer las variables corregidas a1 y a2
phi = np.linalg.pinv(A)@np.hstack((x,y))
a1, a2 = phi[0], phi[1]

xb = a1 * np.cos(theta1)
yb = a1 * np.sin(theta1)
xc = xb + a2 * np.cos(theta12)
yc = yb + a2 * np.sin(theta12)
xbn = a1n * np.cos(theta1)
ybn = a1n * np.sin(theta1)
xcn = xbn + a2n * np.cos(theta12)
ycn = ybn + a2n * np.sin(theta12)

# Salida gráfica
plt.figure()
plt.plot(x, y, 'o', xc, yc, '+', xcn, ycn, '*')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Posicion medida', 'Posicion modelo ajustado', 'Posicion nominal'], loc='best')
plt.title(f'Calibración robot 2GDL, a = {a1:.4f}, b = {a2:.4f}')
plt.axis('equal')
plt.grid(True)
plt.show()