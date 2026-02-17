from note import Note
from Notebook.storage import NotebookStorage


class UI:
    def __init__(self):
        notebookstorage = NotebookStorage()
        self.notebook = notebookstorage.from_file('notebook.json')

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

    @staticmethod
    def mini_menu():    #PRZENIESC DO UI
        try:
            choose = int(input('1 TRY AGAIN  |  2 CANCEL : '))
            if choose == 1:
                return True
            elif choose == 2:
                return False
            print("WRONG OPTION")
            return False
        except ValueError:
            print('INNCORECT OPTION TYPE')

    def choose_note(self):
        if not self.notebook.check_notebook_len():
            print('NOTEBOOK IS EMPTY')
            return None
        for note in self.notebook.notes:
            print(f"ID -{note.note_id}-\nTITLE: {note.title}")
        try:
            note_id = int(input('CHOOSE ID: '))
        except ValueError:
            print("WRONG TYPE OF ID")
            return None
        note = self.notebook.get_note_by_id(note_id)
        if not note:
            print('ID NOT FOUND')
            return None
        return note


    def handle_add_note(self):
        note_id = self.notebook.create_new_id()
        title = input('TITLE: ')
        description = input('DESCRIPTION: ')
        date = input('DATE: ')
        tag = input('TAG: ')
        note = Note(note_id, title, description, date, tag)
        self.notebook.add_note(note)

    def handle_show_notebook(self):
        if not self.notebook.check_notebook_len():
            print('NOTEBOOK IS EMPTY')
            return
        for note in self.notebook.notes:
            print(note)

    def handle_find_note(self):
        while True:
            note = self.choose_note()
            if not note:
                return
            print(note)
            if self.mini_menu():
                continue
            return

    def handle_edit_note(self):
        while True:
            note = self.choose_note()
            if not note:
                return
            print(note)
            try:
                choose_key = int(input(f'\n1 TITTLE\n2 DESCRIPTION\n3 DATE\n4 TAG\nCHOOSE EDIT COLUMN: '))
                key = self.notebook.get_edit_key(choose_key)
                if not key:
                    print('WRONG FIELD CHOSEN')
                    return
                value = input(f'{key.upper()} NEW VALUE: ')
                if self.notebook.make_edit(note, key, value):
                    print("CHANGE SAVED")
                    break
            except ValueError:
                print("INCORRECT TYPE OF COLUMN")
                return

    def handle_delete_note(self):
        note = self.choose_note()
        if not note:
            return
        self.notebook.delete_note(note)
        print('NOTED DELETED')

    def handle_update(self):
        NotebookStorage.to_file(self.notebook, 'notebook.json')
        print("\nUPDATE SAVED")

    def run(self):
        options = {
            1: self.handle_add_note,
            2: self.handle_show_notebook,
            3: self.handle_find_note,
            4: self.handle_edit_note,
            5: self.handle_delete_note,
            6: self.handle_update,
            7: None
        }

        while True:
            print(self.show_menu())
            try:
                option = int(input("CHOOSE MENU OPTION: "))
            except ValueError:
                print("WRONG TYPE OF MENU OPTION")
                continue
            if option == 7:
                print("EXIT")
                break
            action = options.get(option)
            if not action:
                print("WRONG MENU OPTION")
                continue
            action()



