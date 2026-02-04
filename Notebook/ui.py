from Notebook.service import Note
from Notebook.storage import NotebookStorage

class Menu:
    def __init__(self):
        notebookstorage = NotebookStorage()
        self.notebook = notebookstorage.from_file('notebook.csv')

    def run(self):
        while True:
                print("1 ADD NOTE")
                print("2 NOTEBOOK")
                print("3 FIND")
                print("4 EDIT")
                print("5 DELETE")
                print("6 SAVE")
                print("0 EXIT")
                try:
                    choice = int(input('MENU OPTION: '))
                except ValueError:
                    print('INCORRECT TYPE OF MENU OPTION')
                except KeyboardInterrupt:
                    print(f'\nSHUT DOWN')
                    break
                else:
                    if choice == 1:
                        no = self.notebook.get_id()
                        title = input('TITTLE: ')
                        description = input('DESCRIPTION: ')
                        date = input('DATE: ')
                        tag = input('TAG: ')
                        note = Note(no, title, description, date, tag)
                        self.notebook.add(note)
                    elif choice == 2:
                        if not self.notebook.show():
                            print('NOTEBOOK IS EMPTY')
                    elif choice == 3:
                        try:
                            while True:
                                if not self.notebook.find_print_id():
                                    print("NO ID TO FIND")
                                    break
                                no = int(input('CHOOSE ID: '))
                                if self.notebook.find_check_no(no):
                                    self.notebook.find_print_note(no)
                                    if self.notebook.find_menu():
                                        continue
                                    else:
                                        break
                                else:
                                    print("WRONG ID")
                                    if self.notebook.find_menu():
                                        continue
                                    else:
                                        break
                        except ValueError:
                            print('INCORRECT TYPE OF ID')
                    elif choice == 4:
                        if not self.notebook.show():
                            print('NOTEBOOK IS EMPTY')
                            continue
                        else:
                            try:
                                no = int(input('CHOOSE ID TO EDIT: '))
                                x = input(f'\nTITLE\nDESCRIPTION\nDATE\nTAG\nCHOOSE COLUMN: ')
                                value = input('NEW VALUE: ')
                                if self.notebook.edit(no, x , value):
                                    print("CHANGE SAVED")
                                else:
                                    print('SOMETHING WENT WRONG')
                            except ValueError:
                                print('INCORRECT TYPE OF ID')
                    elif choice == 5:
                        try:
                            if not self.notebook.show():
                                print('NOTEBOOK IS EMPTY')
                            else:
                                no = int(input('DELETE ID: '))
                                if not self.notebook.delete_note(no):
                                    print('INCORRECT ID')
                                else:
                                    print('NOTE DELETED')
                        except ValueError:
                            print('INCORRECT TYPE OF ID')
                    elif choice == 6:
                        NotebookStorage.to_file(self.notebook, 'notebook.csv')
                    elif choice == 0:
                        print('GOOD BYE!!!')
                        break
