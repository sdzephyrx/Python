from sys import argv
from os.path import exists

script, from_file, to_file= argv

print("Copiando de {from_file} para {to_file}.")
in_file= open(from_file)
in_data= in_file.read()

print("O arquivo {from_file} tem {len(indata)} bytes.")
print("O arquivo {to_file} existe? {exists(to_file)}")
print("Abort ? CTRL+C (sim), ENTER (não)")
input("? ")

out_file= open(to_file, 'w')
out_file.write(in_data)

print("Feito!")
out_file.close()
in_file.close()
