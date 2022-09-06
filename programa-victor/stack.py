class Stack:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """

    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items=[]

    def push(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)
        print("Texto ingresado exitosamente!")

    def pop(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            print("Elemento eliminado exitosamente")
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def is_empty(self):
        """ Devuelve True si la lista está vacía, False si no. """        
        if( self.items == [] ): 
            print("Pila actualmente vacía!")
            return True
        return False

    
    def longerText(self):
        """ Retorna el texto más largo de la pila """
        lt = max(self.items, key=len)
        print(lt)
        return lt
    
    def smallerText(self):
        """ Retorna el texto más pequeño de la pila """
        st = min(self.items, key=len)
        print(st)
        return st

    def printText(self, i):
        """ Imprime el texto en la posicion i de la pila """
        try:
            print(self.items[i])
        except IndexError:
            raise ValueError("Indice ingresado no es válido. Parte desde 0")
    
    def compareSizes(self, i, j):
        """ Retorna un número que representa la diferencia en tamaño de ambas palabras.
            i, j representan los indices de las palabras a comparar en la pila"""
        try:
            return abs(self.items[i] - self.items[j])
        except IndexError:
            raise ValueError("Indice ingresado no es válido. Parte desde 0")
    
    def printStack(self):
        print("Contenido actual de la pila")
        print(self.items)

