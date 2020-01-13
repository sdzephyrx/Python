#import da bibloteca sys para usaro argv
from sys import argv
#declaracao de variavel
script, filen =argv
#declaracao da variavel com a funcao open([arquivo]) para ler
#o arquivo
txt=open(filen)
#print do nome do arquivo informado no argv
print(f"arquivo {filen}:")
#print do conteudo do arquivo
print(txt.read())
#print
print("digite o arquivo novamente:")
#input do nome do arquivo(teoricamente tem que estar no
#mesmo diretorio)
filea=input("> ")
#le o arquivo
txta= open(filea)
#print do conteudo
print(txta.read())
