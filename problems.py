# Secure Hash Standard: Binary Word Operations (Problem 1)

## Introduction

'''
This notebook forms part of the assessment for the comp theory.  
Problem 1 focuses on implementing a set of 32-bit word operations used in the **Secure Hash Standard (SHA-256)**.  
These operations include logical functions such as `Ch`, `Maj`, `Parity`, and bitwise rotation/shift functions such as `Σ0`, `Σ1`, `σ0`, and `σ1`.

All functions will be implemented in Python using **NumPy**, ensuring that all values behave as unsigned 32-bit integers (`np.uint32`).  
Each function will include:
- a detailed docstring  
- a Markdown explanation  
- tests verifying correctness  

This structure ensures clarity, reproducibility, and suitability for an informed computing professional reviewing the code.
'''

