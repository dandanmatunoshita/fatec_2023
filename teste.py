#a = 120
#b = 18
#brasil = a + b
#print("o resultado da variavel é =", brasil)

#soma = 4 + 6
#div = 20 / 4
#print(soma)
#print(div)


#a = input("digite um valor de A: ")
#b = input("digite um valor de B: ")

#print("A soma de A + B é: ", int(a) + int(b))

#CALCULADORA DE IMC

#entrada dde dados
peso = input("Digite seu peso: ")
altura = input("Digite sua altura: ")

#processamento
imc = float(peso) / float(altura) ** 2

print(f'Seu imc é de: {imc:.2f}')

if imc <= 18.5:
    print("Abaixo do peso")
elif imc > 18.5 and imc <= 24.9:
    print("peso normal")
elif imc > 24.9 and imc <= 29.9:
    print("Excesso de peso")
elif imc > 29.9 and imc <= 34.9:
    print("Obesidade classe 1")
elif imc > 34.9 and imc <= 39.9:
    print("Obesidade classe 2")
else:
    print("Obesidade classe 3")