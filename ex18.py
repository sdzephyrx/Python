#def cria uma funcao para ser usada no codigo, é possivel infomar nos
#argumentos variaveis um entradas do console diretamente.
def print_2(arg1, arg2):
  print(f"Arg1: {arg1}, Arg2: {arg2}")

def print_1(arg1):
  print(f"Arg1: {arg1}")

def print_none():
  print("Nada!")
#usando o console para informar os argumentos
print_1(input("a: "))
print_2(input("a1: "), input("a2: "))
print_none()
