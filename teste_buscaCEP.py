def line(): 
    print('=-' * 20)



import requests  

def obter_cep(cep): 
    #variavel url recebe api do viacep 
    url = f'https://viacep.com.br/ws/{cep}/json/'

# Realiza a solicitação GET do CEP à API
    resposta = requests.get(url)

# verifica se a conexão foi bem sucedida 
    if resposta.status_code == 200: 
        # Converte a resposta em dict Python 
        dados_cep = resposta.json()
        return dados_cep
    else: 
        print(f'Erro: {resposta.status_code}, {resposta.text}')
        #se a solicitação não for bem sucedida retorna o 
        # cod status da falha e o text



while True:
    cep = input('Insira seu cep: ')
    print()
    print('MENU DE ACESSO\n' '******************\n' 'cep,\n' 'logradouro,\n' 'bairro,\n'
          'localidade,\n' 'uf,\n' 'ddd,\n' 'tudo')
    escolha = input('Digite qual acesso deseja: ').lower()
    print()
    if escolha == 'cep':
        print(f'O CEP consultado é: {obter_cep(cep)['cep']}')
    elif escolha == 'logradouro':
        print(f'O logradouro consultado é: {obter_cep(cep)['logradouro']}')
    elif escolha == 'bairro':
        print(f'O bairro consultado é:{obter_cep(cep)['bairro']}')
    elif escolha == 'localidade':
        print(f'A localidade consultada é: {obter_cep(cep)['localidade']}')
    elif escolha == 'uf':
        print(f'A unidade federativa é: {obter_cep(cep)['uf']}')
    elif escolha == 'ddd':
        print(f'A unidade federativa correspode à: {obter_cep(cep)['ddd']}')
    else:
        if escolha == 'tudo': 
            print(f'Todas as informação são:{obter_cep(cep)}')    
        
        
        
        
    menu = input('Continue ? [S/N]: ').upper()
    if menu == 'N':
        break  
    else: 
        while menu not in 'SN': 
            menu = input('Favor inserir somente [S] ou [N]: ').upper()
print()       
print('PROGRAMA ENCERRADO !!!')

