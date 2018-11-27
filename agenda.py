def ajuda():
    print('Acessar,Resetar,Escrever,Mostrar,Sair:')


def sep():
    print('-'*30)


class Agenda(object):

    def __init__(self):

        self.cont = 0
        self.agenda  = open('agenda.txt', 'r')
        print(self.agenda.read())
        self.agenda.close()

    def escrever(self):

        self.agenda = open('agenda.txt', 'a')
        self.data = input('Insira a data:')
        self.conteudo = input('Insira o conteúdo:')

        self.agenda.write(f'\n{self.data}: {self.conteudo}')

        self.agenda.close()

    def acessar(self):

        self.agenda = open('agenda.txt', 'r')
        dx = input('insira a data:')
        sep()
        for d in self.agenda:

            if dx in d:

                self.cont += 1

                sep()
                print(f'Conteúdo encontrado:\n{d}')
                sep()

        print(f'{self.cont} Notas encontradas.')
        self.agenda.close()

    def resetar(self):

         while True:

            funcao = input('Deseja mesmo resetar a agenda? [S/N]').upper()[0]

            if funcao == "N" or funcao == "S":
                break
         if funcao == 'S':
            self.agenda = open('agenda.txt', 'w')
            self.agenda.close()
    def mostrar(self):

        self.agenda = open('agenda.txt', 'r')
        print(self.agenda.read())
        self.agenda.close()

#estruturando a agenda no terminal
a = Agenda()
sep()
ajuda()
sep()
while True:

    f = input('insira o que deseja fazer:').lower()

    if (f == 'acessar'):

        a.acessar()

    elif(f == 'escrever'):

        a.escrever()

    elif(f == 'mostrar'):

        a.mostrar()

    elif(f == 'resetar'):

        a.resetar()
    elif(f == 'sair'):
        break
    
    else:
        print('Função inválida')

    pergunta = input('\nQuer continuar? [N/S]').upper()[0]

    if (pergunta == 'N'):
        break

