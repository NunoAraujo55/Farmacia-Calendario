import tkinter as tk
from tkinter import ttk
import datetime

def gerar_escala():
    # Ajuste os nomes aqui para combinar com o dicionário abaixo
    escala_farmacias = [
        "Chaves",
        "Costa Gomes",
        "Martins",
        "Barroso",
        "Pereira da Silva",
        "Maldonado",
        "Barreiros",
        "Nova Farmácia da Madalena",
        "Paula Files",
        "Farmácia da Nova Ponte",
        "Mariz"
    ]
    total_farmacias = len(escala_farmacias)
    
    escala_dias = {}
    
    for dia_ano in range(365):
        indice_farmacia = dia_ano % total_farmacias
        escala_dias[dia_ano] = escala_farmacias[indice_farmacia]
    
    return escala_dias

def obter_farmacia(dia, mes, hora, minuto, ano=2025):
    primeiro_dia = datetime.date(ano, 1, 1)
    dia_do_ano = (datetime.date(ano, mes, dia) - primeiro_dia).days
    
    escala = gerar_escala()
    
    # Ajustar transição às 9h da manhã
    if hora < 9 and dia_do_ano > 0:
        dia_do_ano -= 1
    
    return escala.get(dia_do_ano, "Desconhecido")

# Dicionário com as informações de cada farmácia
info_farmacias = {
    "Chaves": {
        "telefone": "276 321 200",
        "endereco": "Av. Dom Afonso I Duque de Bragança, n.º 11, 5400-025"
    },
    "Costa Gomes": {
        "telefone": "Desconhecido",
        "endereco": "Rua Direita 172, 5400-220 Chaves"
    },
    "Martins": {
        "telefone": "276 321 535",
        "endereco": "Rua Portas do Anjo, 5400-458"
    },
    "Barroso": {
        "telefone": "276 324 223",
        "endereco": "Ed. América Loja 3 Cinochaves, 5400-032 Chaves"
    },
    "Pereira da Silva": {
        "telefone": "276 324 690",
        "endereco": "Urbanização Raposeira - Loja 1, Lote 3, 5400-279 Chaves"
    },
    "Maldonado": {
        "telefone": "276 324 952",
        "endereco": "Avenida da Trindade, 27, Santa Cruz/Trindade"
    },
    "Barreiros": {
        "telefone": "276 916 219",
        "endereco": "Av. António Granjo, nº 7, Largo da Estação, 5400-080 Chaves"
    },
    "Nova Farmácia da Madalena": {
        "telefone": "276 322 670",
        "endereco": "Rua Cândido Sotto Mayor, 26/32, 5400-000 Chaves"
    },
    "Paula Files": {
        "telefone": "276 318 816",
        "endereco": "Avenida Santo Amaro, 26, 5400-055 Chaves"
    },
    "Farmácia da Nova Ponte": {
        "telefone": "276 348 185",
        "endereco": "Avenida 5 de Outubro, 24, Santa Maria Maior"
    },
    "Mariz": {
        "telefone": "276 322 270",
        "endereco": "Rua de Santo António, 4, Santa Maria Maior"
    }
}

def atualizar_informacoes():
    agora = datetime.datetime.now()
    hora_str = agora.strftime("%H:%M:%S")
    time_label.config(text=hora_str)
    
    # Farmácia atual
    farmacia = obter_farmacia(agora.day, agora.month, agora.hour, agora.minute)
    pharmacy_label.config(text=farmacia)
    
    # Atualizar até às 9h do dia seguinte ou do próprio dia
    if agora.hour >= 9:
        dia_seguinte = agora.day + 1
    else:
        dia_seguinte = agora.day
    
    ate_label.config(text=f"Até às 9h do dia {dia_seguinte}")
    
    # Obter dados (telefone, endereço) do dicionário
    info = info_farmacias.get(farmacia, {})
    telefone = info.get("telefone", "Desconhecido")
    endereco = info.get("endereco", "Desconhecido")
    
    # Atualizar labels de morada e contacto
    morada_label.config(text=f"Morada: {endereco}", wraplength=1300, anchor="center", justify="center")
    contacto_label.config(text=f"Contacto: {telefone}")
    
    # Atualiza a cada 1 segundo
    root.after(1000, atualizar_informacoes)

def sair_fullscreen(event=None):
    root.attributes("-fullscreen", False)
    root.geometry("800x600")

# --- Criação da janela ---
root = tk.Tk()
root.title("Farmácia de Serviço")
root.attributes("-fullscreen", True)
root.configure(bg="white")

# --- Definição de estilos ---
style = ttk.Style()
style.theme_use("clam")

style.configure("TFrame", background="white")

style.configure("Title.TLabel",    background="white", foreground="gray",
                font=("Lusitana", 48, "bold"))
style.configure("Pharmacy.TLabel", background="white", foreground="black",
                font=("Lusitana", 64, "bold"))
style.configure("Subtitle.TLabel", background="white", foreground="black",
                font=("Lusitana", 44))
style.configure("Time.TLabel",     background="white", foreground="black",
                font=("Lusitana", 38))

