#inicio

#definição de um módulo/procedimento/funcao
def verificacao(idd: int, nm: str):
    mensagem = ''
    if (idd>=18):
        mensagem += "Olá seja bem-vindo\n"
        if (nm=="Rafael"):
            mensagem += "Há quanto tempo, Rafael!?\n"
        else:
            mensagem += "Que bom conhecê-lo!\n"
    else:
        mensagem +="Você não tem idade suficiente para acessar.\n"
        if (idd>=10):
            mensagem += "Mas, você pode assistir ao Cartoon Network\n"
    return mensagem

soma=0
for i in range(2):
    nome = ""
    print("Informe o seu nome: ")
    nome = input()
    print("Informe a sua idade: ")
    idade = int(input())
    soma = soma + idade
    texto = verificacao(idade, nome)
    print(texto)

media = soma/2
print("Média de idades: ", media)
print("Tchau")
#fim