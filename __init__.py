import uteis

def cadastroUsuario():
    uteis.cabecalho('Cadastro novo usuário'.center(42))
    nomeUsuario = str(input('Nome Usuario: '))
    senha = str(input('Senha: '))

    try:
        arq = 'usuarios.txt'
        a = open(arq, 'at')
        a.write(f'{nomeUsuario};{senha}\n')
    except:
        print(uteis.fonteVermelha('ERRO ao adionar usuário'))
    else:
        print(uteis.fonteVerde('USUÁRIO ADICIONADO COM SUCESSO'))
        a.close()

def login():
    uteis.cabecalho('LOGIN NO SISTEMA')
    try:
        arq = 'usuarios.txt'
        a = open(arq, 'rt')
    except:
        print(uteis.fonteVermelha('ERRO de execução'))
    else:
        nomeUsuario = str(input('Nome: '))
        senha = str(input('Senha: '))
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            nomeArquivado = dado[0]
            senhaArquivada = dado[1]
            if nomeArquivado == nomeUsuario and senhaArquivada == senha:
                print(uteis.fonteVerde(f'Acesso de {nomeUsuario} LIBERADO!'))
                return True
            
        print(uteis.fonteVermelha('Dados Incorretos,acesso negado'))
        return False
        
def arquivoExiste(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo (nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Houve um Erro na criação do Arquivo')
    else:
        print(f'Arquivo: {nomeArquivo} criado com sucesso!')

def lerArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt', encoding='utf-8')
    except:
        print('Erro ao ler o arquivo')
    else:
        uteis.cabecalho('ITENS CADASTRADOS'.center(42))
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n','')
            print(f'PRODUTO: {dado[0]:<10}  PREÇO: R${dado[1]:>5}  QTD.:{dado[2]:>5}')
    finally:
        a.close()

def novoCadastro(arq, nomeProduto='desconhecido', preco=0.0, quantidade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nomeProduto};{preco};{quantidade}\n')
        except:
            print('Houve um erro ao adionar dados')
        else:
            print(f'PRODUTO: {nomeProduto} - PREÇO: R${preco} - Quantidade: {quantidade}')
            print(uteis.fonteVerde('ADICIONADO COM SUCESSO'))
            a.close()

def totalEmEstoque(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else: 
        total_geral = 0
        for linha in a:
            total_produto = 0
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n','')
            qtd_produto = int(dado[2])
            preco = float(dado[1])
            total_produto = qtd_produto * preco
            total_geral += total_produto
            
        return f'Total em Estoque: R$ {total_geral:.2f} reais'
    finally:
        a.close()
        
  
        






    