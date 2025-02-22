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
    
    # Ajustar transição às 9h
    if hora < 9 and dia_do_ano > 0:
        dia_do_ano -= 1  # Mantém a farmácia do dia anterior
    
    return escala.get(dia_do_ano, "Desconhecido")

def mostrar_farmacia():
    agora = datetime.datetime.now()
    dia, mes, hora = agora.day, agora.month, agora.hour
    farmacia = obter_farmacia(dia, mes, hora)
    ttLabel.config(text=f"Farmácia de serviço dia {dia}/{mes}")
    resultado_label.config(text=f"{farmacia}")

# Criando interface gráfica
root = tk.Tk()
root.title("Farmácia de Serviço")
root.attributes("-fullscreen", True)  # Define a janela para ocupar toda a tela
root.configure(bg="white")

def sair_fullscreen(event=None):
    root.attributes("-fullscreen", False)  # Sai do modo fullscreen
    root.geometry("800x600")  # Define um tamanho padrão para a janela

# Vincular a tecla "Esc" para sair do fullscreen
root.bind("<Escape>", sair_fullscreen)


frame = ttk.Frame(root, padding=20, style="TFrame")
frame.place(relx=0.5, rely=0.5, anchor="center")

style = ttk.Style()
style.configure("TFrame", background="white")
style.configure("TLabel", background="white", foreground="black", font=("Arial", 14))
style.configure("Farmacia.TLabel", font=("Arial", 28, "bold"), foreground="blue")  # Define estilo da farmácia

agora = datetime.datetime.now()
dia, mes = agora.day, agora.month

# Exibir data
ttLabel = ttk.Label(frame, text=f"Farmácia de serviço dia {dia}/{mes}", font=("Arial", 16, "bold"), anchor="center")
ttLabel.pack(pady=10)

# Exibir farmácia com nome grande e centralizado (corrigido para usar estilo correto)
resultado_label = ttk.Label(frame, text="Carregando...", style="Farmacia.TLabel", anchor="center")
resultado_label.pack(pady=20)

mostrar_farmacia()

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