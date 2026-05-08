from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Function class
class FactorialServer:
    def calculate_factorial(self, n):
        if n < 0:
            return "Error: Negative number not allowed"

        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Restrict path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(("localhost", 8000),
                        requestHandler=RequestHandler) as server:

    server.register_introspection_functions()
    server.register_instance(FactorialServer())

    print("Server started at port 8000...")
    server.serve_forever()
