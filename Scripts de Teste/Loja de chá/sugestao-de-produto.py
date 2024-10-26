import tkinter as tk
from tkinter import messagebox

# Função para sugerir chas com preços mais baixos com base em um cogumelo desejado.
def sugerir_chas(cha_desejado):
    catalogo = {
        "Frutas Vermelhas": 10,
        "Mate": 8,
        "Camomila": 6,
        "Erva-Doce": 12,
        "Capim-Santo": 16,
        "Erva-Cidreira": 16
    }

    # Verifica se o cha desejado está no catálogo
    if cha_desejado in catalogo:
        valor_desejado = catalogo[cha_desejado]
        sugestoes = []
        
        # Procura por chas mais baratos no catálogo
        for cha, valor in catalogo.items():
            if valor < valor_desejado and cha != cha_desejado:
                sugestoes.append(f"{cha} - Valor: {valor}")
                if len(sugestoes) == 2:
                    break
        
        if not sugestoes:
            return "Desculpe, não há sugestões disponíveis."
        else:
            return "\n".join(sugestoes)
    else:
        return "Chá não encontrado no catálogo."

# Função de callback para o botão de sugestões
def gerar_sugestoes():
    cha_desejado = entrada.get()
    if cha_desejado:
        resultado = sugerir_chas(cha_desejado)
        messagebox.showinfo("Sugestões de Chás", resultado)
    else:
        messagebox.showwarning("Aviso", "Por favor, insira o nome de um chá!")

# Criando a janela principal
janela = tk.Tk()
janela.title("Catálogo de Chás")
janela.geometry("400x200")

# Texto de instrução
instrucoes = tk.Label(janela, text="Digite o nome de um chá para sugestões:")
instrucoes.pack(pady=10)

# Campo de entrada para o nome do cha
entrada = tk.Entry(janela, width=30)
entrada.pack(pady=5)

# Botão para gerar sugestões
botao_sugerir = tk.Button(janela, text="Gerar Sugestões", command=gerar_sugestoes)
botao_sugerir.pack(pady=10)

# Rodar a janela principal
janela.mainloop()
