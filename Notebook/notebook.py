class Notebook:
    def __init__(self):
        self.notes = []

    @staticmethod
    def mini_menu():
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

    def check_notebook_len(self):
        return bool(self.notes)

    def add_note(self,note):
        self.notes.append(note)

    def get_new_id(self):
        if len(self.notes) > 0:
            numbers = [int(note.note_id) for note in self.notes]
            highest = max(numbers)
            return highest + 1
        return 1

    def check_note_id(self, no):
        for note in self.notes:
            if no == int(note.note_id):
                return note
        return False

    def display_id(self):
        for note in self.notes:
            print(f'ID[{note.note_id}]\nTITTLE: {note.title}')
        return bool(self.notes)

    def display_notebook(self):
        if not self.check_notebook_len():
            print('NOTEBOOK IS EMPTY')
            return False
        for note in self.notes:
            print(f"""
=ID[{note.note_id}]=
===TITTLE===
{note.title}
{note.description}
Date: {note.date}
Tag: {note.tag.upper()}
----------""")
        return True

    def display_single_note(self, note_id):
        for note in self.notes:
            if self.check_note_id(note_id):
                print(f"""
=ID[{note.note_id}]=
===TITTLE===
{note.title}
{note.description}
Date: {note.date}
Tag: {note.tag.upper()}
----------""")

    def find_note(self):
        try:
            while True:
                if not self.display_id():
                    print("NO ID TO FIND")
                    break
                note_id = int(input('CHOOSE ID: '))
                if self.check_note_id(note_id):
                    self.display_single_note(note_id)
                    if self.mini_menu():
                        continue
                    break
                print("WRONG ID")
                break
        except ValueError:
            print('INCORRECT TYPE OF ID')

    @staticmethod
    def get_edit_key(choose):
        keys = {1: "title", 2: "description", 3: "date", 4: "tag"}
        return keys.get(choose, '')

    @staticmethod
    def make_edit(note,key,value):
        setattr(note,key,value)
        return True

    def edit_note(self):
        while True:
            if not self.check_notebook_len():
                print('NOTEBOOK IS EMPTY')
                break
            try:
                self.display_notebook()
                no = int(input("CHOOSE ID: "))
                note = self.check_note_id(no)
            except ValueError:
                print('WRONG TYPE OF ID')
                break
            if not note:
                print('WRONG ID CHOSEN')
                if not self.mini_menu():
                    break
                continue
            try:
                choose = int(input(f'\n1 TITTLE\n2 DESCRIPTION\n3 DATE\n4 TAG\nCHOOSE COLUMN: '))
                key = self.get_edit_key(choose)
                if not key:
                    print('WRONG FIELD CHOSEN')
                    if not self.mini_menu():
                        break
                value = input(f'{key.upper()} NEW VALUE: ')
                if self.make_edit(note, key, value):
                    print("CHANGE SAVED")
                    break
                print('SOMETHING WENT WRONG')
            except ValueError:
                print('INCORRECT TYPE OF COLUMN')
                if self.mini_menu():
                    continue
                break

    def delete_by_id(self):
        note_id = int(input("DELETE ID: "))
        if self.check_note_id(note_id):
            return note_id
        return False

    def delete_note(self):
        try:
            if not self.display_notebook():
                print('NOTEBOOK IS EMPTY')
            note_id = self.delete_by_id()
            if not note_id:
                print('INCORRECT ID')
            else:
                self.notes = [note for note in self.notes if int(note.note_id) != note_id]
                print('NOTE DELETED')
        except ValueError:
            print('INCORRECT TYPE OF ID')



