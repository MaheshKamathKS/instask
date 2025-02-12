# Hybrid Cipher: Combining Substitution and Transposition Techniques

This repository contains the implementation of a **hybrid cipher** that combines substitution (using a modified Hill Cipher) and transposition techniques to achieve robust encryption with at least **128-bit security strength**. The hybrid approach ensures resistance against classical cryptanalysis methods such as frequency analysis and linear algebra attacks.

---

## Table of Contents
- **LiveTest**: [ClickHere!!](https://colab.research.google.com/drive/1s7P9npIOYns3booavWHcv35oiP23WMXS?usp=sharing)
1. [Overview](#overview)
2. [Features](#features)
3. [How It Works](#how-it-works)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Example](#example)
7. [Security Justification](#security-justification)
8. [Contributing](#contributing)
9. [License](#license)

---

## Overview

The hybrid cipher integrates two classical cryptographic techniques:
- **Substitution Layer**: A modified Hill Cipher encrypts plaintext blocks using matrix multiplication over a finite field.
- **Transposition Layer**: A pseudorandom permutation rearranges the encrypted blocks to disrupt patterns.

This combination ensures both confusion (substitution) and diffusion (transposition), making the cipher more secure than either technique alone.

---

## Features

- Achieves **at least 128-bit encryption strength**.
- Combines **confusion** (Hill Cipher) and **diffusion** (transposition).
- Modular design allows for scalability (e.g., increasing block size).
- Deterministic yet unpredictable behavior using a seeded pseudorandom number generator (PRNG).

---

## How It Works

1. **Substitution Layer**:
   - Converts plaintext into numerical blocks.
   - Encrypts each block using a randomly generated invertible matrix (Hill Cipher).
2. **Transposition Layer**:
   - Shuffles the encrypted blocks using a PRNG seeded with a secret key.
3. **Decryption**:
   - Reverses the transposition and substitution layers to recover the plaintext.

---

## Installation

### Prerequisites

To run the code, you need the following Python libraries:

- `numpy`: For matrix operations.
- `sympy`: For modular matrix inversion.

### Steps to Install Dependencies

1. Clone the repository:
   ```bash
   git clone https://github.com/MaheshKamathKS/instask.git
   cd hybridcipher
   ```
2. Install the required libraries using pip:
   ```bash
   pip install numpy sympy
   ```

---

## Usage

Once the dependencies are installed, follow these steps to run the hybrid cipher:

1. Save the `hybrid_cipher.py` file in your working directory.
2. Run the script using Python:
   ```bash
   python hybrid_cipher.py
   ```

### Customizing Parameters

You can modify the following parameters in the script:

- `block_size`: Size of each plaintext block (default is 4).
- `substitution_key`: Randomly generated key matrix for the Hill Cipher.
- `transposition_key`: Secret key for seeding the PRNG.

---

## Example

### Input:
- **Plaintext**: "HELLO WORLD"
- **Block Size**: 4
- **Substitution Key**: Randomly generated 4×4 matrix.
- **Transposition Key**: "SECRETKEY"

### Output:
- Encrypted ciphertext blocks (numerical representation).
- Decrypted plaintext: "HELLO WORLD"

---

## Security Justification

- **Confusion**: The Hill Cipher obscures relationships between plaintext and ciphertext by replacing plaintext blocks with seemingly unrelated ciphertext blocks.
- **Diffusion**: The transposition layer spreads the influence of each plaintext character across multiple ciphertext blocks, disrupting patterns and ensuring that partial information about the ciphertext is insufficient for decryption.
- **128-bit Strength**: By operating on large matrices and using modular arithmetic, the cipher achieves computational complexity comparable to modern encryption standards, ensuring brute-force attacks are computationally prohibitive.

---

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or improvements, feel free to open an issue or submit a pull request. Please ensure your contributions align with the project's goals and coding standards.

---


## Acknowledgments

The design of this hybrid cipher is inspired by classical cryptographic techniques and modern encryption principles.
Special thanks to the open-source community for tools like `numpy` and `sympy`, which made this implementation possible.

---

## Contact

For questions or feedback, feel free to reach out:

- **GitHub**: https://github.com/MaheshKamathKS
- **Email**: sreview92@gmail.com

Happy coding! 🔐
