import tkinter as tk
from tkinter import messagebox

def bin_to_dec():
    b1 = entry.get()
    try:
        dec = int(b1, 2)
        result_label.config(text=f"decimal: {dec}")
    except ValueError:
        messagebox.showerror("Erro", "numero binário inválido")

def dec_to_bin():
    dec_num = entry.get()
    try:
        dec = int(dec_num)
        bin_result = bin(dec)[2:]
        result_label.config(text=f"binario: {bin_result}")
    except ValueError:
        messagebox.showerror("erro", "Numero decimal inválido")

# janela
root = tk.Tk()
root.title('conversor')
root.geometry("300x200")
root.resizable(False, False)

# Campo de entrada
entry = tk.Entry(root, width=25, font=('Arial', 14))
entry.pack(pady=10)

# Botões
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

btn_bin_to_dec = tk.Button(btn_frame, text="Binario para Decimal", command=bin_to_dec)
btn_bin_to_dec.grid(row=0, column=0, padx=5)

btn_dec_to_bin = tk.Button(btn_frame, text="decimal para Binário", command=dec_to_bin)
btn_dec_to_bin.grid(row=0, column=1, padx=5)

# Resultado
result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.pack(pady=20)

# Iniciar loop da interface
root.mainloop()
