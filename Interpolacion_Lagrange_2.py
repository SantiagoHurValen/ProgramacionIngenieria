# Importamos a interpolação de Lagrange do módulo de interpolação do Scipy.
# Importamos a biblioteca Matplotlib com um alias.
# Importamos a biblioteca Numpy com um alias para realizar os cálculos.
from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt

# Guardamos os valores de x e f(x) a serem utilizados em vetores.
x = [1,2,3,4,6]
y = [275000,530000,810000,1155000,1650000]

# Plotamos os valores a serem interpolados.
plt.figure('1')
plt.plot(x,y,'x', mew=2, label='Datos')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

# Polinômio de Lagrange para os pontos dados.
p = lagrange(x,y)

# Avaliar o polinômio obtido em um intervalo de [0,6].
x1 = np.linspace(0,1,1000)
y1 = p(x1)

# Plotamos o polinômio obtido, assim como os pontos utilizados.
plt.figure('2')
plt.plot(x1, y1, label='interpolacion')
plt.plot(x, y, 'x', mew=2, label='Datos')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

# Se quisermos obter valores de f(x), tudo o que precisamos fazer é avaliar o polinômio no ponto x. Por exemplo, para encontrar f(x) quando x=1.8.
print(p(5.5))