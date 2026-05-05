a = float(input("Entrer le premier nombre: "))
b = float(input("Entrer le deuxième nombre: "))

operation = input("Choisir (+, -, *, /): ")

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)
else:
    print("Opération non valide")