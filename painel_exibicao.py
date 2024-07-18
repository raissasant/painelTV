import tkinter as tk
import json
import os
from datetime import datetime
from PIL import Image, ImageTk

def load_data():
    if os.path.exists('data.json'):
        with open('data.json', 'r') as infile:
            data = json.load(infile)
            producer_label.config(text=f"Produtor: {data.get('Produtor', '')}")
            birds_label.config(text=f"Número de Aves: {data.get('Numero de Aves', '')}")
            weight_label.config(text=f"Peso Médio: {data.get('Peso Medio', '')}")
            load_label.config(text=f"Carga: {data.get('Carga', '')}")
    
    # Atualiza a hora e a data
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    time_label.config(text=f"Hora Atual: {current_time}")
    date_label.config(text=f"Data Atual: {current_date}")
    
    app.after(1000, load_data)  # Atualiza os dados a cada 1 segundo

app = tk.Tk()
app.title("Painel de Exibição")
app.attributes('-fullscreen', True)

# Carrega o logotipo da empresa
logo_path = os.path.join('img', 'logo.png')
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((200, 200))  # Redimensiona a imagem, se necessário
logo_photo = ImageTk.PhotoImage(logo_image)

# Adiciona o logotipo da empresa
logo_label = tk.Label(app, image=logo_photo)
logo_label.pack(pady=20)

# Adiciona o nome Agroaraçá - Painel na cor vinho
title_label = tk.Label(app, text="Agroaraçá - Painel", font=("Helvetica", 32, "bold"), fg="#800020")
title_label.pack(pady=20)

# Frame para agrupar data e hora lado a lado
datetime_frame = tk.Frame(app)
datetime_frame.pack(pady=20)

time_label = tk.Label(datetime_frame, text="Hora Atual: ", font=("Helvetica", 24))
time_label.pack(side=tk.LEFT, padx=10)

date_label = tk.Label(datetime_frame, text="Data Atual: ", font=("Helvetica", 24))
date_label.pack(side=tk.LEFT, padx=10)

producer_label = tk.Label(app, text="Produtor: ", font=("Helvetica", 24))
producer_label.pack(pady=20)

birds_label = tk.Label(app, text="Número de Aves: ", font=("Helvetica", 24))
birds_label.pack(pady=20)

# Frame para agrupar peso medio e carga lado a lado
weight_load_frame = tk.Frame(app)
weight_load_frame.pack(pady=20)

weight_label = tk.Label(weight_load_frame, text="Peso Médio: ", font=("Helvetica", 24))
weight_label.pack(side=tk.LEFT, padx=10)

load_label = tk.Label(weight_load_frame, text="Carga: ", font=("Helvetica", 24))
load_label.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(app, text="Sair", command=app.destroy, font=("Helvetica", 24))
exit_button.pack(pady=20)

load_data()
app.mainloop()
