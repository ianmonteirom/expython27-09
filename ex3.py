"""
Exercício 3
Considere o arquivo “heroes.json”, com informações sobre 10 super-heróis. Faça um programa em Python
que leia o arquivo json e informe os nomes dos heróis que possuem o poder de voar ("Flight").
"""
import json

with open('heroes.json', 'r', encoding='utf-8') as arquivo:
    heroes = json.load(arquivo)
    for i in range(len(heroes)):
        if 'Flight' in heroes["members"][i]["powers"]:
            print(f'{heroes["members"][i]["name"]} pode voar')
