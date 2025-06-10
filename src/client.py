import socket

# Menu host
print('\033[1;32;40mSelecione seu host:\033[m')
print('\033[1;32;40m1 - Local Host\033[m')
print('\033[1;32;40m2 - Remote Host\033[m')
opcaoHost = input('\033[1;32;40mOpção: \033[m')

if opcaoHost == '1':
    host = "localhost" # 127.0.0.1
elif opcaoHost == '2':
    host = input('\033[1;32;40mInsira o endereço IP do host: \033[m')
else:
    print('\033[1;32;40mComando Inválido\033[m')
    exit()
    
print('\033[1;32;40m1 - Porta Padrão (49152)\033[m')
print('\033[1;32;40m2 - Porta Específica\033[m')
opcaoPorta = input('\033[1;32;40mOpção: \033[m')

if opcaoPorta == '1':
    port = 49152 # Porta dinamica
elif opcaoPorta == '2':
    try:
        port = int(input('\033[1;32;40mInsira a porta: \033[m')) # Verifica se porta já está em uso
    except ValueError:
        print('\033[1;32;40mPorta inválida.\033[m')
        exit()
else:
    print('\033[1;32;40mComando Inválido\033[m')
    exit()

# Cria o socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Usa tcp-ip para garantir que msg chegue

# Conecta-se ao servidor
client_socket.connect((host, port))

# Comunicação
while True:
    # Envia uma mensagem ao servidor
    message = input(('\033[1;32;40m<>>: \033[m'))
    client_socket.sendall(message.encode())
    
    # Recebe a resposta do servidor
    data = client_socket.recv(1024)
    print(f'\033[1;30;42m<?>: {data.decode()}\033[m')
    
    if message.lower() == 'sair' or message.lower() == 'exit':
        break

# Fecha a conexão
client_socket.close()
