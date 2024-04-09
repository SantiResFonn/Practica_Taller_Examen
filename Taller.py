

class Elemento:
    nombre: str
    def comparar(self,nombre):
        return nombre == nombre
class Conjunto:
    def __init__(self, nombre, contador) -> None:
        self.lista: list[Elemento] = []
        self.nombre = nombre
        self.contador = 0 + contador
    @property
    def privado(self):
        self.id = self.contador
    def contiene(self, objeto: Elemento):
        return self.lista.contains(objeto)
    def agregar_elemento(self, objeto: Elemento):
        if self.contiene(objeto) == True:
            return self.lista.append(objeto)
        else:
            return
    def unir(self, conjunto):
        for i in range(len(conjunto)):
            if self.lista.contains(conjunto[i]):
                return self.lista
            else:
                self.lista.append(conjunto[i])
    def intersectar(self, conjunto1, conjunto2):
        interseccion = []
        for i in range(max(len(conjunto1), len(conjunto2))):
            if conjunto1.contains(conjunto2[i]):
                interseccion.append(conjunto2[i])
                return interseccion
            elif conjunto2.contains(conjunto1[i]):
                interseccion.append(conjunto1[i])
                return interseccion
            else:
                return interseccion
    def __str__(self) -> str:
        return f"{self.lista}"
