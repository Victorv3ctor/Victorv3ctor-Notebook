from Notebook.note import Note
from Notebook.storage import NotebookStorage

class UI:
    def __init__(self):
        self.storage = NotebookStorage()
        self.notebook = self.storage.from_file('notebook.json')

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

    def mini_menu(self): #tested
        choose = self._get_int_input("1 TRY AGAIN\n2 CANCEL\nCHOOSE MENU OPTION: ", "WRONG TYPE OF OPTION")
        if choose == 1:
            return True
        elif choose == 2:
            return False
        print("WRONG OPTION")
        return False

    @staticmethod #tested
    def _get_int_input(message, error_msg): #tested
        try:
            return int(input(message))
        except ValueError:
            print(error_msg)
            return None

    def choose_note(self): #tested
        notes = self.notebook.get_notes()
        if not notes:
            print('NOTEBOOK IS EMPTY')
            return None
        for line in notes:
            print(f"ID -{line.note_id}-\nTITLE: {line.title}\n")
        note_id = UI._get_int_input('CHOOSE YOUR NOTE ID: ', 'WRONG TYPE OF ID')
        note_by_id = self.notebook.get_note_by_id(note_id)
        if not note_by_id:
            print('ID NOT FOUND')
            return None
        return note_by_id


    def handle_add_note(self): #tested
        note_id = self.notebook.create_new_id()
        title = input('TITLE: ')
        description = input('DESCRIPTION: ')
        date = input('DATE: ')
        tag = input('TAG: ')
        note = Note(note_id, title, description, date, tag)
        self.notebook.add_note(note)

    def handle_show_notebook(self): # TO BE CONTINUED
        if not self.notebook.get_notes():
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
            choose_key = (self._get_int_input(

"\n1 TITLE"
"\n2 DESCRIPTION"
"\n3 DATE"
"\n4 TAG"
"\nCHOOSE EDIT KEY: ", "INCORRECT TYPE OF KEY"))
            key = self.notebook.get_edit_key(choose_key)
            if not key:
                print('WRONG KEY CHOSEN')
                return
            value = input(f'{key.upper()} NEW VALUE: ')
            self.notebook.make_edit(note, key, value)
            print("CHANGE SAVED")
            break

    def handle_delete_note(self):
        note = self.choose_note()
        if not note:
            return
        self.notebook.delete_note(note)
        print('NOTED DELETED')

    def handle_update(self):
        self.storage.to_file(self.notebook, 'notebook.json')
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
            option = self._get_int_input('CHOOSE NOTEBOOK OPTION: ', "WRONG TYPE OF MENU OPTION")
            if option is None:
                continue
            if option == 7:
                break
            action = options.get(option)
            if not action:
                print("WRONG MENU OPTION")
                continue
            action()



