# comp-theory

This repository contains the solutions for the Computational Theory assessment.  
All solutions are implemented in the notebook `.vscode/problems.ipynb`, following the instructions in the GitHub provided for the assessment.  
The repository is structured to demonstrate a clear workflow, consistent development, reproducibility, and professional documentation.

---

## 📘 Problem 1 — Secure Hash Standard: Binary Word Operations

Problem 1 involves implementing the 32-bit word operations defined in the Secure Hash Standard (SHA-256), including:

- Logical functions: `Parity`, `Ch`, `Maj`
- SHA-256 mixing functions: `Σ0`, `Σ1`, `σ0`, `σ1`
- Helper functions: `ROTR`, `SHR`

All functions are implemented using **NumPy** to ensure correct unsigned 32-bit behaviour (`np.uint32`).  
The notebook includes:

- Full Markdown explanations of each concept  
- Clear docstrings  
- Clean code and comments
- Tests verifying correctness  
- A structured narrative suitable for an informed computing professional  

---

## 📘 Problem 2 — Fractional Parts of Cube Roots

This problem reproduces the derivation of the 64 SHA-256 round constants defined in
NIST FIPS 180-4 (page 11). The constants are generated from the fractional parts of the
cube roots of the first 64 prime numbers.

The notebook:

- Generates the first 64 prime numbers using a simple trial-division algorithm.
- Computes cube roots, extracts the fractional parts, and scales them by \(2^{32}\).
- Casts the results to `np.uint32` and formats them as eight-character hexadecimal values.
- Verifies programmatically that all computed constants exactly match those published
  in the Secure Hash Standard.

This confirms that the constants used in SHA-256 are deterministically derived from
well-defined mathematical properties rather than chosen arbitrarily.

## 📘 Problem 3 — Padding (Block Parsing)

This problem implements the message padding and block parsing stage of the SHA-256
algorithm, as specified in NIST FIPS 180-4 (§5.1.1 and §5.2.1).

A generator function `block_parse(msg)` is used to process an input message into
512-bit (64-byte) blocks by:

- Appending a single `1` bit (represented as `0x80`).
- Padding with `0` bits until the message length is congruent to 56 modulo 64.
- Appending the original message length as a 64-bit big-endian integer (in bits).

The notebook includes tests covering key boundary cases (empty input, 55-byte,
56-byte, and 64-byte messages) to verify correct padding behaviour and block output.
A formatted hexadecimal dump is also provided to visually inspect padded blocks.

## 📘 Problem 4 — Hashes (SHA-256 Compression Function)

This problem implements the SHA-256 compression function as specified in
NIST FIPS 180-4 (§6.2.2). Given the current intermediate hash state and a
512-bit message block, the function computes the next hash state.

The implementation:

- Constructs the 64-entry message schedule from each 512-bit block.
- Executes the 64-round SHA-256 compression loop using the standard logical
  functions (`Ch`, `Maj`, `Σ0`, `Σ1`) and round constants.
- Updates the intermediate hash state using 32-bit unsigned arithmetic.

The compression function is validated end-to-end by combining it with the
padding and block parsing logic from Problem 3 and comparing the resulting
digests against Python’s `hashlib.sha256` for multiple known test vectors.
 
## 📘 Problem 5 — Passwords (Dictionary Attack)

This problem demonstrates a dictionary attack against unsalted, single-round SHA-256
password hashes. Candidate passwords are UTF-8 encoded, hashed, and compared against
the target digests.

Using a small reproducible wordlist and common variants, one hash was recovered:

- `5e884898...d1542d8` → `password`

The notebook discusses why SHA-256 is unsuitable for password storage and recommends
defences such as unique salts and slow password hashing algorithms (Argon2id/bcrypt/scrypt).


## Research Context and Related Work

This project is grounded in established cryptographic standards and security best practices.
The implementation and analysis are informed by authoritative specifications and widely accepted industry guidance, ensuring correctness, reproducibility, and relevance to real-world software engineering.

### Secure Hash Standard (SHA-256)

The SHA-256 algorithm implemented throughout this repository follows the specification defined in the National Institute of Standards and Technology Secure Hash Standard (FIPS 180-4).

The project reproduces multiple components described in the standard, including:

- 32-bit logical word operations (Ch, Maj, Σ0, Σ1, σ0, σ1)

- Generation of round constants from fractional cube roots of prime numbers

- Message padding and block parsing rules

- The SHA-256 compression function (§6.2.2)

All derived constants and final hash outputs are validated against the official values published by NIST, ensuring full compliance with the standard.

### Reference Implementations

To validate correctness, the custom SHA-256 implementation is compared against Python’s standard library reference implementation provided by Python Software Foundation via the hashlib module.

Matching outputs across multiple test vectors confirm that the algorithm behaves identically to a widely used, production-grade implementation, reinforcing confidence in correctness.

### Password Hashing and Security Best Practices

Problem 5 demonstrates a dictionary attack against unsalted, single-round SHA-256 password hashes.
This approach reflects well-documented weaknesses in using fast cryptographic hash functions for password storage.

Modern security guidance from the OWASP highlights that general-purpose hash functions such as SHA-256 are unsuitable for password storage due to their speed and vulnerability to offline attacks.

Industry-recommended defences include:

- Unique per-user salts to prevent precomputation attacks

- Memory-hard, deliberately slow password hashing algorithms such as Argon2id, bcrypt, or scrypt

The project’s analysis aligns with these recommendations and explains why the demonstrated attack succeeds against weak hashing schemes but would be ineffective against modern password storage mechanisms.


## References

1. National Institute of Standards and Technology
Secure Hash Standard (FIPS 180-4)
https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf

2. Python Software Foundation
hashlib — Secure hashes and message digests
https://docs.python.org/3/library/hashlib.html

3. OWASP
Password Storage Cheat Sheet
https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html

4. Internet Engineering Task Force
RFC 9106 — Argon2 Memory-Hard Function for Password Hashing
https://www.rfc-editor.org/rfc/rfc9106.html


## How to Run the Notebook (GitHub Codespaces)

This repository is designed to be run directly inside GitHub Codespaces, ensuring reproducibility and simplifying setup.

### To run:

1. Open the repository on GitHub.
2. Click the green “Code” button.
3. Select Create a Codespace on main.
4. Once the Codespace loads, open `.vscode/problems.ipynb`.
5. Run the notebook cells in order.


