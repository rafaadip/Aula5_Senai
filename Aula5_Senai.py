# text = "Ola Mundo"
# comprimento = len(text)
# print(comprimento)

# x = "Guarulhos"
# tipo = type(x)
# print(tipo)

# x = input("Digite um número, texto ou qualquer coisa: ")
# tipo = type(x)
# print(tipo)

# n = "1"
# x = int(n)
# print(x+1)

# n="1.2"
# x=float(n)
# print=(x+8)

# str char
# n1 = 250
# c = str(n1)
# print(c, "Olá Mundo")

# text="Boa Tarde"
# lista = list(text)
# print(lista[0])

#Tuplas são dados que não podem ser alterados "Constantes"
#Nesse exemplo, o valor de list pode mudar, porem o list 2 nunca vai mudar.

# list = input("Digite aqui qualquer coisa: ")
# list2 = tuple(list)
# print(list2)

# # Range cria uma contagem, nesse exemplo a contagem vai de 1 até 10
# numeros = range(1,11,2) #o primeiro número dentro do parenteses é o ponto de partida, o segundo é o ponto de chegada e o terceiro é número de casas para pular, intervalo
# print(numeros)

# list = [1,2,3,4,5]
# soma = sum(list)
# print(soma)~

#Encontra o valor maximo e o valor minimo
# numeros = [5, 7, 9, 0, 2, 4]
# minimo = min(numeros)
# maximo = max(numeros)
# print("O número maximo é:", maximo , "e o número minímo é:",minimo)

# list = ["b", "d", "e","f"]
# list2 = sorted(list)
# print(list)

### Exercício 1: Escreva um programa que use a função range() para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.
# numeros = range(2,21,2)
# for i in numeros:
#        print(i)

### Exercício 2: Escreva um programa que use a função range() para gerar os múltiplos de 5 de 5 a 50 e, em seguida, calcule e imprima a soma desses múltiplos.
# numeros = range(5,51,5)
# for i in numeros:
#     print(i)

### Exercício 3: Escreva um programa que use a função `type()` para verificar o tipo de uma variável.
# msg = input("Digite aqui alguma coisa, ou um número: ")
# tipo = type(msg)
# print(tipo)

### Exercício 4: Escreva um programa que use a função print() para imprimir uma mensagem de saudação personalizada, incluindo o nome do usuário.
# nome = input("User: ")
# msg = nome+(", seja bem vindo!")
# print(msg)

### Exercício 5: Escreva um programa que use a função range() para gerar os números ímpares de 1 a 10 e, em seguida, calcule e imprima a média desses números.
# n = range(1,11)
# print(list(n))
# print(sum(n)/10)

### Novos exercicios
### Exercício 1: Escreva um programa que use a função range() para gerar os números pares de 2 a 20 e, em seguida, calcule e imprima a média desses números.
# n = range(2,21,2)
# print(sum(n)/10)

### Exercício 2: Escreva um programa que imprima os números pares de 2 a 20.
# n = range(2,21,2)
# print(list(n))

### Exercício 3: Escreva um programa que calcule a soma dos números de 1 a 100.
# numeros = range(1,101)
# print(sum(numeros))
### Exercício 3.1: Outra maneira de fazer, porem de uma forma mais eficiente quando pensamos em enconomizar recursos computacionais, loop for.
# soma = 0 
# for i in range(1, 101):
#     soma += i
# print("A soma dos números de 1 a 100 é,", soma)
### Exercício 4: Escreva um programa que imprima os múltiplos de 5 de 5 a 50.
# numeros = range(5,51,5)
# print(list(numeros))
### Exercício 4.1
# print("Multiplos de 5 de 5 a 50:")
# for numeros in range(5,51,5):
#     print(numeros)

