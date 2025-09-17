[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/johhanz099/IntroSubat/main?urlpath=lab)

Este entorno reproduce un ambiente listo para análisis científicos con Python (numpy, matplotlib, pandas, etc.) y compilación de programas C++ usando `g++`.

Archivos necesarios:
- `requirements.txt` (librerías Python)
- `apt.txt` (dependencias del sistema como `g++` y `cmake`)


Para instalar las liberías localmente con `uv`:

    uv venv .venv
    source .venv/bin/activate   # en Linux/Mac
    uv pip install -r requirements.txt

Para desactivar `deactivate`    