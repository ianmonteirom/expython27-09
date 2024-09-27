"""
Exercício 1
Considere que o arquivo “notas.txt” apresenta uma listagem com os dados dos alunos de uma turma.
Cada linha do arquivo apresenta os dados de um aluno, no formato:
RM,NOME,NOTA1,NOTA2,NOTA3,NOTA4
Implemente um programa que leia este arquivo e gere um novo arquivo JSON no formato:
{
 "2101254": {
 "nome": "Benicio Pires",
 "notas": [
 3.6,
 10.0,
 8.5,
 7.0
 ]
 },
 "2101624": {
 "nome": "Bruna Goncalves",
 "notas": [
 9.5,
 8.0,
 6.0,
 5.5
 ]
 }
}
"""
import json

with open('notas.txt', 'r', encoding="utf-8") as arquivo_notas:
    dict_alunos = {}
    for linha in arquivo_notas:
        palavras = linha.replace("\n", "").split(",")
        rm = palavras[0]
        nome = palavras[1]
        notas = [float(palavras[2]), float(palavras[3]), float(palavras[4]), float(palavras[5])]
        dict_alunos[rm] = {
            'nome': nome,
            'notas': notas
        }

with open('notas.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(dict_alunos, arquivo_json, indent=4, ensure_ascii=False)
