import requests
import tkinter as tk
from tkinter import messagebox

URL_PRIMARY = "https://economia.awesomeapi.com.br/json/last/"

def conversor(moeda1, valor1, moeda2):
    url = URL_PRIMARY + moeda1 + "-" + moeda2
    siglas = moeda1 + moeda2
    try:
        response = requests.get(url)
        response.raise_for_status()
        sigla = response.json().get(siglas)
        if sigla:
            res = float(sigla.get('bid')) * valor1
            resultado_label.config(text=f"{valor1} {moeda1} = {res:.2f} {moeda2}\nData: {sigla.get('create_date')}")
        else:
            messagebox.showerror("Erro", "Moeda não encontrada.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro", f"Erro na requisição: {e}")

def realizar_conversao():
    moeda1 = moeda1_entry.get().upper()
    valor1 = valor1_entry.get()
    moeda2 = moeda2_entry.get().upper()
    
    if not moeda1 or not valor1 or not moeda2:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
        return
    
    try:
        valor1 = float(valor1)
        conversor(moeda1, valor1, moeda2)
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido para conversão.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Conversor de Moedas")

# Labels
tk.Label(root, text="Moeda de Origem (ex: USD):").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Valor:").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="Moeda de Destino (ex: BRL):").grid(row=2, column=0, padx=10, pady=10)

# Entradas
moeda1_entry = tk.Entry(root)
moeda1_entry.grid(row=0, column=1, padx=10, pady=10)

valor1_entry = tk.Entry(root)
valor1_entry.grid(row=1, column=1, padx=10, pady=10)

moeda2_entry = tk.Entry(root)
moeda2_entry.grid(row=2, column=1, padx=10, pady=10)

# Botão de conversão
converter_button = tk.Button(root, text="Converter", command=realizar_conversao)
converter_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label para exibir o resultado
resultado_label = tk.Label(root, text="", fg="blue")
resultado_label.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar a interface
root.mainloop()