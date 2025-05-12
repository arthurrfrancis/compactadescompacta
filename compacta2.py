import heapq
import os
from collections import Counter
import pickle

class HuffmanNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequency_map):
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency_map.items()]
    heapq.heapify(priority_queue)

    if len(priority_queue) == 1:
        node = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, node.freq, left=node)
        heapq.heappush(priority_queue, merged)

    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)

        merged_node = HuffmanNode(None, left_node.freq + right_node.freq, left_node, right_node)
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0] if priority_queue else None

def generate_huffman_codes(node, current_code="", huffman_codes=None):
    if huffman_codes is None:
        huffman_codes = {}
    if node is None:
        return huffman_codes

    if node.char is not None:
        huffman_codes[node.char] = current_code if current_code else "0"
    else:
        generate_huffman_codes(node.left, current_code + "0", huffman_codes)
        generate_huffman_codes(node.right, current_code + "1", huffman_codes)

    return huffman_codes

def encode_text(text, huffman_codes):
    encoded_text = "".join(huffman_codes[char] for char in text)
    return encoded_text

def compress_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    frequency = Counter(text)
    
    huffman_tree_root = build_huffman_tree(frequency)
    
    huffman_codes = {}
    huffman_codes = generate_huffman_codes(huffman_tree_root, "", huffman_codes)
    
    encoded_text = encode_text(text, huffman_codes)

    padding_amount = 8 - (len(encoded_text) % 8)
    if padding_amount == 8:
        padding_amount = 0

    padded_encoded_text = encoded_text + '0' * padding_amount

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

    with open(output_file_path, 'wb') as f_out:
        pickle.dump(data_to_save, f_out)

if __name__ == "__main__":
    input_filename = "arquivo2.txt"
    output_filename = "compactado2.txt" 
    compress_file(input_filename, output_filename)
    
print(f"Arquivo {input_filename} foi compactado para {output_filename}.")