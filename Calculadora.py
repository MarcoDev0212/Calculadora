# Calculadora que Soma

import tkinter as tk

def limpar_campos():
    entry_num1.delete(0, tk.END)     # Limpa o conteúdo do primeiro campo de entrada
    entry_num2.delete(0, tk.END)     # Limpa o conteúdo do segundo campo de entrada
    label_resultado.config(text="")  # Limpa o texto do rótulo do resultado

# Função para calcular a Soma:
def calcular_soma():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, insira números válidos!")

# Função para calcular a Subtração:
def calcular_sub():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 - num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, insira números válidos!")

# Função para calcular a Multiplicação:        
def calcular_mult():
    try: 
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 * num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, insira números validos")

# Função para calcular a Divisão:            
def calcular_div():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 / num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, insira números validos")

# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Criando os elementos da interface
label_num1 = tk.Label(janela, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(janela, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

botao_somar = tk.Button(janela, text="Somar", command=calcular_soma)
botao_somar.grid(row=2, column=0, padx=10, pady=5)

botao_subtrair = tk.Button(janela, text="Subtrair", command=calcular_sub)
botao_subtrair.grid(row=2, column=1, padx=10, pady=5)

botao_multiplicao = tk.Button(janela, text="Multiplicação", command=calcular_mult)
botao_multiplicao.grid(row=3, column=0, padx=10, pady=5)

botao_divisao = tk.Button(janela, text="Divisão", command=calcular_div)
botao_divisao.grid(row=3, column=1, padx=10, pady=5)

botao_limpar = tk.Button(janela, text="Limpar", command=limpar_campos)
botao_limpar.grid(row=4, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(janela, text="Resultado:")
label_resultado.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar o loop da interface
janela.mainloop()


