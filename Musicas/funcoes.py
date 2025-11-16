import csv

# ler o caminho 
caminho_arquivo = "C:/Users/pedro/Downloads/Aulas Generation\Musicas/assets/musicas.csv"


#criando função 
# sempre devo colocar a instrução def + nome da função
def ler_musicas():
    print("----- Lista de Musicas------")
    try:
        # O 'with open' deve estar aninhado dentro do 'try'
        with open(caminho_arquivo, "r",encoding='utf-8') as arquivo_musicas:
            # o comando with open permite que abra algo 
            # mas preciso informar 
            # 1 onde ele está 
            # 2- o modo de abertura(ler - r; adicionar -a)
            # 3- Não obrigatório - colocar como ler (codificação 'utf-8')
            # e depois dar um apelido para essa instrução
            
            leitor = csv.reader(arquivo_musicas)
            # chamei um leitor para o sistema
            # que lê csv
            
            next(leitor)
            # o comando next é para pular a primeira linha do df
            
            # agora quero exibir linha por linha
            for cada_linha in leitor:
                if cada_linha:
                    titulo,artista,ano,genero,duracao_segundos = cada_linha
                    #tenho que falar todos os cabeçalhos do meu arquivo  
                    dados_formatados = [titulo,artista, genero]
                    print(", ".join(dados_formatados))
    # O 'except' deve estar no mesmo nível do 'try'
    except FileNotFoundError:
        # O 'print' deve estar aninhado dentro do 'except'
        print('erro')