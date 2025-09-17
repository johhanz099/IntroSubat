import numpy as np
import matplotlib.pyplot as plt

# Estilo
plt.style.use('classic')

# Parámetro del pozo
a = 2.0  # fm
x = np.linspace(-a/2, a/2, 500)

# Definición de la función de onda en el pozo [-a/2, a/2]
def psi(n, x, a):
    norm = np.sqrt(2/a)
    k = n * np.pi / a
    if n % 2 == 1:  # n impar → cos
        return norm * np.cos(k * x)
    else:           # n par → sin
        return norm * np.sin(k * x)

# Graficamos los primeros tres niveles
plt.figure(figsize=(8, 5))

for n in range(1, 4):
    plt.plot(x, psi(n, x, a), label=fr"$\psi_{n}(x)$")

plt.xlabel(r"$x$ [fm]")
plt.ylabel(r"$\psi_n(x)$")
plt.legend(
    loc='upper center',
    bbox_to_anchor=(0.5, 1.13),
    ncol=3
)
plt.grid(True)
plt.savefig("p1_grafPozoC_n_1-3.pdf")
#plt.show()
