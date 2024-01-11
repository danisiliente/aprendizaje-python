class Empresa:
    def __init__(self, id, name, country, founded):
        self.__id = id
        self.name = name
        self.country = country
        self.founded = founded
        
    def getMostrar(self):
        print(self.__id, self.name, self.country, self. founded)