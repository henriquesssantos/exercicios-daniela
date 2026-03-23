# exercicio 1 
'''
moeda1 = int(input("digite a quantidade de moedas de 1 centavo:"))
moeda5 = int(input("digite a quantidade de moedas de 5 centavo:"))
moeda10 = int(input("digite a quantidade de moedas de 10 centavo:"))
moeda25 = int(input("digite a quantidade de moedas de 25 centavo:"))
moeda50 = int(input("digite a quantidade de moedas de 50 centavo:"))
moeda1Real = int(input("digite a quantidade de moedas de 1 real"))

total= (moeda1 * 0.01) + (moeda5 * 0.05) + (moeda10 * 0.1) + (moeda25 * 0.25) + (moeda50 * 0.50) + moeda1Real
print(f'o total de moedas em reais foi de {total}')
'''


#exercicio 2
'''
agua = 8/10
suco = 2/10

litrosSuco = float(input("digite quantos litros de suco você precisa:"))

quantidadeAgua = litrosSuco * 0.8
quantidadeSuco = litrosSuco * 0.2

print(f'A quantidade de agua necessária será de {quantidadeAgua}L, e de suco sera de {quantidadeSuco}L')
'''

#exercicio 3
'''
preco = float(input('digite o antigo preço do produto'))

desconto = preco * 0.1
precoNovo = preco - desconto

print(f'o novo preço é de R${precoNovo}')
'''

#exercicio 4
'''
SalarioFIxo = float(input('digite seu salario fixo:'))
vendasRealizadas = float(input('digite o valor vendido deste mes:'))

salarioFinal = ( vendasRealizadas * 0.4) + SalarioFIxo

print(f'Seu salario total foi de {salarioFinal}')
'''
#exercicio 5
'''
peso = float(input('digite seu peso atual:'))

pesoEngordar = (peso * 0.15) + peso
pesoEmagrecer = peso - (peso * 0.20) 

print(f'com sei peso atual sendo {peso}\n caso você engorde seu peso será de {pesoEngordar}\n caso emagreça seu peso será de {pesoEmagrecer}')
'''
#exercicio 6
'''
salarioMinino = float(input('digite o valor do salário minimo:'))
salarioFuncionario = float(input('digite o seu salario:'))

salarios = salarioFuncionario / salarioMinino
print(f'a quantidade de salarios minimos que você recebe é de {salarios}')
'''
#exercicio 7
'''
numero = int(input('de qual nunemo deseja saber a tabuada?'))
print(f'A tabuada de {numero} é:\n {numero * 1}\n{numero *2}\n{ numero *3}\n{ numero *4}\n{ numero *5}\n{ numero *6}\n{ numero *7}\n{ numero *8}\n{ numero *9}\n{ numero *10}')
'''
#exercicio 8
anoNascimento = int(input('digite o ano que você nasceu:'))
anoAtual = int(input('digite o ano atual:'))

idadeAnos = anoAtual - anoNascimento
print(f'sua idade em anos é:{idadeAnos}')

idadeMeses = idadeAnos * 12
print(f'sua idade em meses é de:{idadeMeses}')

idadeDias = idadeAnos * 365
print(f'Sua idade em dias é de:{idadeDias}')

idadeSemanas = idadeDias / 7
idadeSemanas = round(idadeSemanas, 1)
print(f'Sua idade em semanas é de:{idadeSemanas}')

#exercicio 9
'''
salarioJoao = 1200
c1 = 200
c2 = 120

c1Atrasada = (c1 * 0.02)+c1
C2Atrasada = (c2 * 0.02)+c2

print(f'recebendo o salario de {salarioJoao}, tendo o valor da conta 1 com o atraso sendo {c1Atrasada}\nTendo a conta 2 com o atraso sendo {C2Atrasada}\nO restante do salario sera de {salarioJoao - c1Atrasada - C2Atrasada} ')
'''