# Cryptography From First Principles

## About

This project is an exploration of cryptography through the implementation of cryptographic algorithms from first principles.

The goal is to connect mathematical concepts with practical software engineering by implementing the mathematics behind each algorithm rather than relying on existing cryptography libraries.

The project will begin with classical substitution ciphers and progressively introduce the mathematical concepts required to implement the RSA cryptosystem.

## Motivation
This project combines two of my areas of interest:

* Mathematics
* Software Engineering

Rather than treating cryptographic algorithms as black boxes, I want to understand how the underlying mathematics translates into executable code.

The project is therefore being developed incrementally, with each algorithm introducing new mathematical and programming concepts.

## Roadmap

### Classical Ciphers

- [x] Project structure
- [x] Alphabet mapping
- [x] Text preprocessing
- [x] Shift Cipher 
- [ ] Affine Cipher
- [ ] Vigenère Cipher
- [ ] Hill Cipher

### Mathematical Foundations
- [x] Euclidean Algorithm / Greatest Common Divisor
- [x] Extended Euclidean Algorithm
- [x] Modular Inverse
- [ ] Modular Exponetiation
- [ ] Prime Number Generation
- [ ] Fast Modular Exponentiation

### RSA
- [ ] RSA key generation
- [ ] RSA ncryption
- [ ] RSA decyption
- [ ] RSA testing
- [ ] RSA demonstration

## Current Implementation
### Shift Cipher
The first implemented algorithm is the Shift Cipher

The encryption transformation is:
[ 
    `C = (P + K) mod (26) ,0 <= C <= 25`
]

where:
* (P) is the plaintext numerical value
* (K) is the encryption key
* (C) is the ciphertext numerical value


Decrytion reverses the transformation:
[
    `P = (C -K) mod (26),  0 <= C <= 25`
]


The alphabet is represented numerically:
A = 0
B = 1
C = 2
...
Z = 25

for example, with a key of 3:
H = 7

(7 + 3) mod 26 = 10

10 = K

Therefore:
H → K

The implementation applies this transformation to every character in the plaintext.


### Mathematical Foundations
The cyprographic algoritms in this project are supposted by mathematical algorithms implemented from first principles.

#### Greatest Common Divisor
The Greatest Common Divisor (GCD) is calclated using the Euclidean Algorithm.
The algorithm is based on the identity:

    `gcd(a, b) = gcd(b, a mod b)`

The process contines until the remainder becomes zero (0).
For example:
    gcd(48, 18)
    48 mod 18 = 12
    10 mod 12 = 6
    12 mod 6 = 0

Therefore:
    gcd(48, 18) = 6


#### Extended Euclidean Agorithm 
The extended Euclidean Agorithm extends the normal Euclidian Algorithm by fininf integers x and y such that: 

    `ax + bx = gcd(a, b)`

This is important for cryptography because it allows us to calculate modular inverses.

#### 


## Project Structure
Crypto_project/ 
│ 
├── README.md 
├── main.py 
├── .gitignore 
│ 
├── ciphers/ 
│ ├── __init__.py 
│ └── shift_cipher.py 
│ 
├── maths/ 
│ ├── __init__.py 
│ └── alphabet.py 
│ 
├── tests/ 
│ └── test_shift_cipher.py 
│
└── docs/

**ciphers/** 
Contains implementations of the cryptographic algorithms

**maths/** 
Contains reusable mathematical utilities used by the cryptographic algorithms

**tests/** 
COntains automated tests used to verify that the implementations behave as expected

**docs/**
Contains additional explanations of the mathematics and algorithms used throughout the project.

## Testing
The project uses Python's unittest framework for automated testing.

Tests can be executed using:

python -m unittest
python -m unittest discover -s tests

The Shift Cipher currently tests:

Encryption
Decryption
Alphabet wrap-around
Encryption followed by decryption








