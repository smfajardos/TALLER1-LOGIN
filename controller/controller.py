from models.perro import Perro
from models.guarderia import Guarderia

class Controller:
    def __init__(self):
        pass

    def verPerro(self)->tuple:
        perro1 = Perro("Rufo", "Labrador", 22, 7)
        perro2 = Perro("Bingo", "Pug", 6, 2)
        perro3 = Perro("Lassie", "collie", 27, 5)
        perros = (perro1, perro2, perro3)    
        guarderia = Guarderia ("Guarderia Perrito", "Bogotá", perros)
        return guarderia.retornarPerros()

        