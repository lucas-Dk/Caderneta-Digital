import time

#Carregamento do programa
def iniciacao():
  print('\033[32mIniciando...\033[m')
  time.sleep(3)
  print('\033[32mCarregado\n\n\033[m')
#Carregamento inicial
def nome_inicial():
  print('\033[1;31m-=\033[m' * 20)
  print('           \033[1;32mCaderneta Digital\033[m')
  print('\033[1;31m-=\033[m' * 20, '\n')

#Resposta para sexo feminino
def feminino():
  if media >=7.0:
    print('\nA aluna {} foi \033[1;32maprovada\033[m'.format(nome))
  else:
    print('\nA aluna {} foi \033[1;31mreprovada\033[m'.format(nome))

#Resposta para sexo masculino
def masculino():
  if media >=7.0:
    print('\nO aluno {} foi \033[1;32maprovado\033[m'.format(nome))
  else:
    print('\nO aluno {} foi \033[1;31mreprovado\033[m'.format(nome))
#Chamando o carregamento do programa
iniciacao()

#Chamando a função do início
nome_inicial()

#Lista que será preenchida com as notas digitadas pelo usuário
notas = []
#Variaveis para cálculo
i = 1
soma = 0
#Entrada de dados do usuário
nome = str(input('Digite o nome do aluno: ')).capitalize().strip()
quant = int(input('\nQuantas notas serão: '))
sexo = str(input('\nQual o sexo do aluno [M/F]: ')).upper()[0]

#Validação do sexo do aluno
while sexo.strip() not in 'M' and sexo.strip() not in 'F':
  sexo = str(input('\n\033[1;31mSexo inválido!\033[m Qual o sexo do aluno [M/F]: ')).upper()[0]
  if sexo.strip() in 'M' and sexo.strip() in 'F':
    break

#Repetira a entrada pelo número de notas
while i <= quant:
    nota = float(input('\nInforme a {}ª nota do aluno: '.format(i)))
    notas.append(nota)
    i = i + 1
#Somará cada nota da lista
for x in notas:
    soma = soma + x
#Fará a media das notas da lista
media = soma / quant
#Saida de dados
print('\nEssas são as suas notas: \033[1;4;96m{}\033[m\n'.format(notas))
print('\nEssa é sua média: \033[1;33m{:.1f}\033[m'.format(media))

#Pergunta se quer saber se foi aprovado ou reprovado
ap_rp = str(input('\033[1;4mA\033[m ->  Aprovado \033[1;4mR\033[m ->  reprovado (x para sair): ')).upper()[0]

#Pergunta novamente caso as respostas não estiver de acordo
while ap_rp not in 'S' and ap_rp not in 'N' and ap_rp not in 'X':
  print('\n\033[1;31mOpção Inválida!\033[m')
  ap_rp = str(input('\033[1;4mA\033[m ->  Aprovado \033[1;4mR\033[m ->  reprovado (x para sair): ')).upper()[0]

#Saída de dados
if ap_rp in 'S':
  if sexo.strip() in 'F':
      print('Verificando...')
      time.sleep(1)
      print('\nComparando nota com a média...')
      time.sleep(1)
      print('\nObtendo resultado...')
      time.sleep(3)
      print('\nAqui está o resultado:\n')
      feminino()
  elif sexo.strip() in 'M':
      print('Verificando...')
      time.sleep(1)
      print('\nComparando nota com a média...')
      time.sleep(1)
      print('\nObtendo resultado...')
      time.sleep(3)
      print('\nAqui está o resultado:\n')
      masculino()
elif ap_rp in 'N':
  print('\nOk, você escolheu não saber!')

elif ap_rp in 'X':
  print('\n\033[1;31mEncerrando...\033[m')
  time.sleep(2)
  print('\nVocê digitou \033[1;4mX\033[m e saiu do programa')
