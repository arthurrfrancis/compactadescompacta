def descompactar_rle(texto):
    resultado = ""
    numero = ""
 #percorre cada caractere do texto compactado
    for char in texto:
        if char.isdigit():
            numero += char #se for um número, acumula no numero
        else:
             #quando encontra um caractere, multiplica ele pela quantidade lida
            resultado += char * int(numero)
            numero = "" #limpa numero para o próximo grupo
    
    return resultado

def descompactar_arquivo_txt_rle(entrada, saida):
     #abre o arquivo compactado e lê o conteúdo
    with open(entrada, 'r') as f:
        texto = f.read() 
    #usa a função de descompactação para obter o texto original
    descompactado = descompactar_rle(texto)
    #escreve o texto descompactado no arquivo de saída
    with open(saida, 'w') as f:
        f.write(descompactado)

#define os nomes dos arquivos de entrada e saída
entrada = 'arquivo1.txt'  
saida = 'compactado1.txt'  

#executa a descompactação do arquivo compactado
saida_descompactado = 'descompactado1.txt'
descompactar_arquivo_txt_rle(saida, saida_descompactado)
print(f"Arquivo {saida} foi descompactado para {saida_descompactado}.")
