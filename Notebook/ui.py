from note import Note
from Notebook.storage import NotebookStorage
class UI:
    def __init__(self):
        notebookstorage = NotebookStorage()
        self.notebook = notebookstorage.from_file('notebook.csv')

    @staticmethod
    def show_menu():
        return(f"==MENU==\n"
        "1 ADD NOTE\n"
        "2 NOTEBOOK\n"
        "3 FIND\n"
        "4 EDIT\n"
        "5 DELETE\n"
        "6 SAVE\n"
        "7 EXIT\n"
               )

    def run(self):
        while True:
            print(self.show_menu())
            try:
                choice = int(input('OPTION: '))
            except ValueError:
                print('INCORRECT TYPE OF MENU OPTION')
            except KeyboardInterrupt:
                print(f'\nSHUT DOWN')
                break
            else:
                if choice == 1:
                    note_id = self.notebook.get_new_id()
                    title = input('TITLE: ')
                    description = input('DESCRIPTION: ')
                    date = input('DATE: ')
                    tag = input('TAG: ')
                    note = Note(note_id, title, description, date, tag)
                    self.notebook.add_note(note)
                elif choice == 2: self.notebook.display_notebook()
                elif choice == 3: self.notebook.find_note()
                elif choice == 4: self.notebook.edit_note()
                elif choice == 5: self.notebook.delete_note()
                elif choice == 6:
                    NotebookStorage.to_file(self.notebook, 'notebook.csv')
                    print("\nUPDATE SAVED")
                elif choice == 0:
                    print('GOOD BYE!!!')
                    break
                else:
                    print("WRONG MENU OPTION")
                    continue
