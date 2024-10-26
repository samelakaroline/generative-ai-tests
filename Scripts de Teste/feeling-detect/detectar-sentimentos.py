import re
import tkinter as tk
from tkinter import messagebox

def carregar_palavras(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        palavras = f.read().splitlines()
    return palavras 

positivas = carregar_palavras('./datasets/positivas.txt')
negativas = carregar_palavras('./datasets/negativas.txt')
neutras = carregar_palavras('./datasets/neutras.txt')

def analyze_sentiment():
    # Obtém o comentário do usuário a partir da entrada na janela
    comentario = entry.get()

    # Divisão do comentário em palavras
    palavras = re.findall(r'\b\w+\b', comentario.lower())
    
    # Lista de palavras positivas, negativas e neutras
    #positivas = ["bom", "boa", "ótimo", "excelente", "maravilhoso", "gostei", "incrível"]
    #negativas = ["ruim", "péssimo", "horrível", "terrível", "odeio"]
    #neutras = ["mas", "deixou", "apesar", "embora"]

    # Contagem de palavras positivas, negativas e neutras
    count_positivo = sum(palavra in positivas for palavra in palavras)
    count_negativo = sum(palavra in negativas for palavra in palavras)
    count_neutro = sum(palavra in neutras for palavra in palavras)  

    # Verifica o sentimento predominante
    if count_positivo > count_negativo and count_neutro == 0:
        sentimento = "Positivo"
    elif count_negativo > count_positivo and count_neutro == 0:
        sentimento = "Negativo"
    else:
        sentimento = "Neutro"
    
    # Exibe o resultado em uma mensagem
    messagebox.showinfo("Resultado da Análise", f"Sentimento: {sentimento}")

# Função para encerrar o programa
def sair_programa():
    root.destroy()

# Configuração da janela principal do Tkinter
root = tk.Tk()
root.title("Análise de Sentimento")
root.geometry("400x250")

# Rótulo e entrada de texto
tk.Label(root, text="Digite seu comentário:").pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Botão para iniciar a análise
analyze_button = tk.Button(root, text="Analisar Sentimento", command=analyze_sentiment)
analyze_button.pack(pady=10)

# Botão para encerrar o programa
exit_button = tk.Button(root, text="Sair", command=sair_programa)
exit_button.pack(pady=10)

# Inicia a janela do Tkinter
root.mainloop()
