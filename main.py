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
for item in cadastro:
    print(f'Tecido: {item['tecidos']} , Quantidades: {item['qtd']}')