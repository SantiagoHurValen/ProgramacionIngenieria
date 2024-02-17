# Importamos a interpolação de Lagrange do módulo de interpolação do Scipy.
# Importamos a biblioteca Matplotlib com um alias.
# Importamos a biblioteca Numpy com um alias para realizar os cálculos.
from scipy.interpolate import barycentric_interpolate
import numpy as np
import matplotlib.pyplot as plt

# Aplicaremos a interpolação baricêntrica para a função dada.
# A interpolação baricêntrica é um método de interpolação polinomial que utiliza a forma baricêntrica dos polinômios de Lagrange. A ideia principal é evitar a expansão do polinômio de Lagrange completo para cada novo ponto a ser interpolado, o que pode ser computacionalmente caro.
def runge(x):
    """Funcion de Runge"""
    return 1 / (1 + x ** 4)

# Nós de interpolação.
N = 300
# linspace retorna espaços numéricos uniformemente espaçados.
xp = np.linspace(-5,5,N)
fp = runge(xp)
x = np.linspace(-5,5,200)
y = barycentric_interpolate(xp, fp, x)

# Plotamos os polinômios obtidos.
plt.figure('1')
plt.plot(x,y, label='Interpolación')
plt.plot(xp, fp, 'x')
plt.plot(x, runge(x), label='Función real')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc='upper center')
plt.show()