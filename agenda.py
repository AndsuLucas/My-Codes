# preciso arrumar uma forma de armazenar os dados.
agenda = dict()
def insert(dc):
    while True:

        data = input('insira a data de hoje!')
        dc[data] = input('Pode inserir seus compromissos/metas:')
        x = input('deseja continuar? [S/N]').upper()[0]
        if x == "N":
            break


def remove():
    print('caso não saiba a data, insira 0 para mostrar a agenda!')
    while True:
        x = input('quer remover algo certo?, vamos lá: insira a data da nota.')
        if agenda[x] in agenda.keys():
            del agenda[x]
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



boasvindas()

while True:

    funcao = input('o que deseja fazer anderson:? (help = mostrar comandos)')
    if 'inserir' in funcao:
        insert(agenda)
        break
    while True:
        s = input('deseja continuar? [S/N]').upper()[0]

        if s == "S":
            funcao = 0
        else:
            break
#voltar aos comandos! preciso resolver isso para testar o comando de remoção!

















