print('Sistema de Média Aluno')
print()
nome = (input('Coloque seu Nome '))
nota1 = float(input('Coloque sua primeira Nota! '))
nota2 = float(input('Coloque sua segunda Nota! '))

media = (nota1 + nota2) / 2

print(nome, 'A sua Média é:', media)

if media >= 6:
  print('Você foi Aprovado!')
else:
  print('Você foi Reprovado')


print('Obrigado por usar o Sistema de Média Aluno! :D') 
   