import numpy as np
import matplotlib.pyplot as plt

# Estilo
plt.style.use('classic')

# --- Coeficientes (tipo "Wapstra") [MeV] ---
a_v = 15.85
a_s = 18.34
a_c = 0.71
a_a = 23.21
a_p = 12
pair_exp = -0.5   # δ ~ A^{-1/2}

# --- Términos y energías ---
def pairing(Z, N):
    A = Z + N
    if A <= 0: return 0.0
    if (Z % 2 == 0) and (N % 2 == 0):  # par-par
        return +a_p * (A ** pair_exp)
    if (Z % 2 == 1) and (N % 2 == 1):  # impar-impar
        return -a_p * (A ** pair_exp)
    return 0.0                          # impar-par

def B(Z, N):
    A = Z + N
    if A <= 0 or Z < 0 or N < 0:
        return np.nan
    return (a_v*A
            - a_s*A**(2/3)
            - a_c*Z*(Z-1)/A**(1/3)
            - a_a*(A - 2*Z)**2 / A
            + pairing(Z, N))

def S_n(Z, N):  # separación de neutrón
    if N <= 0: return np.nan
    return B(Z, N) - B(Z, N-1)

def S_p(Z, N):  # separación de protón
    if Z <= 0: return np.nan
    return B(Z, N) - B(Z-1, N)

# --- Malla ---
Zmax, Nmax = 120, 200
Z = np.arange(0, Zmax+1)
N = np.arange(0, Nmax+1)
ZZ, NN = np.meshgrid(Z, N, indexing='xy')

# --- Evaluación (vectorizada para mantener el código corto) ---
Sn = np.vectorize(S_n)(ZZ, NN)
Sp = np.vectorize(S_p)(ZZ, NN)

# --- Gráfica básica + labels ---
plt.figure(figsize=(7,7))
cs_sn = plt.contour(NN, ZZ, Sn, colors='red', levels=[0])              # S_n = 0
cs_sp = plt.contour(NN, ZZ, Sp, colors='green',levels=[0])  # S_p = 0
d = np.arange(0, min(Zmax, Nmax)+1)
line_zn, = plt.plot(d, d)                  # línea Z=N

# Handles para la leyenda a partir de los contornos
h_sn, _ = cs_sn.legend_elements()
h_sp, _ = cs_sp.legend_elements()

handles, labels = [], []
handles.append(line_zn); labels.append(r'$Z = N$')
if h_sp: handles.append(h_sp[0]); labels.append(r'$S_p = 0$')
if h_sn: handles.append(h_sn[0]); labels.append(r'$S_n = 0$')


plt.legend(handles, labels, loc='upper left')

plt.xlabel(r'$N$')
plt.ylabel(r'$Z$')
plt.xlim(0, Nmax); plt.ylim(0, Zmax)
plt.grid()
plt.savefig("lineas_goteo.pdf")
