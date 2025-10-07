import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

# Estilo
plt.style.use('classic')

# --- Constantes físicas ---
hbar_c = 197.327  # MeV*fm
m_p = 938.272
m_O = 16 * m_p
mu = (m_p * m_O) / (m_p + m_O)
fm2_to_barn = 0.01

# Parámetros geométricos
R = 4.3  # fm

# Energías de laboratorio (MeV)
E_lab_values = [20.0, 50.0, 100.0]

# Profundidades del pozo a explorar (MeV)
V0_values = [10.0, 20.0, 30.0, 40.0]

# Ángulos
theta = np.linspace(-np.pi/2, np.pi/2, 600)
theta_deg = np.degrees(theta)

def dsigma_domega(theta, E_lab, V0):
    """Distribución angular Born (pozo cuadrado) en barn/sr."""
    E_cm = (m_O / (m_p + m_O)) * E_lab
    k = np.sqrt(2.0 * mu * E_cm) / hbar_c
    q = 2.0 * k * np.sin(theta / 2.0)
    q = np.where(q == 0.0, 1e-12, q)
    f_theta = (2.0 * mu * V0 / (hbar_c**2 * q**3)) * (np.sin(q * R) - q * R * np.cos(q * R))
    return (np.abs(f_theta) ** 2) * fm2_to_barn

# --- Crear un PDF con tres subgráficas en una fila ---
with PdfPages("distribucion_angular_todas.pdf") as pdf:
    fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharey=True)
    
    for ax, E_lab in zip(axes, E_lab_values):
        for V0 in V0_values:
            ax.plot(theta_deg, dsigma_domega(theta, E_lab, V0),
                    label=f"V₀ = {V0:.0f} MeV")
        ax.set_xlabel(r"$\theta$ (grados)")
        ax.set_title(f"$E_{{lab}}$ = {E_lab:.0f} MeV")
        ax.grid(True)
    
    axes[0].set_ylabel(r"$\frac{d\sigma}{d\Omega}$ (barn/sr)")
    axes[-1].legend(loc="upper right", fontsize=8)
    
    plt.tight_layout()
    pdf.savefig(fig, bbox_inches='tight')
    plt.close(fig)

print("✅ PDF 'distribucion_angular_todas.pdf' generado con las tres gráficas en una sola fila.")