# --- Frame principal (centralizado) ---
frame = ttk.Frame(root, style="TFrame")
frame.pack(expand=True)

# --- Labels centrais ---
title_label = ttk.Label(frame, text="Farmácia de Serviço", style="Title.TLabel")
title_label.pack(pady=(0, 100))

pharmacy_label = ttk.Label(frame, text="Carregando...", style="Pharmacy.TLabel")
pharmacy_label.pack(pady=(0, 10))

ate_label = ttk.Label(frame, text="Até às 9h do dia ...", style="Subtitle.TLabel")
ate_label.pack(pady=(0, 90))

morada_label = ttk.Label(frame, text="Morada:", style="Subtitle.TLabel")
morada_label.pack(pady=(0, 40), fill="x")

contacto_label = ttk.Label(frame, text="Contacto:", style="Subtitle.TLabel")
contacto_label.pack(pady=(0, 20))

# --- Hora no canto superior direito ---
time_label = ttk.Label(root, text="", style="Time.TLabel")
time_label.place(relx=0.98, rely=0.05, anchor="ne")  # top-right corner

# --- Tecla ESC para sair do fullscreen ---
root.bind("<Escape>", sair_fullscreen)

# --- Iniciar ciclo de atualização ---
atualizar_informacoes()

root.mainloop()










#                                                       PARA TESTES DE DATAS
'''
import tkinter as tk
from tkinter import ttk
import datetime

def gerar_escala():
    escala_farmacias = [
        "Morais", "Costa Gomes", "Martins", "Barroso", "Pereira da Silva", "Maldonado", 
        "Barreiros", "Farmácia da Nova da Madalena", "Paula Files", "Nova Ponte", "Mariz"
    ]
    total_farmacias = len(escala_farmacias)
    
    escala_dias = {}
    
    # Gerar escala para o ano inteiro
    for dia_ano in range(365):
        indice_farmacia = dia_ano % total_farmacias
        escala_dias[dia_ano] = escala_farmacias[indice_farmacia]
    
    return escala_dias

def obter_farmacia(dia, mes, hora, ano=2025):
    primeiro_dia = datetime.date(ano, 1, 1)
    dia_do_ano = (datetime.date(ano, mes, dia) - primeiro_dia).days
    
    escala = gerar_escala()
    
    # Ajustar transição às 9h da manhã
    if hora < 9 and dia_do_ano > 0:
        dia_do_ano -= 1  # Mantém a farmácia do dia anterior
    
    return escala.get(dia_do_ano, "Desconhecido")

def mostrar_farmacia():
    agora = datetime.datetime.now()
    dia, mes, hora = agora.day, agora.month, agora.hour
    farmacia = obter_farmacia(dia, mes, hora)
    resultado_label.config(text=f"Farmácia de serviço: {farmacia}")
    ttLabel.config(text=f"Farmácia de serviço dia {dia}/{mes}")

def atualizar_farmacia():
    agora = datetime.datetime.now()
    dia, mes, hora = agora.day, agora.month, agora.hour
    
    # Se passou das 9h, atualizar farmácia
    if hora >= 9:
        mostrar_farmacia()
    
    # Atualiza automaticamente a cada minuto
    root.after(60000, atualizar_farmacia)

def testar_farmacia():
    try:
        dia = int(entry_dia.get())
        mes = int(entry_mes.get())
        hora = int(entry_hora.get())
        farmacia = obter_farmacia(dia, mes, hora)
        resultado_label.config(text=f"Farmácia de serviço: {farmacia}")
        ttLabel.config(text=f"Farmácia de serviço dia {dia}/{mes} às {hora}:00")
    except ValueError:
        resultado_label.config(text="Erro: Insira valores válidos!")

# Criando interface gráfica
root = tk.Tk()
root.title("Farmácia de Serviço")
root.geometry("350x200")

frame = ttk.Frame(root, padding=10)
frame.grid()

agora = datetime.datetime.now()
dia, mes = agora.day, agora.month

ttLabel = ttk.Label(frame, text=f"Farmácia de serviço dia {dia}/{mes}")
ttLabel.grid(column=0, row=0, columnspan=2)

resultado_label = ttk.Label(frame, text="Carregando...")
resultado_label.grid(column=0, row=1, columnspan=2)

# Entrada para testar datas manualmente
ttk.Label(frame, text="Dia:").grid(column=0, row=2)
entry_dia = ttk.Entry(frame, width=5)
entry_dia.grid(column=1, row=2)

ttk.Label(frame, text="Mês:").grid(column=0, row=3)
entry_mes = ttk.Entry(frame, width=5)
entry_mes.grid(column=1, row=3)

ttk.Label(frame, text="Hora:").grid(column=0, row=4)
entry_hora = ttk.Entry(frame, width=5)
entry_hora.grid(column=1, row=4)

btn_testar = ttk.Button(frame, text="Testar Data", command=testar_farmacia)
btn_testar.grid(column=0, row=5, columnspan=2)

mostrar_farmacia()
atualizar_farmacia()  # Atualiza automaticamente

root.mainloop()


'''



