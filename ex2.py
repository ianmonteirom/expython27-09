"""
Exercício 2
Considere o arquivo “foods.txt”, com três colunas, no formato abaixo, onde cada linha representa um
indivíduo com suas respectivas informações.
NAME,ID,FAVORITEFOOD
Implemente um programa que a partir do arquivo indicado gere um arquivo JSON no formato:
{
 "1": {
 "name": "John Doe",
 "food": "pizza"
 },
 "2": {
 "name": "Jane Smith",
 "food": "sushi"
 },
 "3": {
 "name": "Michael Johnson",
 "food": "steak"
 }
}
"""
import json

with open('foods.txt', 'r', encoding='utf-8') as arquivo_foods:
    dict_foods = {}
    for linha in arquivo_foods:
        dados = linha.replace("\n", "").split(",")
        print(dados)
        id = dados[1]
        name = dados[0]
        food = dados[2]
        dict_foods[id] = {
            'name': name,
            'food': food
        }

with open('foods.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(dict_foods, arquivo_json, indent=4, ensure_ascii=False)
