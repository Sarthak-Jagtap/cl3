import xmlrpc.client

# Connect to server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/RPC2")

try:
    num = int(input("Enter a number: "))
    result = proxy.calculate_factorial(num)
    print(f"Factorial of {num} is: {result}")

except Exception as e:
    print("Error:", e)
