# 🔐 Projeto de Criptografia Simétrica - Inn Seguros

🇧🇷 **Descrição (Português)**  
Este projeto acadêmico implementa um sistema de criptografia simétrica de 32 bits com 3 rodadas, utilizando substituição e permutação dependentes da chave. Ele permite criptografar e descriptografar arquivos de forma simples, porém segura, com base em blocos binários. O algoritmo foi desenvolvido com foco em aprendizado de fundamentos de segurança da informação, como geração de subchaves, substituição não linear (S-box) e permutação pseudoaleatória.

- A interface gráfica (Tkinter) permite ao usuário selecionar arquivos e visualizar logs da S-box gerada.
- A chave é automaticamente gerada se o usuário não fornecer uma (32 bits = 8 caracteres hexadecimais).
- O processo é completamente reversível, permitindo recuperar os arquivos originais com a chave correta.

---

🇺🇸 **Description (English)**  
This academic project implements a 32-bit symmetric block cipher with 3 rounds, using key-dependent substitution and permutation. It allows users to encrypt and decrypt files simply but securely through a graphical interface. The algorithm was designed to support learning in information security fundamentals, including subkey generation, non-linear substitution (S-box), and pseudo-random permutation.

- The GUI (Tkinter) lets users select files and view logs of the generated S-box.
- If no key is provided by the user, a random 32-bit (8 hexadecimal characters) key is generated automatically.
- The process is fully reversible, allowing full recovery of the original file using the correct key.

---

🛠️ **Tecnologias / Technologies**
- Python 3.12+
- Tkinter
- Pytest (para testes unitários)
- Estrutura modular (`core`, `keyschedule`, `sbox`, `permutation`, `utils`, `tests`)

---

📁 **Como usar / How to use**

1. Clone este repositório / Clone this repository
2. Instale as dependências / Install dependencies:
   ```bash
   pip install -r requirements.txt
