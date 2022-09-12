from ast import Try
import datetime

def comparador(s1, s2):
    if len(s1) == len(s2):
        return "same"
    elif len(s1) > len(s2):
        return 1
    else:
        return 2

text_stack = []
funcionamiento = True
f = open("logs.log", "a")
print("-------- Manipulador y Visor de Texto --------")
print("- Eliga una opción - \n - 1 - Agregar Texto. \n - 2 - Visualizar Textos.\n - 3 - Comparar Textos.\n - 4 - Ver Textos más Largos y más Cortos.\n")
print("- En cualquier momento puede usar el comando 'exit()' para retroceder o salir del programa.")

while funcionamiento:
    #print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")

    opcion = str(input("Ingrese Opción: "))

    if opcion == "1":
        texto = input("Ingrese Texto: ")
        if texto == "exit()":
            print("- Cerrando Programa -")
            f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Modo {opcion} | Entrada {texto} Salida y Cierre de Programa\n")
            break
        text_stack.append(texto)
        f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Modo {opcion} | Entrada {texto}, Añadido a Pila\n")

    elif opcion == "2":
        i = 0
        while i < len(text_stack):
            print(f"{i} - {text_stack[i]}")
            i += 1
        f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Entrada {opcion} | \n")

    elif opcion == "3":
        print("-------- Comparar Tamaños--------")
        print("- Ingrese el numero de los textos a comparar, solo se puede comparar de a 2 textos -")
        peticion1 = True
        peticion2 = True
        breaker = False
        while peticion1:
            p1 = input("- Texto 1: ")
            try:
                if int(p1) < 0 or int(p1) >= len(text_stack):
                    print("- Ha ingresado una opción invalida, por favor vuelva a intentarlo -")
                    f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Modo {opcion} | Entrada {p1}, Error de Indice fuera de Limites\n")
                else:
                    peticion1 = False
            except:
                if p1 == "exit()":
                    print("- Cerrando Programa -")
                    peticion1 = False
                    peticion2 = False
                    breaker = True
                    f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Entrada {opcion} | Salida y Cierre de Programa\n")
                else:
                    print("- Ha ingresado una opción invalida, por favor vuelva a intentarlo -")
                    f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Modo {opcion} | Entrada {p1}, Error de Entrada Erronea\n")

        while peticion2:
            p2 = input("- Texto 2: ")
            try:
                if int(p2) < 0 or int(p2) >= len(text_stack):
                    print("- Ha ingresado una opción invalida, por favor vuelva a intentarlo -")
                    f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Modo {opcion} | Entrada {p2}, Error de Indice fuera de Limites\n")
                else:
                    peticion2 = False
            except:
                if p2 == "exit()":
                    print("- Cerrando Programa -")
                    peticion2 = False
                    breaker = True
                    f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Entrada {opcion} | Salida y Cierre de Programa\n")
                else:
                    print("- Ha ingresado una opción invalida, por favor vuelva a intentarlo -")
                    f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Modo {opcion} | Entrada {p2}, Error de Entrada Erronea\n")
        
        if breaker: break
        else:
            comparar = comparador(text_stack[int(p1)], text_stack[int(p2)])
            if comparar == "same":
                print("- Ambos textos tienen el mismo tamaño -")
                f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Modo {opcion} | Entrada_1 {p1}, Entrada_2 {p2}, Resultado: Mismo Tamaño\n")
            elif comparar == 1:
                print("- El 1er texto es más largo que el segundo -")
                f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Modo {opcion} | Entrada_1 {p1}, Entrada_2 {p2}, Resultado: 1er Texto más largo\n")
            else:
                print("- El 2do texto es más largo que el primero -")
                f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Modo {opcion} | Entrada_1 {p1}, Entrada_2 {p2}, Resultado: 2do Texto más largo\n")
                


    elif opcion == "4":
        #Texto más largo y más corto
        if len(text_stack) > 0:
            print(f"- Texto más largo: {sorted(text_stack)[-1]}")
            print(f"- Texto más corto: {sorted(text_stack)[0]}")
            f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Modo {opcion} | Resultado: Texto Largo = {text_stack.sort()}\n")
            f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Modo {opcion} | Resultado: Texto Corto = {text_stack.sort()}\n")
        else:
            print("- El Stack de Textos está vacío, ingrese textos para poder obtener el texto más largo y el más corto -")
            f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Modo {opcion} | Resultado: No hay textos en pila para separar.\n")

        

    elif opcion == "exit()":
        print("- Cerrando Programa -")
        f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Entrada {opcion} | Salida y Cierre de Progrmaa\n")
        break

    else:
        #Mensaje de error por mal input.
        print("- Ha ingresado una opción invalida, por favor vuelva a intentarlo -")
        f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Info: Entrada {opcion} | Error de Entrada Erronea\n")
        

f.close()