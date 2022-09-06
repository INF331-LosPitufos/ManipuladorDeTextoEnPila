
import subprocess

class Vista:
    """
    Muestra el menú de opciones al usuario
    """
    saludoOpciones = "Presione el número de la opción deseada:\n "
    msgSaludo = "Bienvenido al manipulador de texto en pila!!\n"
    obs = "Obs: La pila comienza vacía"
    opciones = {
        "1": "1. Mostrar contenido de la pila",
        "2": "2. Agregar una palabra a la pila",
        "3": "3. Eliminar palabra más recientemente agregada",
        "4": "4. Ver la palabra más larga de la pila",
        "5": "5. Ver la palabra más corta de la pila",
        "6": "6. Imprimir el texto de una determinada posición de la pila",
        "7": "7. Comparar tamaños de 2 textos",
        "8": "8. Salir"
    }

    def __init__(self):
        """Imprime el menu"""
        print(self.msgSaludo +"\n" + self.obs)
        
    def opcionesfun(self):
        for op in self.opciones.values():
            print(op)
        print(self.saludoOpciones)

    def clear(self):
        print("Presione enter para volver al menu")
        input()
        subprocess.run(["clear"]) 

"""
Que permita almacenar un texto en una pila.
Que dé al usuario la posibilidad de:
Ver cuál es el texto más largo en la pila y el más corto.
Imprimir cualquier texto de la pila en cualquier momento.
Permitir comparar tamaños.
"""