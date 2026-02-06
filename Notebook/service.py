class Note:
    def __init__(self, no, title, description, date, tag):
        self.no = no
        self.title = title
        self.description = description
        self.date = date
        self.tag = tag

    def to_dict(self):
        return {'id':self.no ,'title':self.title, 'description':self.description, 'date':self.date, 'tag':self.tag}


class Notebook:
    def __init__(self):
        self.notes = []

    def add(self,note):
        self.notes.append(note)

    def get_id(self):
        if len(self.notes) > 0:
            numbers = [int(note.no) for note in self.notes]
            highest = max(numbers)
            return highest + 1
        return 1

    def find_print_id(self):
        for note in self.notes:
            print(f'ID[{note.no}]\nTITLE: {note.title}')
        return bool(self.notes)

    def find_check_no(self, no):
        for note in self.notes:
            if no == int(note.no):
                return True
        return False

    def find_print_note(self, no):
        for note in self.notes:
            if no == int(note.no):
                print(f"""
=ID[{note.no}]=
===TITLE===
{note.title}
{note.description}
Date: {note.date}
Tag: {note.tag}
----------""")

    @staticmethod
    def find_menu():
        option = True
        choose = int(input('1 TRY AGAIN  |  2 CANCEL : '))
        if choose == 2:
            option = False
        return option

    def show(self):
        for note in self.notes:
            print(f"""
=ID[{ note.no}]=
===TITLE===
{note.title}
{note.description}
Date: {note.date}
Tag: {note.tag}
----------""")
        return bool(self.notes)

    def edit_check_no(self, no):
        for note in self.notes:
            if no == int(note.no):
                return note
        return False

    @staticmethod
    def edit_key(choose):
        keys = {1: "title", 2: "description", 3: "date", 4: "tag"}
        return keys.get(choose, '')

    @staticmethod
    def edit(note,key,value):
        setattr(note,key,value)
        return True

    def delete_note(self, no):
        for note in self.notes:
            if int(note.no) == no:
                self.notes = [note for note in self.notes if int(note.no) != no]
                return True
        return False


