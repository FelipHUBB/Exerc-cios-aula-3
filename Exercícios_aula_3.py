#1 Simulação de Treinamento
"""
Crie um programa que simule 10 épocas de treinamento de uma IA.

O programa deverá mostrar:

Treinando época 1
Treinando época 2
...
Treinando época 10
Utilize for e range().
"""
"""
for epoca in range(1, 11):
    print(f"Treinando época {epoca}")
"""
#2 Dados de Sensores
"""
Considere:

temperaturas = [22.5, 24.8, 27.1, 23.9, 26.5]
Percorra a lista utilizando for e exiba:

Temperatura registrada: 22.5°C
Temperatura registrada: 24.8°C
...
"""
"""
temperaturas = [22.5, 24.8, 27.1, 23.9, 26.5]

for temperatura in temperaturas:
    print(f"Temperatura registrada: {temperatura}°C")
"""
#3 Detectando Temperaturas Altas
"""
Utilize:

temperaturas = [22, 25, 31, 28, 35, 24]
Percorra os valores.

Quando a temperatura for maior que 30, exiba:

ALERTA: temperatura elevada!
Caso contrário, exiba a temperatura normalmente.
"""
"""
temperaturas = [22, 25, 31, 28, 35, 24]

for temperatura in temperaturas:

    if temperatura > 30:
        print(f"{temperatura} ALERTA: temperatura elevada!")
    else:
        print(temperatura)
"""

#4  Classificação de Confiança
"""
Considere:

confiancas = [0.95, 0.65, 0.34, 0.82, 0.71]
Para cada valor:

confiança maior ou igual a 0.8: "Alta confiança"
confiança entre 0.5 e 0.79: "Confiança média"
confiança abaixo de 0.5: "Baixa confiança"
"""
"""
confiancas = [0.95, 0.65, 0.34, 0.82, 0.71]

for confianca in confiancas:

    if confianca >= 0.8:
        print(f"{confianca} → Alta confiança")
    elif confianca >= 0.5 and confianca <= 0.79:
        print(f"{confianca} → Confiança média")
    else:
        print(f"{confianca} → Baixa confiança")
"""
#5Contando Classificações
"""
Considere as previsões:

previsoes = [
    "gato",
    "cachorro",
    "gato",
    "pássaro",
    "gato",
    "cachorro"
]
Crie um programa que conte quantas vezes "gato" aparece.

Resultado esperado:

Gatos detectados: 3
"""
"""
previsoes = [
    "gato",
        "cachorro",
        "gato",
        "pássaro",
        "gato",
        "cachorro"
]

quantidade_gatos = 0

for previsao in previsoes:

    if previsao == "gato":
        quantidade_gatos += 1

print(f"Gatos detectados: {quantidade_gatos}")
"""
#6 Média dos Dados
"""
Considere:

dados = [10, 15, 20, 25, 30]
Utilizando um for:

some todos os valores;
calcule a média;
exiba o resultado.
Evite utilizar sum() neste exercício.
"""
"""
dados = [10, 15, 20, 25, 30]

soma = 0

for dado in dados:
    soma += dado

media = soma / len(dados)

print(f"Média: {media}")
"""
#7 Processamento de Texto
"""
Peça ao usuário uma frase.

Utilizando for, conte quantas vezes a letra "a" aparece.

Exemplo:

Digite uma frase: Inteligência Artificial

Quantidade de letras 'a': 3
Considere tanto "a" quanto "A".
"""
"""
texto = input("Escreva uma frase: ")

quantidade = 0

for letra in texto:

    if letra == "a" or letra == "A":
        quantidade += 1

print(f"A letra 'a ou (A)' apareceu {quantidade} vezes.")
"""
#8 Ignorando Dados Inválidos
"""
Considere:

dados = [12, 15, None, 18, None, 21]
Utilizando continue, ignore os valores None e exiba apenas os números válidos.
"""
"""
dados = [12, 15, None, 18, None, 21]

for dado in dados:

    if dado is None:
        continue

    print(dado)
"""
#9 Analisando Previsões
"""
Considere:

previsoes = [
    0.92,
    0.84,
    0.35,
    0.76,
    0.28,
    0.95
]
Crie um programa que mostre cada previsão.

Entretanto, se encontrar uma confiança menor que 0.30, interrompa o processamento utilizando break.
"""
"""
previsoes = [
    0.92,
    0.84,
    0.35,
    0.76,
    0.28,
    0.95
]

for previsao in previsoes:

    if previsao < 0.30:
        print("Erro! Previsão < 0.30")
        break

    print(f"Previsão: {previsao}")
"""
#10 Matriz de Pixels
"""
Considere a seguinte representação simplificada de uma imagem:

imagem = [
    [0, 255, 0],
    [255, 255, 0],
    [0, 0, 255]
]
Utilizando dois for aninhados, exiba:

0 255 0
255 255 0
0 0 255
"""
"""
imagem = [
    [0, 255, 0],
    [255, 255, 0],
    [0, 0, 255]
]

for linha in imagem:

    for pixel in linha:
        print(pixel, end=" ")

    print()
"""
#11 Contador de Classes
"""
Considere:

previsoes = [
    "gato",
    "cachorro",
    "gato",
    "gato",
    "cachorro",
    "pássaro",
    "gato"
]
Crie um programa que conte separadamente:

Gatos: 4
Cachorros: 2
Pássaros: 1
Utilize variáveis contadoras e estruturas condicionais.
"""
"""
previsoes = [
    "gato",
    "cachorro",
    "gato",
    "gato",
    "cachorro",
    "pássaro",
    "gato"
]

quantidade_gatos = 0
quantidade_cachorros = 0
quantidade_passaros = 0

for previsao in previsoes:

    if previsao == "gato":
        quantidade_gatos += 1

print(f"Quantidade de gatos detectados: {quantidade_gatos}")
    
    if previsao == "cachorro":
            quantidade_cachorro += 1

print(f"Quantidade de cachorros detectados: {quantidade_cachorros}")

    if previsao == "pássaro":
                quantidade_passaros += 1
print(f"Quantidade de pássaros detectados: {quantidade_passaros}")
"""

#12 Sistema Simples de Detecção
"""
Considere os dados:

objetos = [
    "pessoa",
    "carro",
    "pessoa",
    "bicicleta",
    "carro",
    "pessoa"
]
Percorra todos os elementos e exiba:

Objeto detectado: pessoa
Objeto detectado: carro
...
Ao final, informe quantas pessoas foram detectadas.

Resultado:

Total de pessoas detectadas: 3
"""
"""
objetos = [
    "pessoa",
    "carro",
    "pessoa",
    "bicicleta",
    "carro",
    "pessoa"
]

pessoas_detectadas = 0

for objeto in objetos:
    
    if objeto == "carro":
        print("Objeto detectado: carro")
    
    if objeto == "pessoa":
        print("Objeto detectado: pessoa")
        pessoas_detectadas +=1
print()   
print("Resultado:")
print()
print(f"Total de pessoas detectadas: {pessoas_detectadas}")
"""