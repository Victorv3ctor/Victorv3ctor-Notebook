
class Note:
    def __init__(self, no, title, description, date, tags):
        self.no = no
        self.title = title
        self.description = description
        self.date = date
        self.tags = tags

    def dict(self):
        return {'id':self.no ,'title':self.title, 'description':self.description, 'date':self.date, 'tags':self.tags}

    def __str__(self):
        return f'{self.no} {self.title} {self.description} {self.date} {self.tags}'


class Notebook:
    def __init__(self):
        self.notes = []

    def create_id(self):
        biggest = 0
        for row in self.notes:
            current = int(row.no)
            if current > biggest:
                biggest = current
        return biggest + 1

    def add(self,note):
        self.notes.append(note)

    def find_id(self):
        for note in self.notes:
            print(f'ID[{note.no}]')

    def find(self, no):
        for note in self.notes:
            if no == int(note.no):
                print(f"""
=ID[{note.no}]=
===TITLE===
{note.title}
{note.description}
Date: {note.date}
Tags {note.tags}
----------""")
                return True
        return False


    def show(self):
        if len(self.notes) > 0:
            for note in self.notes:
                print(f"""
=ID[{ note.no}]=
===TITLE===
{note.title}
{note.description}
Date: {note.date}
Tags {note.tags}
----------""")
        else:
            print('Brak zapisow')

    def edit(self,no,x,value):
        found = False
        for note in self.notes:
            if int(note.no) == int(no):
                setattr(note,x,value) # setattr -> ustawia atrybut X obiektu NOTE na wawrtosc Value
            #uzywamy go gdy chcemy zmienic atrybut obiektu dynamicznie i gdy nie jest przypisany na sztywno
            #pozwala uniknac ifow i pozwala obiektowi (note) nadpisac okreslony atrybut (x) np.title na nowa wartosc (value) wybrana przez uzytkownika np.hej
                found = True
                break
        if not found:
            print('Nie znaleziono')


    def delete(self, no):
        self.notes = [note for note in self.notes if int(note.no) != no]


