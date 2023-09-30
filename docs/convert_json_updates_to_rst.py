# Queste funzioni vengono eseguite al momento della compilazione della documentazione, dal file conf.py

def update_changelog():

    import os
    import requests
    # "updates.rst" è il file rst contenuto nella directory docs che contiene la lista delle modifiche

    # ottengo il file rst dalla directory docs he è nella stessa root di questo file
    updates_rst = os.path.join(os.path.dirname(__file__), "updates_log.rst")

    url = "https://raw.githubusercontent.com/ExtremeAddons/hdri_maker/master/exa_update.json"

    json_data = requests.get(url).json()

    updates = json_data["updates"]


    with open(updates_rst, "w") as f:
        # Go ahead after the first line
        f.write("Updates Log\n")
        f.write("===========\n")
        f.write("\n")

        for version, value in updates.items():
            date = value.get("date")

            # Scriviamo la versione
            version_date = "{}".format(version)
            f.write(version_date + "\n")
            f.write("-" * len(version_date) + "\n")
            f.write("\n")
            f.write("**Release date: {} (D/M/Y)**\n".format(date))
            f.write("\n")
            descriptions = value.get("descriptions")

            for idx, title_description in descriptions.items():
                title = title_description.get("title")
                description = title_description.get("description")

                f.write("- **" + title + "**\n")
                f.write("\n")
                f.write("    " + description + "\n")
                f.write("\n")

    print("updates_log.rst recompiled :)")





