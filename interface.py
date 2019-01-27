from bancodedados import (
	Agenda
)
interface_agenda = Agenda()
print('--------SEJA BEM VINDO!------')
print('Comandos: consultar, escrever, excluir, sair')
while True:
	comandos_agenda = str(input('Insira o comando: ')).lower()
	
	if comandos_agenda == 'consultar':
		interface_agenda.consultar()
	
	if comandos_agenda == 'escrever':
		interface_agenda.criar_registro()
	
	if comandos_agenda == 'excluir':
		interface_agenda.excluir_registro()
	
	if comandos_agenda == 'sair':
		print('Bye!')
		break			