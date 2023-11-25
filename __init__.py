#Modulo com funções de cunho estético para o Sistema

def linha(tam = 42):
    print('-' * tam)

def cabecalho (msg):
    """
    -> Função titulo exibe mensagem de titulo com borda em '=='
    :param msg: recebe mensagem a ser mostrada
    Função criada por Vinicius Cardoso
    """
    linha()
    print(msg)
    linha()

def fonteCiano(msg):
    return f'\033[36m{msg}\033[m'

def fonteVermelha(msg):
    return f'\033[31m{msg}\033[m'

def fonteVerde(msg):
    return f'\033[32m{msg}\033[m'

def fonteAmarela(msg):
    return f'\033[33m{msg}\033[m'

def leiaInt(msg='Infome um número Inteiro: '):
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! NÃO é um número inteiro. TENTE NOVAMENTE\033[m')
        else:
            break
    return i

def leiaFloat(msg='Infome um número Decimal: '):
    while True:
        try:
            f = float(msg)
        except (ValueError, TypeError):
            print(f'\033[31mERRO! NÃO é um número Decimal. TENTE NOVAMENTE\033[m')
        else:
            break
    return f

def leiaDinheiro(msg='Digite o preço:R$ '):
    """
    -> Valida dado convertendo-o valor digitado em float.
    :param n: mensagem a ser exibida no input
    :return: float de n
    """
    valido = False
    while not valido:
        try:
            entrada = str(input(msg)).replace(',','.').strip()
            if entrada.isalpha() or entrada == '':
                print(f'\033[0;31mERR0! {entrada} NÃO é um valor válido!\033[m')
            else:
                valido = True
                return float(entrada)
        except (ValueError, TypeError):
            print('Valor inserido não é válido tente novamente')
            valido = False

def menu (lista):
    cabecalho('MENU PRINCIPAL'.center(42))
    c = 1
    for p in lista:
        print(f'{fonteVerde(c)} - {fonteAmarela(p)}')
        c += 1
    linha()

    while True:
        resp = leiaInt(fonteCiano('Sua opção? '))    
        if resp >= 1 and resp <= c:
            print(fonteVerde(f'Opção {resp} selecionada'))
            break
        else:
            print(fonteVermelha('Opção Inválida.Tente novamente.'))    
    return resp
     
        
