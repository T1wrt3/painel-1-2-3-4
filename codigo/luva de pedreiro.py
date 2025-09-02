import tkinter as tk
from tkinter import PhotoImage

imagens = {
    1: ("imagens/feliz.png", "Feliz"),
    2: ("imagens/triste.png", "Triste"),
    3: ("imagens/raiva.png", "Raiva"),
    4: ("imagens/confuso.png", "confuso")
}

def mostrar_emocao(numero):
    dados = imagens.get(numero)
    if dados:
        caminho, nome = dados
        img = PhotoImage(file=caminho)
        label_imagem.config(image=img)
        label_imagem.image = img
        label_texto_emocao.config(text=nome)
    else:
        label_imagem.config(image="")
        label_imagem.image = None
        label_texto_emocao.config(text="Número inválido")

def on_input_change(event):
    valor = entry_numero.get()
    if valor.isdigit():
        mostrar_emocao(int(valor))
    else:
        label_texto_emocao.config(text="Digite um número válido")

root = tk.Tk()
root.title("Painel de Emoções")
root.configure(bg="lightgray")

texto = tk.Label(root, text="Selecione um número de 1 a 4", font=("Arial", 14), bg="lightgray")
texto.pack(pady=10)

frame_botoes = tk.Frame(root, bg="lightgray")
frame_botoes.pack(pady=10)

for numero, (_, nome) in imagens.items():
    frame = tk.Frame(frame_botoes, bg="lightgray")
    frame.grid(row=0, column=numero-1, padx=10)
    btn = tk.Button(frame, text=str(numero), font=("Arial", 20),
                    width=5, command=lambda n=numero: mostrar_emocao(n))
    btn.pack()
    lbl = tk.Label(frame, text=nome, font=("Arial", 12), bg="lightgray")
    lbl.pack()

frame_input = tk.Frame(root, bg="lightgray")
frame_input.pack(pady=10)

entry_numero = tk.Entry(frame_input, font=("Arial", 14), width=5)
entry_numero.pack(side="left", padx=5)

# 🔥 Evento que dispara toda vez que o texto do Entry muda
entry_numero.bind("<KeyRelease>", on_input_change)

label_imagem = tk.Label(root, bg="lightgray")
label_imagem.pack(pady=10)

label_texto_emocao = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="lightgray")
label_texto_emocao.pack(pady=5)

root.mainloop()
