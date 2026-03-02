class Note: #testes all - unit
    def __init__(self, note_id, title, description, date, tag):
        self.note_id = note_id
        self.title = title
        self.description = description
        self.date = date
        self.tag = tag

    def change_title(self, new_value):
        self.title = new_value

    def change_description(self, new_value):
        self.description = new_value

    def change_date(self, new_value):
        self.date = new_value

    def change_tag(self, new_value):
        self.tag = new_value

    def to_dict(self): # to make test
        return {'id':self.note_id ,'title':self.title, 'description':self.description, 'date':self.date, 'tag':self.tag}

    def __str__(self): # to make test
        return (f"""
=ID[{self.note_id}]=
===TITLE===
{self.title}
{self.description}
Date: {self.date}
Tag: {self.tag.upper()}
----------\n"""
        )
