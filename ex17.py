from sys import argv
#import do comando exists da biblioteca os.path
from os.path import exists

script, from_file, to_file= argv

print(f"Copiando de {from_file} para {to_file}.")
#abrindo e armazenando o arquivo
in_file= open(from_file)
#lendo o conteudo e armazenando
in_data= in_file.read()

#O comando len() conta o tamanho em bytes
print(f"O arquivo {from_file} tem {len(in_data)} bytes.")
#o comando exists() realiza o teste se existe ou nao
print(f"O arquivo {to_file} existe? {exists(to_file)}")
print("Abort ? CTRL+C (sim), ENTER (não)")
input("? ")

out_file= open(to_file, 'w')
out_file.write(in_data)

print("Feito!")
out_file.close()
in_file.close()
