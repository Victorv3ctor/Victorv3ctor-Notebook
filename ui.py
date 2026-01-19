from service import Note
from storage import NotebookStorage



class Menu:
    def __init__(self):
        notebookstorage = NotebookStorage()
        self.notebook = notebookstorage.from_file('notebook.csv')

    def run(self):
        while True:
                print("1 Add new note")
                print("2 Show notes")
                print("3 Find note")
                print("4 Edit note")
                print("5 Delete note")
                print("6 Save")
                print("0 Exit")
                try:
                    choice = int(input('Choose menu option: '))
                except ValueError:
                    print('Incorrect menu option')
                except KeyboardInterrupt:
                    print(f'\nProgram zakonczony dzialanem spoza MENU')
                    break
                else:
                    if choice == 1:
                        no = self.notebook.create_id()
                        title = input('Tittle: ')
                        description = input('Description: ')
                        date = input('Date: ')
                        tags = input('Tags: ')
                        note = Note(no, title, description, date, tags)
                        self.notebook.add(note)
                    elif choice == 2:
                        self.notebook.show()
                    elif choice == 3:
                        try:
                            self.notebook.find_id()
                            no = int(input('Choose ID that you looking for: '))
                            self.notebook.find(no)
                        except ValueError:
                            print('Incorrect ID')
                    elif choice == 4:
                        self.notebook.show()
                        try:
                            no = int(input('Wynbierz ID notatki do edycji: '))
                            x = input('Ktora kolumne edytujesz ?: ')
                            value = input('Wprowadz zmiane: ')
                            self.notebook.edit(no, x , value)
                        except ValueError:
                            print('Incorrect ID')
                    elif choice == 5:
                        try:
                            self.notebook.show()
                            no = int(input('Usun ID: '))
                            self.notebook.delete(no)
                        except ValueError:
                            print('Incorrect ID')
                    elif choice == 6:
                        NotebookStorage.to_file(self.notebook,'notebook.csv')
                    elif choice == 0:
                        print('Good bye!!!')
                        break
