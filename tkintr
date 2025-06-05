import tkinter as tk

def clicar(botao):
    n1 = str(entrada.get())
    if botao == "=":
        try:
            resultado = eval(n1)
            entrada.delete(0, tk.END)
            entrada.insert(0, str(resultado))
        except:
            entrada.delete(0, tk.END)
            entrada.insert(0, "Erro")
    elif botao == "C":
        entrada.delete(0, tk.END)
    else:
        entrada.insert(tk.END, botao)

# janela
janela = tk.Tk()
janela.title('calculadorabb')

# campo de entrada
entrada = tk.Entry(janela, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# botoes
botoes = [
    "1", "2", "3", "/",
    "4", "5", "6", "*",
    "7", "8", "9", "-",
    "C", "0", "=", "+"
]

linha = 1
coluna = 0
for botao in botoes:
    comando = lambda x=botao: clicar(x)
    tk.Button(janela, text=botao, width=5, height=2, font=("Arial", 18),
              command=comando).grid(row=linha, column=coluna, padx=5, pady=5)
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Inicia a aplicação
janela.mainloop()
