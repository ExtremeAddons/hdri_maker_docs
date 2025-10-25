import subprocess
import os

# Percorso della cartella docs (relativo al file Python)
docs_path = os.path.join("docs")
build_path = os.path.join("docs", "_build", "html")

# Esegue lo stesso comando che daresti da terminale
subprocess.run(["sphinx-build", "-b", "html", docs_path, build_path], check=True)
