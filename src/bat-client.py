import socket

# 1. Escolha do host
print("Selecione seu host:")
print("1 - Local Host")
print("2 - Remote Host")
opcaoHost = input("Opção: ")

if opcaoHost == '1':
    host = "localhost" # 127.0.0.1
elif opcaoHost == '2':
    host = input("Insira o endereço IP do host: ")
else:
    print("Comando Inválido")
    exit()
    
print("1 - Porta Padrão (49152)")
print("2 - Porta Específica")
opcaoPorta = input("Opção: ")

if opcaoPorta == '1':
    port = 49152 # Porta dinamica
elif opcaoPorta == '2':
    port = input("Insira o endereço da porta: ")
else:
    print("Comando Inválido")
    exit()

# Verificar se a porta está em uso
    # IMPLEMENTAR
    
# Interface TK
    # Implementar

# Cria o socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Usa tcp-ip para garantir que msg chegue

# Conecta-se ao servidor
client_socket.connect((host, port))

# Comunicação
while True:
    # Envia uma mensagem ao servidor
    message = input("<>>: ")
    client_socket.sendall(message.encode())
    
    # Recebe a resposta do servidor
    data = client_socket.recv(1024)
    print(f"<?>: {data.decode()}")
    
    if message.lower() == 'sair':
        break  # Encerra a comunicação se o usuário digitar "sair"

# Fecha a conexão
client_socket.close()
