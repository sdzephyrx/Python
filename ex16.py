from sys import argv

script, filename= argv

print("Vamos apagar o arquivo {filename}")
print("Aperte CTRL+C para cancelar ou ENTER para continuar:")
input("?")

print("Abrindo arquivo...")
#a opcao w é para abrir o arquivo no modo gravacao, o padrao é modo leitura
target= open(filename, 'w')

print("Truncate, adeus!")
#truncate apaga tudo do arquivo
target.truncate()

print("Populando o arquivo, escreva:")
line1= input("Line 1: ")
line2= input("Line 2: ")
line3= input("Line 3: ")

print("Escrevendo no arquivo...")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Feito, fechando o arquivo...")
#close fecha o arquivo lido pelo codigo
target.close()
