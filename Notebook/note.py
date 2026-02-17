class Note:
    def __init__(self, note_id, title, description, date, tag):
        self.note_id = note_id
        self.title = title
        self.description = description
        self.date = date
        self.tag = tag

    def to_dict(self):
        return {'id':self.note_id ,'title':self.title, 'description':self.description, 'date':self.date, 'tag':self.tag}

    def __str__(self):
        return (f"""
=ID[{self.note_id}]=
===TITTLE===
{self.title}
{self.description}
Date: {self.date}
Tag: {self.tag.upper()}
----------\n"""
        )
