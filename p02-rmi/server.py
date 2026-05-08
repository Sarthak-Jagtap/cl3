import Pyro4

@Pyro4.expose
class StringServer:
    def concatenate(self, str1, str2):
        return str1 + str2

def main():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()

    server = StringServer()
    uri = daemon.register(server)

    ns.register("string.concat", uri)

    print("Server is ready...")
    print("URI:", uri)

    daemon.requestLoop()

if __name__ == "__main__":
    main()
