def add(a, b):
    print(f"Adicao de {a} + {b}:\n")
    return a+b

def subtract(a ,b):
    print(f"Subtracao de {a} - {b}:\n")
    return a-b

def multiply(a, b):
    print(f"Multiplicacao de {a} * {b}:\n")
    return a*b

def division(a, b):
    print(f"Divisao de {a} / {b}:\n")
    return a/b

print ("Calculando:\n")

age=subtract(2020, 1993)
altura=multiply(10,0.174)
peso=add(22, 40.5)
qi=division(200, 2)

print(f"Idade: {age}\nAltura: {altura}\nPeso: {peso}\nQI: {qi}\n")
