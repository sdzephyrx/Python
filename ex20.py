from sys import argv
script, input_file= argv
#define a funcao para ler e mostrar o conteudo do arquivo
def print_all(f):
    print(f.read())
#define a funcao para mostrar uma linha especifica
def print_a_line(line_count, f):
    print(line_count,f.readline())
#define a funcao para voltar ao primeiro byte do conteudo do arquivo
def rewind(f):
    f.seek(0)
#variavel que recebe o conteudo do arquivo
current_file= open(input_file)

print("Primeiro o arquivo completo:\n")
print_all(current_file)

print("Voltando ao inicio do arquivo\n")
rewind(current_file)

print("Agora as 3 prmeiras linhas:\n")
current_line= 1
print_a_line(current_line, current_file)
current_line+=1
print_a_line(current_line, current_file)
current_line+=1
print_a_line(current_line, current_file)
