import sqlite3


PESO_SACO_KG = 20

TIPOS_TECIDO = {
    '1': 'jeans',
    '2' : 'pt',

}


conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS coletas(
        id INTEGER PRIMARY KEY,
        tecido TEXT,
        qtd_sacos INTEGER
    )
""")
conexao.commit()

cadastro = []

def cadastro_tecido():
    while True:
        print('\n1 - Jeans')
        print('2 - PT')
        print('0 - Sair')

        opcao = input('Escolha o tipo de tecido: ')

        if opcao == '0':
            print('Encerrando o programa...')
            break
        if opcao not in TIPOS_TECIDO:
            print('Inválida, tente novamente.')

        tecidos = TIPOS_TECIDO[opcao]

        
        qtd = int(input('Digite a quantidade de saco coletados: '))


        lista = {'tecidos': tecidos, 'qtd': qtd}

        cadastro.append(lista.copy())

        cursor.execute("INSERT INTO coletas (tecido, qtd_sacos) VALUES (?,?)",
        (tecidos,qtd))
        conexao.commit()

        print('Tecido cadastrado com sucesso!')

#Programa principal
print('Digite no campo abaixo o tipo de tecido e a quantidade')

cadastro_tecido()
resumo = {}
for item in cadastro:
    nome = item['tecidos']
    quantidade = item['qtd']

    resumo[nome] = resumo.get(nome, 0) + quantidade

cursor.execute('SELECT * FROM coletas')
todos = cursor.fetchall()
print('--- Dados salvos no banco ---')
for linha in todos:
    print(linha)

for tecido, total in resumo.items():
    peso = total * PESO_SACO_KG
    print(f'Tecido: {tecido} , Quantidades total de sacos: {total}, Peso total: {peso}kg ')