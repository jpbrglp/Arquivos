import sys
def arquivos():
 mensagem = int(input("Você está em um programa que manipula arquivos. Digite 1 para ler o conteúdo de um arquivo no terminal, 2 para editar um arquivo no terminal, 3 para criar um arquivo e editá-lo no terminal e digite 4 duas vezes para encerrar o programa: "))
 entrada_do_arquivo = str(input("Digite o nome do arquivo e sua extensão: "))
 while mensagem != 0:
    mensagem == 1
    if mensagem == 1:
        with open(entrada_do_arquivo,"r") as arquivo:
            conteudo = arquivo.read()
        print(conteudo)
        break
    elif mensagem == 2:
        with open(entrada_do_arquivo,"a") as arquivo:
            conteudo = arquivo.write(f"\n{str(input("Digite o seu texto: "))}")
        break
    elif mensagem == 3:
        with open(entrada_do_arquivo,"w") as arquivo:
            conteudo = arquivo.write(str(input("Digite o seu texto: ")))
        break
    elif mensagem >= 4:
        sys.exit()
    continuar
arquivos()
continuar = str(input("Deseja continuar? "))
while continuar.lower() =="sim":
    arquivos()