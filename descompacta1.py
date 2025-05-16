def descompactar_rle(texto):
    resultado = ""
    numero = ""

    for char in texto:
        if char.isdigit():
            numero += char 
        else:
            resultado += char * int(numero)
            numero = "" 
    
    return resultado

def descompactar_arquivo_txt_rle(entrada, saida):
    with open(entrada, 'r') as f:
        texto = f.read() 
    descompactado = descompactar_rle(texto)
    with open(saida, 'w') as f:
        f.write(descompactado)

entrada = 'arquivo1.txt'  
saida = 'compactado1.txt'  

saida_descompactado = 'descompactado1.txt'
descompactar_arquivo_txt_rle(saida, saida_descompactado)
print(f"Arquivo {saida} foi descompactado para {saida_descompactado}.")
