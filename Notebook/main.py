# Fixme 3 zrobic testy jednostkowe, ogarnac testy integracyjne i wprowadzic w projekt
#  Nic poza tym juz nie dodwac, ruszyc z API!

from ui import UI


ui = UI()
try:
    ui.run()
except KeyboardInterrupt:
    print(f'\nProgram zakonczony dzialanem spoza MENU')
#







