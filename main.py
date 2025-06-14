import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from tkinter import filedialog
from cipher.keyschedule import generate_subkeys
from cipher.sbox import print_log_sbox, generate_sbox
from cipher.sbox import generate_sbox
from cipher.core import encrypt_file, decrypt_file, encrypt_block
import os
import hashlib
import random

class CryptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciados de Criptografia da Inn Seguros")
        self.root.geometry("500x300")
        self.root.resizable(True, True)
        self.file_path = tk.StringVar()
        self.key = tk.StringVar()
        self.mode = tk.StringVar(value="encrypt")
        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.exit_system)

    def create_widgets(self):
        ttk.Label(self.root, text="Sistema de Criptografia - Inn Seguros", font=("Arial", 14)).pack(pady=5)
        frame_file= ttk.Frame(self.root)
        frame_file.pack(pady=5)
        ttk.Entry(frame_file, textvariable=self.file_path, width=40, state="readonly").pack(side="left", padx=5)
        ttk.Button(frame_file, text="Selecione o arquivo", command=self.choose_file).pack(side="left") 
        frame_mode = ttk.Frame(self.root)
        frame_mode.pack(pady=10)
        ttk.Radiobutton(frame_mode, text="Realizar Encriptação", variable=self.mode, value="encrypt").pack(side="left", padx=20)
        ttk.Radiobutton(frame_mode, text="Realizar Decriptação", variable=self.mode, value="decrypt").pack(side="left", padx=20)
        ttk.Button(self.root, text="Executar",  command=self.execute).pack(pady=15)
        ttk.Button(self.root, text="Mostrar Rounds", command=self.mostrar_rounds).pack(pady=5)
        self.label_status = ttk.Label(self.root, text="", foreground="green")
        self.label_status.pack(pady=5)
        self.text_log = tk.Text(self.root, height=10, width=60, state='disabled')
        self.text_log = tk.Text(self.root, height=10, width=60, state='disabled')

    def choose_file(self):
        file = filedialog.askopenfilename(
            title="Selecione o arquivo",
            filetypes=[("All Files", "*.*")]
        )
        if file:
            self.file_path.set(file)
        
    def entry_validation(self):
        if not self.file_path.get() or not os.path.isfile(self.file_path.get()):
            messagebox.showerror("Aviso","Selecione um arquivo válido")
            return False
        return True
    
    def mostrar_rounds(self):
        block = 0x12345678  
        key_a = 'A1B2C3D4'
        key_b = 'A1B2C3D5'  
        log_a, log_b = [], []
        sub_a = generate_subkeys(key_a)
        sbox_a = generate_sbox(key_a.encode())
        encrypt_block(block, sub_a, sbox_a, verbose_log=log_a)
        sub_b = generate_subkeys(key_b)
        sbox_b = generate_sbox(key_b.encode())
        encrypt_block(block, sub_b, sbox_b, verbose_log=log_b)
        janela = tk.Toplevel(self.root)
        janela.title("Resultado Round a Round")
        janela.geometry("800x400")
        txt = tk.Text(janela, wrap="none", font=("Courier", 10))
        txt.pack(fill="both", expand=True)
        txt.insert("end", f"Chave A: {key_a}\nChave B: {key_b}\n\n")
        txt.insert("end", f"{'Round':<6} {'Chave A':<35} {'Chave B':<35}\n")
        txt.insert("end", "-" * 80 + "\n")
        for i in range(len(log_a)):
            txt.insert("end", f"{i+1:<6} {log_a[i]:<35} {log_b[i]}\n")
        txt.config(state="disabled")
            
    def execute(self):
        if not self.entry_validation():
            return
        file = self.file_path.get()
        key = self.key.get()
        mode = self.mode.get()
        try:
            if mode == "encrypt":
                generated_key = ''.join(random.choices('0123456789ABCDEF', k=8))
                self.key.set(generated_key)
                output_path = encrypt_file(file, generated_key)
                messagebox.showinfo("Encriptação", f"Arquivo encriptado com sucesso!\nSalvo em:\n{output_path}")
            else:
                output_path = decrypt_file(file, self.key.get())
                messagebox.showinfo("Decriptação", f"Arquivo decriptado com sucesso!\nSalvo em:\n{output_path}")
            self.label_status.config(text=f"Processamento concluído.\nArquivo salvo em:\n{output_path}", foreground="green")
            with open(file, 'rb') as f:
                content = f.read()
            seed = hashlib.sha256(content).digest()
            sbox = generate_sbox(seed)
            sbox_log = print_log_sbox(sbox)
            self.text_log.config(state='normal')
            self.text_log.delete(1.0, tk.END)
            self.text_log.insert(tk.END, sbox_log)
            self.text_log.config(state='disabled')
        except Exception as e:
            messagebox.showerror("Erro",f"Algo deu errado no seguinte processamento: {str(e)}")
            self.label_status.config(text="Erro durante o processamento", foreground="red")

    def exit_system(self):
        if messagebox.askyesno("Sair","Tem certeza que deseja sair?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptApp(root)
    root.mainloop()