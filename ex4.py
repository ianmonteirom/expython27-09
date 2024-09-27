"""
Exercício 4
Implemente um sistema para cadastro de Pets, com as opções Inserir, Excluir, Listar Todos.
Utilize um arquivo JSON para armazenar as informações.
O arquivo JSON deve ter a estrutura abaixo e conforme as operações realizadas, o arquivo deve ser
modificado.
[
 {
 "tipo": "Cachorro",
 "nome": "Bebel",
 "idade": 4
 },
 {
 "tipo": "Hamster",
 "nome": "Pimpão",
 "idade": 2
 },
 {
 "tipo": "Cavalo",
 "nome": "Trovão",
 "idade": 6
 }
]
"""
import json

try:
    print('Tentando abrir o arquivo...')
    with open('pets.json', 'r', encoding='utf-8') as arquivo:
        arquivo.read()
except FileNotFoundError:
    print(f'Arquivo não encontrado, criando...')
    with open('pets.json', 'w', encoding='utf-8') as arquivo:
        arquivo.write('')
else:
    print('Arquivo encontrado com sucesso.')

with open('pets.json', 'r', encoding='utf-8') as arquivo_json:
    pets = json.load(arquivo_json)

print(pets)

while True:
    print(
        '''
----------------------------------------------------
1 - Inserir
2 - Excluir
3 - Listar Todos
----------------------------------------------------
        ''')
    opc = int(input('Digite uma opção: '))
    match opc:
        case 1:
            with open('pets.json', 'w', encoding='utf-8') as arquivo:
                dados = {'tipo': str(input('Tipo do animal: ')).strip().capitalize(),
                         'nome': str(input('Nome do animal: ')).strip().capitalize(),
                         'idade': int(input('Idade do animal: '))}
                pets.append(dados)
                json.dump(pets, arquivo, indent=4, ensure_ascii=False)
        case 2:
            with open('pets.json', 'w', encoding='utf-8') as arquivo:
                for i in range(len(pets)):
                    print(f'{i + 1} - Tipo: {pets[i]['tipo']}, Nome: {pets[i]['nome']}, Idade: {pets[i]['idade']}')
                esc = int(input('Digite um índice para excluir: '))
                pets.pop(esc - 1)
                print(pets)
                json.dump(pets, arquivo, indent=4, ensure_ascii=False)
        case 3:
            for i in range(len(pets)):
                print(f'{i + 1} - Tipo: {pets[i]['tipo']}, Nome: {pets[i]['nome']}, Idade: {pets[i]['idade']}')
