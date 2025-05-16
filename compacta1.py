def compactar(texto):
    resultado = ""
    contador = 1
    # Percorre o texto a partir do segundo caractere
    for i in range(1, len(texto)):
        # Se o caractere atual é igual ao anterior, incrementa o contador
        if texto[i] == texto[i - 1]:
            contador += 1
        else:
            # Se for diferente, adiciona a contagem e o caractere anterior ao resultado
            resultado += str(contador) + texto[i - 1]
            contador = 1  # Reinicia o contador
    # Adiciona o último grupo ao resultado
    resultado += str(contador) + texto[-1]
    return resultado

# Função que lê um arquivo de texto, aplica a compactação RLE e salva o resultado em outro arquivo
def compactar_arquivo_txt_rle(entrada, saida):
    # Abre o arquivo de entrada e lê seu conteúdo
    with open(entrada, 'r') as f:
        texto = f.read()
    # Compacta o texto usando a função compactar
    compactado = compactar(texto) 
    # Escreve o texto compactado no arquivo de saída
    with open(saida, 'w') as f:
        f.write(compactado) 

# Define os nomes dos arquivos de entrada e saída
entrada = 'arquivo1.txt'  
saida = 'compactado1.txt' 

# Executa a compactação do arquivo
compactar_arquivo_txt_rle(entrada, saida)
print(f"Arquivo {entrada} foi compactado para {saida}.")
