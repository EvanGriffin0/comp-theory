# comp-theory

This repository contains the solutions for the Computational Theory assessment.  
All solutions are implemented in the notebook `problems.ipynb` at the root of the repository, following the instructions in the github provided for the assessment.  
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

## How to Run the Notebook (GitHub Codespaces)

This repository is designed to be run directly inside GitHub Codespaces, ensuring reproducibility and simplifying setup.

### To run:

1. Open the repository on GitHub.
2. Click the green “Code” button.
3. Select Create a Codespace on main.
4. Once the Codespace loads, open `problems.ipynb`.
5. Run the notebook cells in order 
6. The second last cell contains the test function that once ran will output the results of the tests

