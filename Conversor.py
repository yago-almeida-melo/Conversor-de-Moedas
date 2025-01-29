import requests
import tkinter as tk
from tkinter import *

URL_PRIMARY = "https://economia.awesomeapi.com.br/json/last/"

class App:
    def __init__(self):
        self.screen = tk.Tk()
        self.tela()
        self.screen.mainloop()

    def tela(self):
        # Configuração da interface gráfica
        self.screen.title("Conversor de Moedas")
        self.screen.configure(background='black')  # Fundo preto
        self.screen.geometry("400x300")  # Tamanho inicial da janela
        self.screen.resizable(False, False)  # Impede redimensionamento

        # Frame principal
        self.frame_1 = Frame(self.screen, bg='black')
        self.frame_1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        # Labels (com cores contrastantes)
        tk.Label(
            self.frame_1, 
            text="Moeda de Origem (ex: USD):", 
            bg='black', fg='white', font=('Arial', 10)
        ).grid(row=0, column=0, padx=10, pady=10, sticky='w')

        tk.Label(
            self.frame_1, 
            text="Valor:", 
            bg='black', fg='white', font=('Arial', 10)
        ).grid(row=1, column=0, padx=10, pady=10, sticky='w')

        tk.Label(
            self.frame_1, 
            text="Moeda de Destino (ex: BRL):", 
            bg='black', fg='white', font=('Arial', 10)
        ).grid(row=2, column=0, padx=10, pady=10, sticky='w')

        # Entradas (campos de texto)
        self.moeda1_entry = tk.Entry(
            self.frame_1, 
            bg='white', fg='black', font=('Arial', 10), insertbackground='black'
        )
        self.moeda1_entry.grid(row=0, column=1, padx=10, pady=10)

        self.valor1_entry = tk.Entry(
            self.frame_1, 
            bg='white', fg='black', font=('Arial', 10), insertbackground='black'
        )
        self.valor1_entry.grid(row=1, column=1, padx=10, pady=10)

        self.moeda2_entry = tk.Entry(
            self.frame_1, 
            bg='white', fg='black', font=('Arial', 10), insertbackground='black'
        )
        self.moeda2_entry.grid(row=2, column=1, padx=10, pady=10)

        # Botão de conversão (estilizado)
        converter_button = tk.Button(
            self.frame_1, 
            text="Converter", 
            command=self.realizar_conversao, 
            bg='blue', fg='white', font=('Arial', 10, 'bold'), 
            relief='flat', activebackground='darkblue', activeforeground='white'
        )
        converter_button.grid(row=3, column=0, columnspan=2, pady=20)

        # Label para exibir o resultado (estilizado)
        self.resultado_label = tk.Label(
            self.frame_1, 
            text="", 
            bg='black', fg='green', font=('Arial', 12, 'bold')
        )
        self.resultado_label.grid(row=4, column=0, columnspan=2, pady=8)

    def conversor(self, moeda1, valor1, moeda2):
        url = URL_PRIMARY + moeda1 + "-" + moeda2
        siglas = moeda1 + moeda2
        try:
            response = requests.get(url)
            response.raise_for_status()
            sigla = response.json().get(siglas)
            if sigla:
                res = float(sigla.get('bid')) * valor1
                self.resultado_label.config(text=f"{valor1} {moeda1} = {res:.2f} {moeda2}\nData: {sigla.get('create_date')}")
            else:
                messagebox.showerror("Erro", "Moeda não encontrada.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro", f"Erro na requisição: {e}")

    def realizar_conversao(self):
        moeda1 = self.moeda1_entry.get().upper()
        valor1 = self.valor1_entry.get()
        moeda2 = self.moeda2_entry.get().upper()

        if not moeda1 or not valor1 or not moeda2:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        try:
            valor1 = float(valor1)
            self.conversor(moeda1, valor1, moeda2)
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido para conversão.")

if __name__ == "__main__":
    app = App()