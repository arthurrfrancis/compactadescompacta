def compactar(texto):
    resultado = ""
    contador = 1

    for i in range(1, len(texto)):
        if texto[i] == texto[i - 1]:
            contador += 1
        else:
            resultado += str(contador) + texto[i - 1]
            contador = 1

    resultado += str(contador) + texto[-1]
    return resultado


def compactar_arquivo_txt_rle(entrada, saida):
    with open(entrada, 'r') as f:
        texto = f.read()
    compactado = compactar(texto) 
    with open(saida, 'w') as f:
        f.write(compactado) 


entrada = 'arquivo1.txt'  
saida = 'compactado1.txt' 

compactar_arquivo_txt_rle(entrada, saida)
print(f"Arquivo {entrada} foi compactado para {saida}.")