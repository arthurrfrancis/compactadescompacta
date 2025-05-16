import pickle

def decode_text(encoded_text, huffman_codes):
    #cria um dicionário invertido código - caractere
    reverse_huffman_codes = {v: k for k, v in huffman_codes.items()}
    decoded_chars = [] #lista para armazenar os caracteres decodificados
    current_code = ""  #armazena temporariamente o código binário enquanto o percorre
    #percorre cada bit da string de texto codificado
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_huffman_codes:
        #se o código for encontrado no dicionário, adiciona o caractere correspondente
            character = reverse_huffman_codes[current_code]
            decoded_chars.append(character)
            current_code = "" #reinicia o código para o próximo caractere
    return "".join(decoded_chars)

def decompress_file(input_file_path, output_file_path):
     #abre o arquivo compactado e carrega os dados binários
    with open(input_file_path, 'rb') as f_in:
        saved_data = pickle.load(f_in)

    #extrai as informações necessárias
    huffman_codes = saved_data['codes']
    padding_amount = saved_data['padding']
    compressed_bytes = saved_data['data']

    #converte os bytes compactados em uma string binária
    bit_string = ""
    for byte_val in compressed_bytes:
        bits = bin(byte_val)[2:].rjust(8, '0') #converte cada byte para 8 bits
        bit_string += bits

    #remove o padding
    if padding_amount > 0:
        encoded_text_unpadded = bit_string[:-padding_amount]
    else:
        encoded_text_unpadded = bit_string

    #se houver dados válidos, faz a decodificação do texto
    if not encoded_text_unpadded and not huffman_codes and not compressed_bytes:
        decompressed_text = ""
    else:
        decompressed_text = decode_text(encoded_text_unpadded, huffman_codes)

    with open(output_file_path, 'w', encoding='utf-8') as f_out:
        f_out.write(decompressed_text)

#define os nomes dos arquivos de entrada e saída
if __name__ == "__main__":
    compressed_filename = "compactado2.txt"
    decompressed_filename = "descompactado2.txt"

    #chama a função de descompactação
    decompress_file(compressed_filename, decompressed_filename)
print(f"Arquivo {compressed_filename} foi descompactado para {decompressed_filename}.")
