import numpy as np
from sympy import Matrix, gcd, mod_inverse
from random import shuffle, seed

# Helper function to convert text to numerical blocks
def text_to_blocks(text, block_size):
    # Convert text to ASCII values and pad if necessary
    padding = block_size - (len(text) % block_size)
    text += ' ' * padding  # Pad with spaces
    blocks = [text[i:i + block_size] for i in range(0, len(text), block_size)]
    return [[ord(char) for char in block] for block in blocks]

# Helper function to convert numerical blocks back to text
def blocks_to_text(blocks):
    return ''.join([chr(int(round(num))) for block in blocks for num in block])

# Generate a random invertible matrix for the Hill Cipher
def generate_key_matrix(block_size):
    while True:
        key_matrix = np.random.randint(0, 256, (block_size, block_size))
        det = int(round(Matrix(key_matrix).det())) % 256
        
        # Ensure determinant is nonzero and has a modular inverse under mod 256
        if det != 0 and gcd(det, 256) == 1:
            return key_matrix

# Encrypt using Hill Cipher (Substitution Layer)
def hill_cipher_encrypt(blocks, key_matrix):
    encrypted_blocks = []
    for block in blocks:
        block_vector = np.array(block).reshape((len(block), 1))
        encrypted_block = np.dot(key_matrix, block_vector) % 256
        encrypted_blocks.append(encrypted_block.flatten().tolist())
    return encrypted_blocks

# Decrypt using Hill Cipher
def hill_cipher_decrypt(blocks, key_matrix):
    key_matrix_inv = Matrix(key_matrix).inv_mod(256)  # Modular inverse
    key_matrix_inv = np.array(key_matrix_inv).astype(int)
    decrypted_blocks = []
    for block in blocks:
        block_vector = np.array(block).reshape((len(block), 1))
        decrypted_block = np.dot(key_matrix_inv, block_vector) % 256
        decrypted_blocks.append(decrypted_block.flatten().tolist())
    return decrypted_blocks

# Transposition using a pseudorandom permutation
def transposition_encrypt(blocks, transposition_key):
    seed(transposition_key)  # Seed the PRNG
    indices = list(range(len(blocks)))
    shuffle(indices)  # Shuffle indices
    shuffled_blocks = [blocks[i] for i in indices]
    return shuffled_blocks, indices  # Return shuffled blocks and shuffle order

# Reverse transposition using stored order
def transposition_decrypt(blocks, indices):
    reverse_indices = sorted(range(len(indices)), key=lambda x: indices[x])
    return [blocks[i] for i in reverse_indices]

# Main Encryption Function
def hybrid_encrypt(plaintext, block_size, substitution_key, transposition_key):
    # Step 1: Convert plaintext to numerical blocks
    blocks = text_to_blocks(plaintext, block_size)
    
    # Step 2: Apply Hill Cipher (Substitution Layer)
    encrypted_blocks = hill_cipher_encrypt(blocks, substitution_key)
    
    # Step 3: Apply Transposition
    transposed_blocks, indices = transposition_encrypt(encrypted_blocks, transposition_key)
    
    return transposed_blocks, indices

# Main Decryption Function
def hybrid_decrypt(ciphertext_blocks, indices, substitution_key):
    # Step 1: Reverse Transposition
    untransposed_blocks = transposition_decrypt(ciphertext_blocks, indices)
    
    # Step 2: Reverse Hill Cipher (Substitution Layer)
    decrypted_blocks = hill_cipher_decrypt(untransposed_blocks, substitution_key)
    
    # Step 3: Convert blocks back to text
    plaintext = blocks_to_text(decrypted_blocks)
    return plaintext.strip()  # Remove padding spaces

# Example Usage
if __name__ == "__main__":
    # Parameters
    block_size = 4  # Block size for Hill Cipher
    substitution_key = generate_key_matrix(block_size)  # Random key matrix
    transposition_key = input("Enter SECRETKEY : ")  # Key for transposition
    
    # Plaintext
    plaintext = input("Enter Plain text: ")
    
    # Encryption
    ciphertext_blocks, indices = hybrid_encrypt(plaintext, block_size, substitution_key, transposition_key)
    print("Ciphertext Blocks:", ciphertext_blocks)
    
    # Decryption
    decrypted_text = hybrid_decrypt(ciphertext_blocks, indices, substitution_key)
    print("Decrypted Text:", decrypted_text)
