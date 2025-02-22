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
    global ultimo_dia, ultima_hora
    agora = datetime.datetime.now()
    dia, mes, hora = agora.day, agora.month, agora.hour
    farmacia = obter_farmacia(dia, mes, hora)
    
    resultado_label.config(text=f"Farmácia de serviço: {farmacia}")
    ttLabel.config(text=f"Farmácia de serviço dia {dia}/{mes}")
    
    # Atualiza os últimos valores
    ultimo_dia, ultima_hora = dia, hora
    
def atualizar_farmacia():
    agora = datetime.datetime.now()
    dia, mes, hora = agora.day, agora.month, agora.hour
    
    # Se o dia mudou ou passou das 9h, atualiza a farmácia
    if hora >= 9 and (dia != ultimo_dia or hora != ultima_hora):
        mostrar_farmacia()
    
    # Verifica novamente a cada minuto
    root.after(60000, atualizar_farmacia)

# Criando interface gráfica
root = tk.Tk()
root.title("Farmácia de Serviço")
root.geometry("300x150")

frame = ttk.Frame(root, padding=10)
frame.grid()

agora = datetime.datetime.now()
dia, mes = agora.day, agora.month

# Variáveis para controle da atualização
ultimo_dia = dia
ultima_hora = agora.hour

ttLabel = ttk.Label(frame, text=f"Farmácia de serviço dia {dia}/{mes}")
ttLabel.grid(column=0, row=0, columnspan=2)

resultado_label = ttk.Label(frame, text="Carregando...")
resultado_label.grid(column=0, row=1, columnspan=2)

mostrar_farmacia()
atualizar_farmacia()  # Inicia a atualização automática

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