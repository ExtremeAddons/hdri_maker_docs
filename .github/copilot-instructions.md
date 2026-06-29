# Istruzioni per GitHub Copilot

Questo progetto contiene la documentazione di HDRi Maker, l'addon è sviluppato da me che ti porrò le domande.

# Regole generali
- Questa documentazione è scritta con Sphinx e reStructuredText (reST).
- Segui sempre le convenzioni di stile PEP 8 per il codice Python.
- Quando scrivi codice, assicurati che sia ben commentato e facilmente leggibile.

# Traduzione
- La documentazione viene scritta in Italiano, ti verrà sempre chiesto di tradurre in Inglese internazionale e tecnico 
  coerente con la terminologia di Blender e del software 3D in generale.
- Consulta sempre le API di Blender qui: https://docs.blender.org/api/current/ per assicurarti che la terminologia sia 
  corretta.

# Contesto
- Assicurati di comprendere sempre tutto il contesto dai file ".rst" presenti nella cartella "docs" del progetto.

# Python Regole Ferree da rispettare sempre senza eccezioni
- Non accetto metodi try/except in nessun caso e non chiedermelo nemmeno, la risposta è sempre no.
- RIPETO, Non usare mai try / except in nessun caso! MAI! Voglio poter vedere sempre gli errori in modo da poterli correggere.
- C'è un file di nome config.py in cui sono definite le costanti globali, tale file viene sempre eseguito quando si
  questa documentazione.
- Non usare mai getattr() o setattr() per controllare se esiste un attributo. Tale attributo deve esistere per forza.
- Non scrivere codice complicato, limitati a seguire le best practice di Python.