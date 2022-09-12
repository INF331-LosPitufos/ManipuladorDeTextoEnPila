import logging

class Stack:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """

    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        logging.info("Se crea una pila vacía")
        print("Se ha creado una pila vacía")
        self.items=[]

    def push(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)
        logging.info("Texto %s ingresado exitosamente!",x )
        print("Texto ingresado exitosamente!")

    def pop(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            print("Elemento eliminado exitosamente")
            n = len(self.items)
            logging.info("Elemento %s eliminado exitosamente", self.items[n-1])
            return self.items.pop()
        except IndexError:
            logging.info("La pila está vacía")
            raise ValueError("La pila está vacía")

    def is_empty(self):
        """ Devuelve True si la lista está vacía, False si no. """        
        if( self.items == [] ): 
            logging.info("Pila actualmente vacía!")
            print("Pila actualmente vacía!")
            return True
        return False

    
    def longerText(self):
        """ Retorna el texto más largo de la pila """
        lt = max(self.items, key=len)
        logging.info("El texto mas largo de la pila es %s",lt)
        print(lt)
        return lt
    
    def smallerText(self):
        """ Retorna el texto más pequeño de la pila """
        st = min(self.items, key=len)
        logging.info("El texto mas largo de la pila es %s",st)
        print("El texto mas largo de la pila es %s",st)
        return st

    def textInPosition(self, i):
        """ Imprime el texto en la posicion i de la pila """
        try:
            logging.info("retorna el item en la posicion "+str(i))
            return self.items[int(i)]
        except IndexError:
            logging.info("Indice ingresado no es válido. Parte desde 0")
            raise ValueError("Indice ingresado no es válido. Parte desde 0")
    
    def compareSizes(self, i, j):
        """ Retorna un número que representa la diferencia en tamaño de ambas palabras.
            i, j representan los indices de las palabras a comparar en la pila"""
        try:
            logging.info("se retorna la diferencia en el numero de caracteres")
            return abs(len(self.items[i]) - len(self.items[j]))
        except IndexError:
            logging.info("Indices ingresados para comparar tamaños no son válidos")
            raise ValueError("Indices ingresados para comparar tamaños no son válidos")
    
    def printStack(self):
        logging.info("Contenido actual de la pila")
        logging.info(self.items)
        print("Contenido actual de la pila")
        print(self.items)

    def stackSize(self):
        """Funcion retorna el número de objetos en pila"""
        n = len(self.items)
        logging.info("El numero de objetos en la pila es ",n)
        print("El numero de objetos en la pila es ",n)
        return n