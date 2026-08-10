PESO_SACO_KG = 20

cadastro = []

def cadastro_tecido():
    while True:
        tecidos = input('Digite o tipo de tecido: ')
        if tecidos == '3':
            print('Encerrando o programa...')
            break
        
        qtd = int(input('Digite a quantidade de saco coletados: '))


        lista = {'tecidos': tecidos, 'qtd': qtd
         
}

        cadastro.append(lista.copy())

        print('Tecido cadastrado com sucesso!')

#Programa principal
print('Digite no campo abaixo o tipo de tecido e a quantidade')
print('Digite 3 - Para sair do programa')

cadastro_tecido()
resumo = {}
for item in cadastro:
    nome = item['tecidos']
    quantidade = item['qtd']

    resumo[nome] = resumo.get(nome, 0) + quantidade

for tecido, total in resumo.items():
    peso = total * PESO_SACO_KG
    print(f'Tecido: {tecido} , Quantidades total de sacos: {total}, Peso total: {peso}kg ')