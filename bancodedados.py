import mysql.connector

conexao_banco_de_dados = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='agenda_db'
)

cursor_banco_de_dados = conexao_banco_de_dados.cursor()


class Agenda(object):
    def __init__(self):
        cursor_banco_de_dados.execute('USE agenda_db')

    def criar_registro(self):
        assunto = str(input('Insira o assunto: '))
        data = str(input('Insira a data: '))
        conteudo = str(input(' Insira o conteudo: '))

        cursor_banco_de_dados.execute('''
			INSERT INTO agenda (assunto, data, conteudo)
			VALUES ('{}','{}','{}')
		'''.format(assunto, data, conteudo))

    def salvar_alteracoes(self):
        self.pergunta = input('Deseja salvar as alterações ? [S/N]').upper()[0]
        if self.pergunta == 'S':
            conexao_banco_de_dados.commit()
            print('Processo efetuado com êxito.')
        else:
            conexao_banco_de_dados.rollback()
            print('Processo Cancelado.')

    def consultar(self):
        print('Consultar todos os registros: -a')
        print('Consultar registro específico: -e')
        acao = input('\n Ação: ').lower()

        if acao == '-a':
            contador = 0
            cursor_banco_de_dados.execute('SELECT * FROM agenda')
            for registro in cursor_banco_de_dados:
                contador += 1
                print('-'*30)
                print('Assunto: {}'.format(registro[0]))
                print('Data: {}'.format(registro[1]))
                print('Conteudo: {}'.format(registro[2]))
                print('ID do registro: {}'.format(registro[3]))
                print('-'*30)
            print('\n')
            print(f'{contador} registros encontrados.')
        if acao == '-e':
            contador = 0

            campo = input(
                '''Por qual campo deseja filtrar os registros?[id,assunto,data]'''
            ).lower()
            conteudo = input('Insira o conteudo do campo:')

            cursor_banco_de_dados.execute('''
				SELECT * FROM agenda
				WHERE {} = '{}'	
			'''.format(campo, conteudo))

            for registro in cursor_banco_de_dados:
                contador += 1
                print('-'*30)
                print('Assunto: {}'.format(registro[0]))
                print('Data: {}'.format(registro[1]))
                print('Conteudo: {}'.format(registro[2]))
                print('ID do registro: {}'.format(registro[3]))
                print('-'*30)
            print(f'{contador} registros encontrados.')

    def excluir_registro(self):
        registro = str(
            input('Por favor insira o ID do registro que deseja deletar.'))
        cursor_banco_de_dados.execute('''
	   		DELETE FROM agenda
			WHERE id = '{}'
	   '''.format(registro))
