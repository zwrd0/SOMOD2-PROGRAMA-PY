import time
import os
clear = lambda: os.system('cls')
def a():
	input("Clique Enter para continuar...")
	clear()

def b(x):
	input("Clique Enter para abrir a aplicação em questão! ")
	app = lambda: os.system(x)
	app()


def Menu():
	print("Módulo 2 - Comandos Básicos do MSDOS")
	time.sleep(1)
	print("Trabalho Realizado por Miguel Figueiredo nº17, 10ºH")
	a()
	for i in range(1, 6):
		print("Começando em", i)
		time.sleep(1)
	clear()

Menu()

print("appwiz.cpl")
print("Abre a aba de controlo de funcionalidades do windows")
b("appwiz.cpl")
a()

print("compmgmt.msc")
print("Abre a aba de gestão de computadores do windows")
b("compmgmt.msc")
a()

print("calc")
print("Abre a calculadora")
b("calc")
a()

print("control folders")
print("Abre as definições do Explorador de Ficheiros")
b("control folders")
a()

print("control")
print("Abre todos os paines de controlo")
b("control")
a()

print("control userpasswords")
print("Abre a aba de alteração de informações da conta")
b("control userpasswords")
a()

print("control netconnections")
print("Abre as definições de rede")
b("control netconnections")
a()

print("firewall.cpl")
print("Abre a firewall do windows")
b("firewall.cpl")
a()

print("inetcpl.cpl")
print("Abre as propriedades da internet")
b("inetcpl.cpl")
a()

print("dxdiag")
print("Abre a ferramenta do DirectX")
b("dxdiag")
a()

print("msconfig")
print("Abre a aba de resolução de problemas no arranque do Windows")
b("msconfig")
a()

print("services.msc")
print("Abre o local de gestão de serviços do Windows")
b("services.msc")
a()

print("sysdm.cpl")
print("Abre uma aplicação para carregar propriedades do sistema que não foram carregadas e vice-versa")
b("sysdm.cpl")
a()

print("sysedit")
print("Abre um editor de texte ASCII do Windows")
print("O comando foi descontinuado.")
a()

print("Taskmgr")
print("Abre o gestor de tarefas")
b("Taskmgr")
a()

print("Wiaacmgr")
print("Abre o portal de utlização de scanners, câmeras e equipamentos similares")
b("Wiaacmgr")
a()

print("winver")
print("Abre a aba com informações sobre o Windows")
b("winver")
a()

print("wscui.cp")
print("Abre a aba de resolução de problemas")
print("O comando foi descontinuado.")
a()


print("Fim da apresentação! (:\n")
time.sleep(4)
