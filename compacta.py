def compactar(texto):
    resultado = ""
    contador = 1

    for i in range(1, len(texto)):
        if texto[i] == texto[i - 1]:
            contador += 1
        else:
            resultado += str(contador) + texto[i - 1]
            contador = 1

    resultado += str(contador) + texto[-1]  # Último grupo
    return resultado


# Função para compactar o arquivo .txt
def compactar_arquivo_txt_rle(entrada, saida):
    with open(entrada, 'r') as f:
        texto = f.read()  # Lê todo o conteúdo do arquivo
    compactado = compactar(texto)  # Compacta o conteúdo
    with open(saida, 'w') as f:
        f.write(compactado)  # Escreve o conteúdo compactado no novo arquivo



# Teste de compactação
entrada = 'arquivo1.txt'  # Arquivo de entrada
saida = 'compactado.txt'  # Arquivo de saída (compactado)

compactar_arquivo_txt_rle(entrada, saida)
print(f"Arquivo {entrada} foi compactado para {saida}.")


