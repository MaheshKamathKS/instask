import numpy as np
from sympy import Matrix, gcd
from random import shuffle, seed

def text_to_blocks(text, block_size):
    padding = block_size - (len(text) % block_size)
    text += ' ' * padding
    blocks = [text[i:i + block_size] for i in range(0, len(text), block_size)]
    return [[ord(char) for char in block] for block in blocks]

def blocks_to_text(blocks):
    return ''.join([chr(int(round(num))) for block in blocks for num in block])

def generate_key_matrix(block_size):
    while True:
        key_matrix = np.random.randint(1, 256, (block_size, block_size))
        det = int(round(Matrix(key_matrix).det())) % 256
        if det != 0 and gcd(det, 256) == 1:
            try:
                Matrix(key_matrix).inv_mod(256)
                return key_matrix
            except ValueError:
                continue

def hill_cipher_encrypt(blocks, key_matrix):
    encrypted_blocks = []
    for block in blocks:
        block_vector = np.array(block).reshape((len(block), 1))
        encrypted_block = (np.dot(key_matrix.astype(np.int64), block_vector) % 256).astype(np.uint8)
        encrypted_blocks.append(encrypted_block.flatten().tolist())
    return encrypted_blocks

def hill_cipher_decrypt(blocks, key_matrix):
    try:
        key_matrix_inv = Matrix(key_matrix).inv_mod(256)
    except ValueError:
        raise ValueError("The generated key matrix is not invertible under mod 256. Please regenerate.")
    
    key_matrix_inv = np.array(key_matrix_inv).astype(int)
    decrypted_blocks = []
    for block in blocks:
        block_vector = np.array(block).reshape((len(block), 1))
        decrypted_block = np.dot(key_matrix_inv, block_vector) % 256
        decrypted_blocks.append(decrypted_block.flatten().tolist())
    return decrypted_blocks

def transposition_encrypt(blocks, transposition_key):
    seed(transposition_key)
    indices = list(range(len(blocks)))
    shuffle(indices)
    shuffled_blocks = [blocks[i] for i in indices]
    return shuffled_blocks, indices

def transposition_decrypt(blocks, indices):
    reverse_indices = sorted(range(len(indices)), key=lambda x: indices[x])
    return [blocks[i] for i in reverse_indices]

def hybrid_encrypt(plaintext, block_size, substitution_key, transposition_key):
    blocks = text_to_blocks(plaintext, block_size)
    encrypted_blocks = hill_cipher_encrypt(blocks, substitution_key)
    transposed_blocks, indices = transposition_encrypt(encrypted_blocks, transposition_key)
    return transposed_blocks, indices

def hybrid_decrypt(ciphertext_blocks, indices, substitution_key):
    untransposed_blocks = transposition_decrypt(ciphertext_blocks, indices)
    decrypted_blocks = hill_cipher_decrypt(untransposed_blocks, substitution_key)
    plaintext = blocks_to_text(decrypted_blocks)
    return plaintext.strip()

if __name__ == "__main__":
    block_size = 4
    substitution_key = generate_key_matrix(block_size)
    
    transposition_key = input("Enter SECRETKEY: ")
    seed_val = sum(ord(c) for c in transposition_key)  

    plaintext = input("Enter Plain text: ")

    ciphertext_blocks, indices = hybrid_encrypt(plaintext, block_size, substitution_key, seed_val)
    print("Ciphertext Blocks:", ciphertext_blocks)

    decrypted_text = hybrid_decrypt(ciphertext_blocks, indices, substitution_key)
    print("Decrypted Text:", decrypted_text)
