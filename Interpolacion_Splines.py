# Importamos a interpolação InterpolatedUnivariateSpline do módulo de interpolação do Scipy.
# Importamos a biblioteca Matplotlib com um alias.
# Importamos a biblioteca Numpy com um alias.

from scipy.interpolate import InterpolatedUnivariateSpline
import numpy as np
import matplotlib.pyplot as plt

# Armazenamos em arrays os pontos (x, y) a serem interpolados.
x = [0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]
y = [10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1]

# Realizamos a interpolação correspondente.
# O valor de k é a ordem do polinômio desejado, neste caso usaremos k=3.
f_interp = InterpolatedUnivariateSpline(x, y, k=3)

# Plotamos o polinômio obtido.
x1 = np.linspace(0.1, 10)
y_interp = f_interp(x1)
plt.plot(x, y, 'x', mew=3)
plt.plot(x1, y_interp)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Importância de K

    # No código, o parâmetro k refere-se à ordem do polinômio desejado para a interpolação. Neste caso específico, k=3 indica que está sendo utilizado um spline cúbico para realizar a interpolação.

    # A importância de k reside no controle da ordem do polinômio que se ajusta aos dados fornecidos. Aqui estão algumas considerações:

        # Escolha da Ordem do Polinômio:

            # k determina a ordem do polinômio utilizado para a interpolação. Neste caso, k=3 significa que está sendo utilizado um polinômio cúbico para conectar os pontos dados. Os polinômios cúbicos são comumente utilizados na interpolação spline devido ao seu bom equilíbrio entre suavidade e capacidade de se adaptar à forma dos dados.

        # Controle da Suavidade:

            # À medida que k aumenta, o polinômio resultante se torna mais suave e pode se adaptar melhor às variações nos dados. No entanto, um aumento excessivo em k pode levar a um sobreajuste e à introdução de oscilações indesejadas entre os pontos de dados.

        # Equilíbrio entre Flexibilidade e Estabilidade:

            # A escolha de k implica um equilíbrio entre a flexibilidade para se ajustar aos dados e a estabilidade numérica. Ordens de polinômios mais altas podem levar a uma maior complexidade e possivelmente a problemas numéricos, enquanto ordens mais baixas podem não capturar adequadamente a variabilidade nos dados.

    # Em resumo, o valor de k neste contexto controla a ordem do polinômio desejado para a interpolação. A escolha da ordem do polinômio depende da natureza dos dados e dos requisitos específicos do problema. Em geral, um valor de k=3 é uma escolha comum para splines cúbicos na interpolação.

# Por que não é possível atribuir um valor de 10 a k

    # A restrição de que o valor de k deve estar entre 1 e 5 é específica da implementação do ' InterpolatedUnivariateSpline' na biblioteca SciPy. Essa restrição é imposta porque o intervalo normalmente aceito para k neste contexto está entre 1 e 5, e está alinhado com a convenção de que k representa a ordem do polinômio desejado para a interpolação.

    # A razão por trás dessa limitação é principalmente prática e teórica. Aqui estão algumas razões possíveis:

        # Complexidade Computacional:

            # À medida que a ordem do polinômio (k) aumenta, a complexidade computacional para resolver o sistema de equações associado também aumenta significativamente. Ordens mais altas podem exigir mais recursos computacionais e tempo de processamento.

        # Estabilidade Numérica:

            # O uso de polinômios de ordem muito alta pode levar a problemas de estabilidade numérica, especialmente ao lidar com conjuntos de dados ruidosos ou mal condicionados.

        # Sobreajuste:

            # Ordens de polinômios muito altas podem levar a um sobreajuste, onde o polinômio se ajusta demais aos dados de entrada e pode perder a capacidade de generalização.

    # Em resumo, a restrição de k a valores entre 1 e 5 na implementação do 'InterpolatedUnivariateSpline' no SciPy é feita para fornecer uma interface mais segura e eficiente, evitando problemas computacionais e mantendo a estabilidade numérica. Se você precisar de uma ordem de polinômio mais alta, pode considerar outras formas de interpolação ou aproximação que possam lidar com ordens mais elevadas com maior eficiência.