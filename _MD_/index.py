import os
import sys
import json
import subprocess

projects = json.load(open("index.json", "r", encoding="UTF8"))

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

while True:
    print("Projects:")
    for i, project in enumerate(projects):
        print(f"{i + 1}: {project['name']}")

    choice = input("Choose a Project: ")

    try:
        index = int(choice) - 1
        selected = projects[index]
        programm = selected["programm"]
        path = selected["path"]
        abs_path = os.path.abspath(path)

        print(f"opening {selected['name']} with {programm} in {path} ...")
        subprocess.run(f'{programm} "{abs_path}"', shell=True)

    except (IndexError, ValueError):
        print("Invalid Choice.")
        sys.exit(1)
    
    input("... ")
