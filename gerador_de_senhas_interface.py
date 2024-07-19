import tkinter as tk
from tkinter import ttk
import random
import string

#função de gerar senhas recebe tamanho da senha
def gerar_senha(comprimento):

    #uma string que recebe os elementos desejados na senha
    caracteres = string.ascii_letters + string.digits + string.punctuation

    #senha recebe a uniao desses elementos sem espaços de maneira aleatoria
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))

    return senha

#função de clicar no botao
def ao_clicar_no_botao():

    #recebe o tamanho da senha pelo get da box
    comprimento = int(entrada_comprimento.get())

    #senha recebe o return da função de gerar senha
    senha = gerar_senha(comprimento)

    #limpa a entrada se tiver algo escrito
    entrada_senha.delete(0, tk.END)

    #lança a senha na box de baixo
    entrada_senha.insert(0, senha)

#==============configs do tkinter=====================
janela = tk.Tk()
janela.title("Gerador de Senhas")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 22))
style.configure("TButton", font=("Arial", 22), padding=5)
style.configure("TEntry", font=("Arial", 22))

frame = ttk.Frame(janela, padding=50)
frame.grid(row=0, column=5, padx=100, pady=100)

#==============configs do tkinter=====================

#escrito do tamanho
rotulo_comprimento = ttk.Label(frame, text="Comprimento da senha:")
rotulo_comprimento.grid(row=0, column=0, sticky=tk.W, pady=10)

#box do tamanho
entrada_comprimento = ttk.Entry(frame, width=20)
entrada_comprimento.grid(row=0, column=1, padx=50, pady=30)

#botao de gerar
botao_gerar = ttk.Button(frame, text="Gerar Senha", width= 15, command=ao_clicar_no_botao)
botao_gerar.grid(row=0, column=3, columnspan=1, pady=5)

#escrito da senha gerada
rotulo_senha = ttk.Label(frame, width=15 ,text="Senha Gerada:")
rotulo_senha.grid(row=1, column=0, sticky=tk.W, pady=5)

#box da senha gerada
entrada_senha = ttk.Entry(frame, width=40)
entrada_senha.grid(row=1, column=1, padx=5)

#executando
janela.mainloop()
