import tkinter as tk
from tkinter import ttk
import json
import os

def submit_data():
    data = {
        "Produtor": producer_entry.get(),
        "Numero de Aves": birds_entry.get(),
        "Peso Medio": weight_entry.get(),
        "Carga": load_entry.get()
    }
    
    # Salva os dados em um arquivo JSON
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
    
    producer_entry.delete(0, tk.END)
    birds_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    load_entry.delete(0, tk.END)

app = tk.Tk()
app.title("Entrada de Dados")

tk.Label(app, text="Produtor:").grid(row=0, column=0)
producer_entry = ttk.Entry(app)
producer_entry.grid(row=0, column=1)

tk.Label(app, text="Número de Aves:").grid(row=1, column=0)
birds_entry = ttk.Entry(app)
birds_entry.grid(row=1, column=1)

tk.Label(app, text="Peso Médio:").grid(row=2, column=0)
weight_entry = ttk.Entry(app)
weight_entry.grid(row=2, column=1)

tk.Label(app, text="Carga:").grid(row=3, column=0)
load_entry = ttk.Entry(app)
load_entry.grid(row=3, column=1)

submit_button = ttk.Button(app, text="Enviar", command=submit_data)
submit_button.grid(row=4, column=0, columnspan=2)

app.mainloop()
