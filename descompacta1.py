def descompactar_rle(texto):
    resultado = ""
    numero = ""
 # Percorre cada caractere do texto compactado
    for char in texto:
        if char.isdigit():
            numero += char # Se for um número, acumula no numero
        else:
             # Quando encontra um caractere, multiplica ele pela quantidade lida
            resultado += char * int(numero)
            numero = "" # Limpa numero para o próximo grupo
    
    return resultado

def descompactar_arquivo_txt_rle(entrada, saida):
     # Abre o arquivo compactado e lê o conteúdo
    with open(entrada, 'r') as f:
        texto = f.read() 
    # Usa a função de descompactação para obter o texto original
    descompactado = descompactar_rle(texto)
    # Escreve o texto descompactado no arquivo de saída
    with open(saida, 'w') as f:
        f.write(descompactado)

# Define os nomes dos arquivos de entrada e saída
entrada = 'arquivo1.txt'  
saida = 'compactado1.txt'  

# Executa a descompactação do arquivo compactado
saida_descompactado = 'descompactado1.txt'
descompactar_arquivo_txt_rle(saida, saida_descompactado)
print(f"Arquivo {saida} foi descompactado para {saida_descompactado}.")
