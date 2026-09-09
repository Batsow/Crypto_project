# Cryptography From First Principles

## About

This project is an exploration of cryptography through the implementation of cryptographic algorithms from first principles.

The goal is to connect mathematical concepts with practical software engineering by implementing the mathematics behind each algorithm rather than relying on existing cryptography libraries.

The project begins with classical substitution ciphers and progressively introduces the mathematical concepts required to understand and implement the RSA cryptosystem.

---

## Motivation

This project combines two of my areas of interest:

* Mathematics
* Software Engineering

Rather than treating cryptographic algorithms as black boxes, I want to understand how the underlying mathematics translates into executable code.

The project is therefore being developed incrementally, with each algorithm introducing new mathematical and programming concepts.

The main question behind the project is:

> How can the mathematical definitions behind cryptographic algorithms be translated into working, tested software from first principles?

---

## Roadmap

### Classical Ciphers

* [x] Project structure
* [x] Alphabet mapping
* [x] Text preprocessing
* [x] Shift Cipher
* [x] Affine Cipher
* [ ] Vigenère Cipher
* [ ] Hill Cipher

### Mathematical Foundations

* [x] Euclidean Algorithm / Greatest Common Divisor
* [x] Extended Euclidean Algorithm
* [x] Modular Inverse
* [x] Coprimality
* [ ] Modular Exponentiation
* [ ] Prime Number Generation
* [ ] Fast Modular Exponentiation
* [ ] Euler's Totient Function

### RSA

* [ ] RSA key generation
* [ ] RSA encryption
* [ ] RSA decryption
* [ ] RSA testing
* [ ] RSA demonstration

---

## Current Implementation

### Shift Cipher

The first implemented algorithm is the Shift Cipher.

The encryption transformation is:

`C = (P + K) mod 26`

where:

* `P` is the numerical value of the plaintext letter
* `K` is the encryption key
* `C` is the numerical value of the ciphertext letter

The alphabet is represented numerically:

```text
A = 0
B = 1
C = 2
...
Z = 25
```

For example, using a key of `3`:

```text
H = 7

(7 + 3) mod 26 = 10

10 = K
```

Therefore:

```text
H → K
```

The implementation applies this transformation to every character in the plaintext.

#### Decryption

Decryption reverses the transformation:

`P = (C - K) mod 26`

where:

* `C` is the numerical value of the ciphertext letter
* `K` is the encryption key
* `P` is the numerical value of the recovered plaintext letter

The implementation also performs text preprocessing by converting input to uppercase and removing spaces, punctuation, and numbers.

---

### Affine Cipher

The Affine Cipher is the second classical cipher implemented in this project.

Unlike the Shift Cipher, which uses only addition, the Affine Cipher combines multiplication and addition using modular arithmetic.

The encryption transformation is:

`C = (aP + b) mod 26`

where:

* `P` is the numerical value of the plaintext letter
* `C` is the numerical value of the ciphertext letter
* `a` is the multiplication key
* `b` is the addition key

For example, using:

```text
a = 5
b = 8
```

and encrypting the letter `H`:

```text
H = 7

C = (5 × 7 + 8) mod 26

C = 43 mod 26

C = 17
```

Since `17 = R`:

```text
H → R
```

#### Decryption

Decryption requires the modular inverse of `a`.

The decryption transformation is:

`P = a⁻¹(C - b) mod 26`

For example, when:

```text
a = 5
```

the modular inverse of `5` modulo `26` is:

```text
5⁻¹ mod 26 = 21
```

because:

```text
(5 × 21) mod 26 = 1
```

Therefore, the inverse can be used to recover the original plaintext.

#### Affine Cipher Key Requirement

For the Affine Cipher to be reversible, `a` must have a modular inverse modulo `26`.

A modular inverse exists only when:

`gcd(a, 26) = 1`

Therefore, `a` must be coprime with `26`.

For example:

```text
gcd(5, 26) = 1
```

so `a = 5` is a valid key.

However:

```text
gcd(2, 26) = 2
```

so `a = 2` is not a valid key.

The implementation therefore validates the Affine Cipher keys before encryption and decryption.

#### Implementation

The Affine Cipher is implemented using mathematical utilities developed earlier in the project:

* `maths/gcd.py` — calculates the Greatest Common Divisor
* `maths/extended_euclidean.py` — calculates the coefficients required for modular inverses
* `maths/modular_inverse.py` — calculates modular inverses
* `maths/coprime.py` — determines whether two numbers are coprime
* `maths/affine_keys.py` — validates Affine Cipher keys
* `ciphers/affine_cipher.py` — implements Affine Cipher encryption and decryption

The Affine Cipher is tested using Python's `unittest` framework.

The tests cover:

