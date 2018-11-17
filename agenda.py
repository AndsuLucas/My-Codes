# preciso arrumar uma forma de armazenar os dados.
agenda = dict()

def insert(dc):
    while True:

        data = input('insira a data de hoje!')
        dc[data] = input('Pode inserir seus compromissos/metas:')
        x = input('deseja continuar inserindo? [S/N]').upper()[0]
        if x == "N":
            break


def remove():
    print('caso não saiba a data, insira 0 para mostrar a agenda!')

    while True:
        x = input('quer remover algo certo?, vamos lá: insira a data da nota.')
        if x in agenda.keys():
            del agenda[x]
            print('Nota removida com sucesso!')
        else:
            print('Nota inexistente, favor repetir o processo.')

        funcao = input('Quer continuar ? [S/N]').upper()[0]
        if x == 0:
            mostrartudo(agenda)

        if funcao == 'N':
            break

def boasvindas():

    print('Bem vindo Anderson!')
    print('--------'*30)
    while True:
        senha = int(123)
        validacao = int(input('Insira sua senha:'))
        print('------------'*30)

        if validacao == senha:
            break

        print('Senha incorreta.')

def mostrartudo(dc):

    print(dc)



def mostrar(dc):
    while True:
        print('Caso não saiba a data, insira "0" para mostrar tudo.')

        x = input('insira a data da nota:')

        if x == 0:
            mostrartudo(agenda)
        else:
            print(f'{dc[x]}')

        funcao = input('Deseja acessar algo mais? [S/N]:').upper()[0]

        if funcao == 'N':
            break

boasvindas()

while True:
    acao = ''
    print('insira "ajuda" para mais informações:')
    funcao = input('insira o que quer fazer:')

    if funcao == 'ajuda':
        print("mostrar =  mostra uma notas.\n inserir = insere uma nota nova.\n remover = remove uma nota. \n modificar = modifica uma nota. \n mostrartudo = mostra todas as notas")
    else:
        if funcao == 'inserir':
            insert(agenda)
            funcao = 'x'
        else:
            if funcao == 'remover':
                remove()
            else:
                if funcao == 'mostrartudo':
                    mostrartudo(agenda)
                else:
                    if funcao == 'mostrar':
                        mostrar(agenda)








    acao = input('Quer fazer mais algo? [S/N]').upper()[0]

    if acao  == 'N':
        print('Volte sempre <3')
        break





























