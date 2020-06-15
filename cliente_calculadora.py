from xmlrpc.client import ServerProxy
PUERTO = 8000

server = ServerProxy('http://localhost:' + str(PUERTO), allow_none=True)

print(server.prefijo('Expresion en prefijo xd'))
print(server.infijo('Expresion en infijo xd'))
print(server.posfijo('Expresion en posfijo xd'))