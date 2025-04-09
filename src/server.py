import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox

# Criação da janela principal
app = tk.Tk()
app.title("Servidor TCP com Tkinter")
app.geometry("400x300")

# Variáveis globais
server_socket = None
client_socket = None

def iniciar_servidor():
    global server_socket, client_socket

    host = host_var.get()
    if host == "localhost":
        host = "127.0.0.1"
    else:
        host = simpledialog.askstring("Host Remoto", "Insira o IP do host:")

    if porta_var.get() == "padrão":
        port = 49152
    else:
        port = simpledialog.askinteger("Porta", "Insira o número da porta:")

    # Verifica se porta está em uso
    try:
        # Criar socket TCP/IP
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        log(f"Servidor ouvindo em {host}:{port}...")
    except OSError:
        messagebox.showerror("Erro", "Porta já está em uso.")
        return

    def aceitar_conexao():
        global client_socket
        client_socket, client_address = server_socket.accept()
        log(f"Conexão com {client_address}")
        receber_mensagens()

    threading.Thread(target=aceitar_conexao, daemon=True).start()

def receber_mensagens():
    def thread_receber():
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                log(f"Cliente: {data.decode()}")
            except:
                break
    threading.Thread(target=thread_receber, daemon=True).start()

def enviar_mensagem():
    msg = msg_entry.get()
    if client_socket and msg:
        client_socket.sendall(msg.encode())
        log(f"Você: {msg}")
        msg_entry.delete(0, tk.END)

def log(msg):
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, msg + "\n")
    log_text.config(state=tk.DISABLED)
    log_text.see(tk.END)

# Interface gráfica
tk.Label(app, text="Escolha o host:").pack()

host_var = tk.StringVar(value="localhost")
tk.Radiobutton(app, text="Localhost", variable=host_var, value="localhost").pack()
tk.Radiobutton(app, text="Host Remoto", variable=host_var, value="remoto").pack()

tk.Label(app, text="Escolha a porta:").pack()

porta_var = tk.StringVar(value="padrão")
tk.Radiobutton(app, text="Padrão (49152)", variable=porta_var, value="padrão").pack()
tk.Radiobutton(app, text="Personalizada", variable=porta_var, value="personalizada").pack()

tk.Button(app, text="Iniciar Servidor", command=iniciar_servidor).pack(pady=10)

log_text = tk.Text(app, height=10, state=tk.DISABLED)
log_text.pack()

msg_entry = tk.Entry(app)
msg_entry.pack(fill=tk.X, padx=10)

tk.Button(app, text="Enviar", command=enviar_mensagem).pack(pady=5)

# Rodar a interface
app.mainloop()
