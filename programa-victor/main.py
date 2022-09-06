from stack import Stack
from vista import Vista


#Se crea una pila vacía
s = Stack()
#print(s.is_empty())

###### Ciclo principal del programa ######
salir = False
v = Vista()

while not salir:
    v.opcionesfun()
    op = input()

    if(op=="1"):
        s.printStack()
        v.clear()
        
    elif(op=="2"):
        print("Escriba el texto a agregar en la pila: ")
        texto = input()
        s.push(texto)
        v.clear()

    elif(op=="3"):
        if(not s.is_empty()):
            s.pop()
            v.clear()

    elif(op=="4"):
        if(not s.is_empty()):
            s.longerText()
            v.clear()

    elif(op=="5"):
        if(not s.is_empty()):
            s.smallerText()
            v.clear()

    elif(op=="6"):
        if(not s.is_empty()):
            print("Ingresa la posición del texto a imprimir")
            print("Nota que la posición parte desde 0")
            i = input()
            s.printText(int(i))

    elif(op=="7"):
        s.printStack()
        if(not s.is_empty()):
            print("Ingresa la posición del primer texto")
            i = input()
            print("Ingresa la posición del segundo texto")
            j = input()
            s.compareSizes(i,j)
            
    elif(op=="8"):
        print("Presione cualquier tecla para salir")
        op = input()
        print("Hasta pronto!")
        salir = True

            
# Mostrar Menú de opciones

