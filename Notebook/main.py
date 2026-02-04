#Fixme Poprawiona metoda generowania nowego ID - done
#Fixme Poprawic funkcje FIND !!! Sprawdz jak dziala i sobie zobacz XD -> done
#Fixme Poprawic metode edit aby ta obslugiwala kazdy warunek
#Fixme Skrocic metody tam gdzie to mozliwe, np rozbic jedna metode na wiecej?
#Fixme Zrefaktorowac projekt na dzialajacy na json
#Fixme Testy
#Fixme Wrzucic na github


#FIXME 03/02/26 Zrobione: Dodano zwracanie True lub False dla:
#metody wyswietlania notatek
#metody usuwania notatki
#metody edytowania
#poprawiono stringi w menu (petli glownej .run)
#poprawiono metode wyswietlania opcji do zmiany w metodzie edit



from ui import Menu

menu = Menu()
try:
    menu.run()
except KeyboardInterrupt:
    print(f'\nProgram zakonczony dzialanem spoza MENU')










