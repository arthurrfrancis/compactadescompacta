import heapq
import os
from collections import Counter
import pickle

class HuffmanNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char         #caractere armazenado
        self.freq = freq         #frequência desse caractere 
        self.left = left         #filho da esquerda representa 0
        self.right = right       #filho da direita representa 1

    def __lt__(self, other):
        return self.freq < other.freq #define comparação entre nós pela frequência

def build_huffman_tree(frequency_map):
    #cria uma fila de prioridade com os nós individuais
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency_map.items()]
    heapq.heapify(priority_queue)

     #trata o caso de texto com apenas 1 caractere diferente
    if len(priority_queue) == 1:
        node = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, node.freq, left=node)
        heapq.heappush(priority_queue, merged)

    #combina os dois nós de menor frequência até sobrar apenas a raiz
    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)

        merged_node = HuffmanNode(None, left_node.freq + right_node.freq, left_node, right_node)
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0] if priority_queue else None #retorna a raiz da árvore

def generate_huffman_codes(node, current_code="", huffman_codes=None):
    if huffman_codes is None:
        huffman_codes = {} #inicializa dicionário
    if node is None:
        return huffman_codes

    #se o nó for uma folha, salva o código
    if node.char is not None:
        huffman_codes[node.char] = current_code if current_code else "0"
    else:
         #para a esquerda adiciona '0' e para a direita adiciona '1'
        generate_huffman_codes(node.left, current_code + "0", huffman_codes)
        generate_huffman_codes(node.right, current_code + "1", huffman_codes)

    return huffman_codes

def encode_text(text, huffman_codes):
    encoded_text = "".join(huffman_codes[char] for char in text)
    return encoded_text  #retorna string de bits como texto

def compress_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    #conta a frequência de cada caractere
    frequency = Counter(text)
    
    #constrói a árvore de Huffman
    huffman_tree_root = build_huffman_tree(frequency)
    
    #g era os códigos de Huffman
    huffman_codes = {}
    huffman_codes = generate_huffman_codes(huffman_tree_root, "", huffman_codes)
    
    #codifica o texto usando os códigos
    encoded_text = encode_text(text, huffman_codes)

    #calcula e aplica o padding para que o tamanho seja múltiplo de 8
    padding_amount = 8 - (len(encoded_text) % 8)
    if padding_amount == 8:
        padding_amount = 0

    padded_encoded_text = encoded_text + '0' * padding_amount

    #converte o texto binário em uma sequência de bytes
    byte_array = bytearray()
    for i in range(0, len(padded_encoded_text), 8):
        byte = padded_encoded_text[i:i+8]
        byte_array.append(int(byte, 2))

    compressed_data = bytes(byte_array)

    data_to_save = {
        'codes': huffman_codes,
        'padding': padding_amount,
        'data': compressed_data
    }

    #salva os dados compactados usando pickle
    with open(output_file_path, 'wb') as f_out:
        pickle.dump(data_to_save, f_out)

if __name__ == "__main__":
    #define os nomes dos arquivos de entrada e saída
    input_filename = "arquivo2.txt"
    output_filename = "compactado2.txt" 
    compress_file(input_filename, output_filename)
    
print(f"Arquivo {input_filename} foi compactado para {output_filename}.")
