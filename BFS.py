class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.padre = None
        self.set_hijos(hijos)

    def set_hijos(self, hijos):
        self.hijos = hijos
        if self.hijos is not None:
            for hijo in hijos:
                hijo.padre = self

    def get_datos(self):
        return self.datos

    def get_padre(self):
        return self.padre

    def en_lista(self, lista_nodos):
        for nodo in lista_nodos:
            if self.igual(nodo):
                return True
        return False

    def igual(self, nodo):
        return self.get_datos() == nodo.get_datos()

    def set_padre(self, padre):
        self.padre = padre

    def __str__(self):
        return str(self.get_datos())
