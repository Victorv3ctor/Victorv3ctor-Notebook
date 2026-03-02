class UI:
    def __init__(self, service):
        self.service = service

    @staticmethod
    def print_if_empty(notes):
        if not notes:
            print('NOTEBOOK IS EMPTY')
            return True
        return False

    @staticmethod  # tested
    def get_int_input(message, error_msg):  # tested
        try:
            return int(input(message))
        except ValueError:

            print(error_msg)
            return None

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

    def show_and_choose_note(self):
        notes = self.service.get_notes()
        if self.print_if_empty(notes):
            return None
        for note in notes:
            print(note)
        note_id = self.get_int_input('CHOOSE NOTE: ', 'WRONG TYPE OF NOTE ID')
        note_by_id = self.service.choose_note_by_id(note_id)
        if not note_by_id:
            print('ID NOT FOUND')
            return None
        return note_by_id

    def run(self):
        while True:
            print(self.show_menu())
            option = UI.get_int_input('CHOOSE NOTEBOOK OPTION: ', "WRONG TYPE OF MENU OPTION")

            if option == 1:
                title = input('TITLE: ')
                description = input('DESCRIPTION: ')
                date = input('DATE: ')
                tag = input('TAG: ')
                self.service.add_note(title,description,date,tag)

            elif option == 2:
                notes = self.service.get_notes()
                if self.print_if_empty(notes):
                    continue
                for note in notes:
                    print(note)

            elif option == 3:
                note_by_id = self.show_and_choose_note()
                if not note_by_id:
                    continue
                print(note_by_id)

            elif option == 4:
                note = self.show_and_choose_note()
                if not note:
                    continue
                edit_map = {
                    1: 'title',
                    2: 'description',
                    3: 'date',
                    4: 'tag'
                }
                key = self.get_int_input(
"\n1 TITLE"
"\n2 DESCRIPTION"
"\n3 DATE"
"\n4 TAG"
"\nCHOOSE EDIT KEY: ", "INCORRECT TYPE OF KEY")
                if key not in edit_map:
                    print("INCORRECT COLUMN")
                    continue
                value = input('NEW VALUE: ')
                self.service.edit_note(note, key, value)

            elif option == 5:
                notes = self.service.get_notes()
                if self.print_if_empty(notes):
                    continue
                for note in notes:
                    print(note)
                note_by_id = self.get_int_input('CHOOSE NOTE: ', 'WRONG TYPE OF NOTE ID')
                note = self.service.choose_note_by_id(note_by_id)
                if self.service.delete_note(note):
                    print('NOTE DELETED')
                    continue
                print('ID NOT FOUND')

            elif option == 6: self.service.update_notebook()
            elif option == 7: break
            else:
                print('WRONG MENU OPTION')
                break