* Encryption
* Decryption
* Encryption followed by decryption
* Invalid keys
* Text cleaning
* Key normalisation

---

## Mathematical Foundations

The cryptographic algorithms in this project are supported by mathematical algorithms implemented from first principles.

### Greatest Common Divisor

The Greatest Common Divisor (GCD) is calculated using the Euclidean Algorithm.

The algorithm is based on the identity:

`gcd(a, b) = gcd(b, a mod b)`

The process continues until the remainder becomes zero.

For example:

```text
gcd(48, 18)

48 mod 18 = 12

gcd(48, 18) = gcd(18, 12)

18 mod 12 = 6

gcd(18, 12) = gcd(12, 6)

12 mod 6 = 0
```

Therefore:

```text
gcd(48, 18) = 6
```

The GCD is important to the project because it is used to determine whether numbers are coprime.

---

### Extended Euclidean Algorithm

The Extended Euclidean Algorithm extends the Euclidean Algorithm by finding integers `x` and `y` such that:

`ax + by = gcd(a, b)`

For example, when:

```text
a = 5
b = 26
```

the algorithm finds values of `x` and `y` satisfying:

`5x + 26y = 1`

One solution is:

```text
x = -5
y = 1
```

because:

```text
5(-5) + 26(1) = 1
```

This is important for cryptography because the value of `x` can be used to calculate a modular inverse when:

`gcd(a, b) = 1`

---

### Modular Inverse

The modular inverse of `a` modulo `m` is a number `x` satisfying:

`(a × x) mod m = 1`

A modular inverse exists only when:

`gcd(a, m) = 1`

The project calculates modular inverses using the Extended Euclidean Algorithm rather than searching through possible values.

For example:

`5⁻¹ mod 26 = 21`

because:

`(5 × 21) mod 26 = 1`

Modular inverses are required for decrypting the Affine Cipher and will later be used in RSA.

---

### Coprimality

Two integers are coprime if their Greatest Common Divisor is equal to `1`.

Mathematically:

`gcd(a, b) = 1`

The project implements a reusable `is_coprime()` function to determine whether two numbers are coprime.

Coprimality is particularly important for the Affine Cipher because the multiplication key `a` must be coprime with `26`.

---

## Project Structure

```text
crypto_project/
│
├── README.md
├── main.py
├── .gitignore
│
├── ciphers/
│   ├── __init__.py
│   ├── shift_cipher.py
│   └── affine_cipher.py
│
├── maths/
│   ├── __init__.py
│   ├── alphabet.py
│   ├── gcd.py
│   ├── extended_euclidean.py
│   ├── modular_inverse.py
│   ├── coprime.py
│   └── affine_keys.py
│
├── tests/
│   ├── test_shift_cipher.py
│   ├── test_gcd.py
│   ├── test_extended_euclidean.py
│   ├── test_modular_inverse.py
│   ├── test_coprime.py
│   ├── test_affine_cipher.py
│   └── test_affine_keys.py
│
└── docs/
```

### `ciphers/`

Contains implementations of the cryptographic algorithms.

### `maths/`

Contains reusable mathematical utilities used by the cryptographic algorithms.

### `tests/`

Contains automated tests used to verify that the implementations behave as expected.

### `docs/`

Contains additional explanations of the mathematics and algorithms used throughout the project.

---

## Testing

The project uses Python's built-in `unittest` framework for automated testing.

Tests can be executed from the project root using:

```bash
python -m unittest discover -s tests
```

The tests currently cover:

### Shift Cipher

* Encryption
* Decryption
* Alphabet wrap-around
* Encryption followed by decryption

### Mathematical Foundations

* Greatest Common Divisor
* Extended Euclidean Algorithm
* Modular Inverse
* Coprimality

### Affine Cipher

* Encryption
* Decryption
* Encryption followed by decryption
* Invalid keys
* Text cleaning
* Key normalisation

---

## Development Approach

The project is being developed incrementally.

Each algorithm is implemented by first understanding its mathematical definition and then translating that definition into Python.

The development process follows this general approach:

```text
Mathematical concept
        ↓
Mathematical formula
        ↓
Python implementation
        ↓
Unit tests
        ↓
Documentation
```

This approach is intended to make the connection between the mathematics and the software explicit.

Rather than relying on existing cryptography libraries, the mathematical building blocks are implemented directly wherever practical.

The project will progressively move from simple classical ciphers to the number-theoretic foundations required for RSA.

---

## Future Goals

The long-term goal of the project is to implement RSA from first principles.

Before implementing RSA, the project will build the required mathematical foundations, including:

* Modular exponentiation
* Prime number generation
* Euler's Totient Function
* Modular inverses
* RSA key generation

The final implementation will demonstrate how these mathematical concepts come together to form the RSA cryptosystem.
