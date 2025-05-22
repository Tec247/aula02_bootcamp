import math
# #### Inteiros (`int`)
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
result = numero1+numero2
print(f"O resultado da soma é: {result}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
CONST_NUM = 5
n = int(input("Digite um número: "))
valor2 = n % CONST_NUM
print(f"O resto da divisão pelo número {CONST_NUM} é {valor2}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
valor = numero1*numero2
print(f"O resultado da multiplicação de {numero1} X {numero2} = {valor} ")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
valor = num1//num2
print(f"o resultado da divisão inteira de {num1} / {num2} = {valor}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
num = int(input("Digite um número inteiro: "))
valor = num **2
print(f"O quadrado do número digitado é: {valor}")

#### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
valor = num1+num2
print(f"A adição de pontos flutuantes entre os números {num1} + {num2} = {valor}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
media = (num1+num2)/2
print(f"A média calculada dos dois números é: ({num1} + {num2}) / 2 = {media}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

base = float(input("Digite o valor do número da base: "))
expoente = float(input("Digite o valor do número do expoente: "))
valor = base**expoente
print(f"O resultado de {base}**{expoente} = {valor}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
PRIMEIRO_PARAMETRO = 1.8
SEGUNDO_PARAMETRO = 32
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
temperatura_fahrenheit = (temperatura_celsius*PRIMEIRO_PARAMETRO)+SEGUNDO_PARAMETRO
print(f"A temperatura {temperatura_celsius}ºC, convertido para Fahrenheit {temperatura_fahrenheit:.2f}ºF")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio do círculo: "))
area_circulo = math.pi * raio**2
print(f"A área do círculo referente ao raio de {raio} é de {area_circulo:.2f}") 

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

nome = input("Digite uma palavra: ")
palavra = nome.upper()
print(f"A palavra digitada foi {nome}, já convertendo todas as letras para maiúsculo fica: {palavra} ")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome = input("Digite seu nome completo: ")
nome_tratado = nome.lower()
print(f"Seu nome é: {nome} e nome tratado é {nome_tratado}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = input("Digite uma frase: ")
frase_tratada = frase.strip()
print(f"A frase tratada é: {frase_tratada}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input("Insira uma data no seguinte formato: dd/mm/aaaa: ")
data_tratada = data.split("/")
print(f"O dia digitado foi: {data_tratada[0]}")
print(f"O mês digitado foi: {data_tratada[1]}")
print(f"O ano digitado foi: {data_tratada[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

texto1 = input("Digite o primeiro texto: ")
texto2 = input("Digite o segundo texto: ")
print(f" A concatenação gerou o seguinte: {texto1} {texto2}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

valor1 = False
valor2 = False
resultado = valor1 and valor2
print(f"O resultado entre a operação de OR é: {resultado}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

valor1 = False
valor2 = True
resultado = valor1 or valor2
print(f"O resultado entre a operação de OR é: {resultado}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
valor1 = True
valor_not = not valor1
print(f"O valor negado é: {valor_not}")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

num1 = 22
num2 = 21
result_igualdade = (num1 == num2)
print(f"Resultado da igualdade é: {result_igualdade}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura


# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação