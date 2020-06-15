"""
suma, resta, multiplicación, división, exponenciación, seno, coseno,
tangente, cotangente, secante, cosecante, log, raíz y uso de
paréntesis anidados.

"""

from xmlrpc.server import SimpleXMLRPCServer
PUERTO = 8000

class RPC:
    _metodos = ['prefijo', 'infijo', 'posfijo']

    def __init__(self, direccion):
        self._servidor = SimpleXMLRPCServer(direccion, allow_none=True)

        for metodo in self._metodos:
            self._servidor.register_function(getattr(self, metodo))

    def prefijo(self, expresion):
        return('Evaluar expresion en prefijo {}'.format(expresion))

    def infijo(self, expresion):
        return('Evaluar expresion en infijo {}'.format(expresion))

    def posfijo(self, expresion):
        return('Evaluar expresion en posfijo {}'.format(expresion))

    def iniciar_servidor(self):
        self._servidor.serve_forever()

if __name__ == '__main__':
    rpc = RPC(('', PUERTO))
    print('Servidor iniciado en el puerto {}...'.format(PUERTO))
    rpc.iniciar_servidor()
    