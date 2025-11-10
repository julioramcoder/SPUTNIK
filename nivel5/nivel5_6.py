#Agenda de contactos (lista de diccionarios)

class Agenda:
    def __init__(self):
        self.lista = []
    def addNew(self,contacto,numero):
        nuevo = {contacto : numero}
        self.lista.append(nuevo)
    def getLista(self):
        for contacName in self.lista:
            for nombre, numero in contacName.items():
                print(f"{nombre} : {numero}")


agenda = Agenda()

agenda.addNew("pepe",1233)

agenda.addNew("pepito",12233)

agenda.getLista()

#TODO: documentar todo, agregar función para modificar contacto, eliminar contacto, buscar contacto