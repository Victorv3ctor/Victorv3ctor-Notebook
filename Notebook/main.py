from Notebook.ui import UI
from Notebook.service import Service
from Notebook.storage import NotebookStorage

notebook = NotebookStorage.from_file('notebook.json')
service = Service(notebook)

ui = UI(service)
try:
    ui.run()
except KeyboardInterrupt:
    print(f'\nAPP SHUT DOWN')
#







