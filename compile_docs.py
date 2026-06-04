import subprocess
import os
import sys

# Recupera la cartella in cui si trova questo script
base_path = os.path.dirname(os.path.abspath(__file__))

# Percorsi relativi calcolati in modo sicuro
docs_path = os.path.join(base_path, "docs")
build_path = os.path.join(base_path, "docs", "_build", "html")

# Punta direttamente allo 'sphinx-build' dentro l'ambiente virtuale Linux (.venv/bin/)
sphinx_executable = os.path.join(base_path, ".venv", "bin", "sphinx-build")

# Se per qualche motivo usi ancora l'ambiente Windows, usa questa riga di riserva:
if not os.path.exists(sphinx_executable):
    sphinx_executable = os.path.join(base_path, ".venv", "Scripts", "sphinx-build")

print(f"Esecuzione di Sphinx tramite: {sphinx_executable}")

# Esegue il comando puntando al percorso esatto del file eseguibile
subprocess.run([sphinx_executable, "-b", "html", docs_path, build_path], check=True)
