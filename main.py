import uteis
import arquivo

#.\\venv\Scripts\Activate.ps1 


uteis.cabecalho('SISTEMA ADEGA'.center(42))

arquivo.arquivoExiste('estoqueAdega.txt')

if arquivo.arquivoExiste('estoqueAdega.txt') == False:
    arquivo.criarArquivo('estoqueAdega.txt')

validacao = arquivo.login()

if validacao == True:  
    while True:
        resp = uteis.menu(['Ver estoque', 'Adicionar Produto','Repor estoque', 'Sair'])
        
        if resp == 1:
            arquivo.lerArquivo('estoqueAdega.txt')
            print()
            print(uteis.fonteCiano(arquivo.totalEmEstoque('estoqueAdega.txt')))
        elif resp == 2:
            uteis.cabecalho('INSERIR NOVOS PRODUTOS'.center(42))
            nomeProduto = str(input('Nome do produto: ')).upper()
            preco = uteis.leiaDinheiro()
            qtd = uteis.leiaInt('Quantidade do produto: ')
            arquivo.novoCadastro('estoqueAdega.txt', nomeProduto, preco, qtd)
        elif resp == 3:
            uteis.cabecalho('REPOR ESTOQUE'.center(42))
        elif resp == 4:
            print(uteis.fonteVermelha('Encerrando Sistema'))
            break


