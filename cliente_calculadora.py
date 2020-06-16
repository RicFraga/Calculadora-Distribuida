from xmlrpc.client import ServerProxy
PUERTO = 8000

server = ServerProxy('http://localhost:' + str(PUERTO), allow_none=True)

while(True):
    print("¿Qué operación deseas realizar?")
    print("1.- Evaluar una expresión en notación prefija")
    print("2.- Evaluar una expresión en notación infija")
    print("3.- Evaluar una expresión en notación posfija")
    print("4.- Salir")

    respuesta = int(input())

    # Evaluar expresión prefija
    if(respuesta == 1):
        print("\nIngresa tu expresión: ")
        expresion = input()

        print("\nResultado de evaluar la expresión: ")
        print(str(server.prefijo(expresion)) + '\n')

    elif(respuesta == 2):
        print("\nIngresa tu expresión: ")
        expresion = input()

        print("\nResultado de evaluar la expresión: ")
        print(str(server.infijo(expresion)) + '\n')

    elif(respuesta == 3):
        print("\nIngresa tu expresión: ")
        expresion = input()

        print("\nResultado de evaluar la expresión: ")
        print(str(server.posfijo(expresion)) + '\n')

    elif(respuesta == 4):
        break

    else:
        print("\nIngresa una opción válida\n")
