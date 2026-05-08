import Pyro4

def main():
    uri = input("Paste server URI: ")
    server = Pyro4.Proxy(uri)

    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    result = server.concatenate(str1, str2)
    print("Result:", result)

if __name__ == "__main__":
    main()
