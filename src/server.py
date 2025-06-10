import socket

# Menu host
print('\033[1;32;40mServidor em execução...\033[m')
print('\033[1;32;40m1 - Local Host\033[m')
print('\033[1;32;40m2 - Remote Host\033[m')
opcaoHost = input('\033[1;32;40mOpção: \033[m')

if opcaoHost == '1':
    host = "localhost"  # 127.0.0.1
elif opcaoHost == '2':
    host = input('\033[1;32;40mInsira o endereço IP para o servidor escutar: \033[m')
else:
    print('\033[1;32;40m"Comando Inválido\033[m')
    exit()

# Configuração da porta
print('\033[1;32;40m1 - Porta Padrão (49152)\033[m')
print('\033[1;32;40m2 - Porta Específica\033[m')
opcaoPorta = input('\033[1;32;40mOpção: \033[m')

if opcaoPorta == '1':
    port = 49152 
elif opcaoPorta == '2':
    try:
        port = int(input('\033[1;32;40mInsira a porta: \033[m'))
    except ValueError:
        print('\033[1;32;40mPorta inválida.\033[m')
        exit()
else:
    print('\033[1;32;40mComando Inválido\033[m')
    exit()

# Criação do socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz o bind do servidor ao host e porta
try:
    server_socket.bind((host, port))
except socket.error as e:
    print(f'\033[1;32;40mErro ao vincular o socket: {e}\033[m')
    exit()

# Escutando por conexões
server_socket.listen(1)
print(f'\033[1;32;40mServidor escutando em {host}:{port}...\033[m')

# Aceita a conexão do cliente
conn, addr = server_socket.accept()
print(f'\033[1;32;40mConexão estabelecida com {addr}\033[m')

# Comunicação
while True:
    data = conn.recv(1024)
    if not data:
        break

    mensagem = data.decode()
    print(f'\033[1;32;40m<>>: {mensagem}\033[m')

    if mensagem.lower() == 'sair':
        conn.sendall("Conexão encerrada.".encode())
        break

    resposta = input("<?>: ")
    conn.sendall(resposta.encode())

# Fecha a conexão
conn.close()
server_socket.close()
print('\033[1;32;40mServidor finalizado\033[m')
