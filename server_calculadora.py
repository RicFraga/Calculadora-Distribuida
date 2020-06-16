"""
suma, resta, multiplicación, división, exponenciación, seno, coseno,
tangente, cotangente, secante, cosecante, log, raíz y uso de
paréntesis anidados.

"""

import numpy as np
from xmlrpc.server import SimpleXMLRPCServer
PUERTO = 8000

class RPC:
    _metodos = ['prefijo', 'infijo', 'posfijo',
                'infijo_a_posfijo' ,'evaluar_posfijo',
                'evaluar_prefijo']

    def __init__(self, direccion):
        self._servidor = SimpleXMLRPCServer(direccion, allow_none=True)

        for metodo in self._metodos:
            self._servidor.register_function(getattr(self, metodo))

    def infijo_a_posfijo(self, expresion):
        pila = []
        posfijo = ""
        numeros = '0123456789'
        especial = 'sctl'
        i = 0

        while(i < len(expresion)):
            char = expresion[i]

            # Si es un número
            if(char in numeros):
                posfijo = posfijo + char

            # Si es un paréntesis que abre
            elif(char == '('):
                pila.append('(')

            # Si es un paréntesis que cierra
            elif(char == ')'):

                # Buscas el paréntesis que abre
                aux = pila.pop()

                if(aux != '('):
                    posfijo = posfijo + aux

                while(aux != '('):
                    aux = pila.pop()
                    # No agregamos los (
                    if(aux != '('):
                        posfijo = posfijo + aux

            # Si es del tipo +-
            elif(char in '+-'):
                # Si la pila está vacía
                if(len(pila) == 0  or pila[-1] == '('):
                    pila.append(char)

                # Si la pila no está vacía
                else:
                    # Si el tope es de misma priori
                    if(pila[-1] in '+-'):
                        posfijo = posfijo + pila.pop()
                        pila.append(char)

                    # Si el tope es de mayor priori
                    elif(pila[-1] in '*/' or pila[-1] in '^'):
                        for i in range(len(pila)):
                            posfijo = posfijo + pila.pop()

                        pila.append(char)

            # Si es del tipo */
            elif(char in '*/'):
                # Si la pila está vacía
                if(len(pila) == 0 or pila[-1] == '('):
                    pila.append(char)

                # Si la pila no está vacía
                else:
                    # Si el tope es de misma priori
                    if(pila[-1] in '*/'):
                        posfijo = posfijo + pila.pop()
                        pila.append(char)

                    # Si el tope es de mayor priori
                    elif(pila[-1] in '^'):
                        for i in range(len(pila)):
                            posfijo = posfijo + pila.pop()

                        pila.append(char)

                    # Si el tope es de menor prioridad
                    elif(pila[-1] in '+-'):
                        pila.append(char)

            # Si es del tipo ^
            elif(char in '^' or pila[-1] == '('):
                # Si la pila está vacía
                if(len(pila) == 0):
                    pila.append(char)

                # Si la pila no está vacía
                else:
                    # Si el tope es de misma priori
                    if(pila[-1] in '^'):
                        posfijo = posfijo + pila.pop()
                        pila.append(char)

                    # Si el tope es de menor prioridad
                    elif(pila[-1] in '*/' or pila[-1] in '+-'):
                        pila.append(char)
            
            # Si es una funcion trigonometrica
            elif(char in especial):
                
                # Si es una funcion seno
                if(expresion[i:i+3] == 'sen'):
                    pila.append('sen')
                
                elif(expresion[i:i+3] == 'cos'):
                    pila.append('cos')

                elif(expresion[i:i+3] == 'tan'):
                    pila.append('tan')
                
                elif(expresion[i:i+3] == 'cot'):
                    pila.append('cot')
                
                elif(expresion[i:i+3] == 'sec'):
                    pila.append('sec')
                
                elif(expresion[i:i+3] == 'csc'):
                    pila.append('csc')
                
                elif(expresion[i:i+3] == 'log'):
                    pila.append('log')

                i = i + 2
            
            i = i +1
                
        # Si la pila no está vacía
        if(len(pila) > 0):
            for i in range(len(pila)):
                posfijo = posfijo + pila.pop()

        return posfijo


    def evaluar_posfijo(self, expresion):
        pila = []
        numeros = '0123456789'
        especial = 'sctl'
        i = 0

        while(i < len(expresion)):
        #for char in expresion:
            char = expresion[i]

            # Si encontramos un número
            if(char in numeros):
                pila.append(char)

            # Si encontramos un operador
            elif(char in '+-*/^'):
                aux1 = pila.pop()
                aux2 = pila.pop()

                if(char == '+'):
                    pila.append(float(aux1) + float(aux2))

                elif(char == '-'):
                    pila.append(float(aux2) - float(aux1))

                elif(char == '/'):
                    pila.append(float(aux2) / float(aux1))

                elif(char == '*'):
                    pila.append(float(aux2) * float(aux1))
            
            elif(char in especial):

                # Si es una funcion seno
                if(expresion[i:i+3] == 'sen'):
                    valor = float(pila.pop())
                    pila.append(np.sin(valor))
                
                elif(expresion[i:i+3] == 'cos'):
                    valor = float(pila.pop())
                    pila.append(np.cos(valor))

                elif(expresion[i:i+3] == 'tan'):
                    valor = float(pila.pop())
                    sen = np.sin(valor)
                    cos = np.cos(valor)
                    pila.append(sen / cos)
                
                elif(expresion[i:i+3] == 'cot'):
                    valor = float(pila.pop())
                    sen = np.sin(valor)
                    cos = np.cos(valor)
                    pila.append(cos / sen)
                
                elif(expresion[i:i+3] == 'sec'):
                    valor = float(pila.pop())
                    cos = np.cos(valor)
                    pila.append(1 / cos)
                
                elif(expresion[i:i+3] == 'csc'):
                    valor = float(pila.pop())
                    sen = np.sin(valor)
                    pila.append(1 / sen)
                
                elif(expresion[i:i+3] == 'log'):
                    valor = float(pila.pop())
                    pila.append(np.log10(valor))

                i = i + 2

            i = i + 1

        return pila.pop()
    
    def evaluar_prefijo(self, expresion):
        numeros = '0123456789'
        operadores = '+-*/^'
        pila = []

        # Recorremos la expresion al reves
        for char in expresion[::-1]:
            if(char in numeros):
                pila.append(char)

            elif(char in operadores):
                aux1 = pila.pop()
                aux2 = pila.pop()

                if(char == '+'):
                    pila.append(float(aux1) + float(aux2))
            
                elif(char == '-'):
                    pila.append(float(aux1) - float(aux2))

                elif(char == '*'):
                    pila.append(float(aux1) * float(aux2))

                elif(char == '/'):
                    pila.append(float(aux1) / float(aux2))

                elif(char == '^'):
                    pila.append(float(aux1) + float(aux2))

        return float(pila.pop())

    def prefijo(self, expresion):
        return self.evaluar_prefijo(expresion)

    def infijo(self, expresion):
        return self.evaluar_posfijo(self.infijo_a_posfijo(expresion))

    def posfijo(self, expresion):
        return self.evaluar_posfijo(expresion)

    def iniciar_servidor(self):
        self._servidor.serve_forever()

if __name__ == '__main__':
    rpc = RPC(('', PUERTO))
    print('Servidor iniciado en el puerto {}...'.format(PUERTO))
    rpc.iniciar_servidor()
