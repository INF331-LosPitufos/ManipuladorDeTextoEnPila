from stack import Stack
from vista import Vista
import re
import logging

#Se crea un archivo que almacena la info de logging
logging.basicConfig(filename='infoLogging.log', filemode='w', level=logging.DEBUG, format='%(asctime)s %(message)s' )
#Se crea una pila vacía
s = Stack()
###### Ciclo principal del programa ######
salir = False
v = Vista()

while not salir:
    v.opcionesfun()
    op = input()

    if(op=="1"):
        s.printStack()
        
    elif(op=="2"):
        print("Escriba el texto a agregar en la pila: ")
        texto = input()
        s.push(texto)

    elif(op=="3"):
        if(not s.is_empty()):
            s.pop()

    elif(op=="4"):
        if(not s.is_empty()):
            s.longerText()

    elif(op=="5"):
        if(not s.is_empty()):
            s.smallerText()

    elif(op=="6"):
        if(not s.is_empty()):
            # Si el input ingresado no es un número
            # el programa lo indica y pide una nueva entrada
            s.printStack()
            print("Ingresa la posición del texto a imprimir")
            print("Nota que la posición parte desde 0")
            entradaInvalida = True
            while(entradaInvalida):
                i = input()
                if re.search('^[0-9]+$',i):
                    i = int(i)
                    if(i>=0 and i < s.stackSize()):
                        s.textInPosition(i)
                        entradaInvalida = False
                    else:
                        logging.info("Error: Debes ingresar un número válido!")
                        print("Error: Debes ingresar un número válido!")
                else:
                    logging.info("Error: Debes ingresar un número!")
                    print("Error: Debes ingresar un número!")
                

    elif(op=="7"):
        if(not s.is_empty()):
            s.printStack()
            print("Ingresa la posición de los textos a comparar")
            print("Nota que la posición parte desde 0")
            entradaInvalida = True
            while(entradaInvalida):
                print("Ingresa la posición del primer texto")
                logging.info("Opción 7 Ingresa la posición del primer texto")
                i = input()
                print("Ingresa la posición del segundo texto")
                logging.info("Opción 7 Ingresa la posición del segundo texto")
                j = input()
                if re.search('^[0-9]+$',i) and re.search('^[0-9]+$',j):
                    i = int(i)
                    j = int(j)
    
                    if((i>=0 and i < s.stackSize()) and (j>=0 and j < s.stackSize())):
                        delta = s.compareSizes(i,j)
                        entradaInvalida = False
                        #print(type(s.textInPosition(i)))
                        print("La palabra <<"+s.textInPosition(i) + ">> se diferencia de <<"+ s.textInPosition(j)+">> en " + str(delta) + " caracteres\n")
                    else:
                        logging.info("Error: Ambos números deben ser válidos!")
                        print("Error: Ambos números deben ser válidos!")
                else:
                    logging.info("Error: Debes ingresar solo números!")
                    print("Error: Debes ingresar solo números!")
            
    elif(op=="8"):
        print("Presione cualquier tecla para salir")
        logging.info("Opcion 8 Presione cualquier tecla para salir")
        op = input()
        print("Hasta pronto!")
        logging.info("Opcion se termina el programa")
        salir = True

    else:
        print("Error: Opción de menú no válida\n")
        logging.info("Error: Opción de menú no válida\n")
# Mostrar Menú de opciones

