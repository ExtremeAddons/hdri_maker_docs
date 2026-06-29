import subprocess
import os
import sys

# Percorso della cartella docs (relativo al file Python)
docs_path = os.path.join("docs")
build_path = os.path.join("docs", "_build", "html")

# Esegue lo stesso comando che daresti da terminale
# subprocess.run(["sphinx-build", "-b", "html", docs_path, build_path], check=True)
subprocess.run([sys.executable, "-m", "sphinx", "-b", "html", docs_path, build_path], check=True)
