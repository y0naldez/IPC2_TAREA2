
class Nodo():
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaCDoblementeEnlazada():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    
    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False

    
    def agregar_final(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo 
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.__unir_nodos()

    def agregar_inicio(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unir_nodos()
    
    def __unir_nodos(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero


    def recorrer_inicio(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def recorrer_fin(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior
            if aux == self.ultimo:
                break

    def buscar(self,dato):
        aux = self.primero
        while aux:
            if(aux.dato == dato):
                print(" ********* BUSQUEDA ************ ")
                print("ACTUAL" , aux.dato)
                print("SIGUIENTE" , aux.siguiente.dato)
                print("ANTERIOR" , aux.anterior.dato)
            if (aux.siguiente == self.primero):
                return
            aux = aux.siguiente
               


listaDoble = ListaCDoblementeEnlazada()
listaDoble.agregar_final(17)
listaDoble.agregar_final(30)
listaDoble.agregar_final(13)
listaDoble.agregar_final(7)
listaDoble.agregar_final(31)
listaDoble.recorrer_inicio()
nBuscar = int(input("Ingrese un numero: "))
listaDoble.buscar(nBuscar)


