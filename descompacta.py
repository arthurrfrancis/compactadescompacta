def descompactar_rle(texto):
    resultado = ""
    numero = ""

    # Descompressão
    for char in texto:
        if char.isdigit():
            numero += char  # Acumula números
        else:
            resultado += char * int(numero)  # Repete o caractere
            numero = ""  # Reseta o contador
    
    return resultado

# Função para descompactar o arquivo .txt (se necessário)
def descompactar_arquivo_txt_rle(entrada, saida):
    with open(entrada, 'r') as f:
        texto = f.read()  # Lê o conteúdo compactado
    descompactado = descompactar_rle(texto)  # Descompacta o conteúdo
    with open(saida, 'w') as f:
        f.write(descompactado)  # Escreve o conteúdo descompactado no novo arquivo

entrada = 'arquivo1.txt'  # Arquivo de entrada
saida = 'compactado.txt'  # Arquivo de saída (compactado)

# Teste de descompactação (se necessário)
saida_descompactado = 'descompactado.txt'
descompactar_arquivo_txt_rle(saida, saida_descompactado)
print(f"Arquivo {saida} foi descompactado para {saida_descompactado}.")
