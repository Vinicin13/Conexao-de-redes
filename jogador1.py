import socket
host = "127.0.0.1"
port = 2002
def main():


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    mensagem = client_socket.recv(1024).decode()
    print(mensagem)

    nickname = input("Digite seu apelido: ")
    client_socket.send(nickname.encode())

    response = client_socket.recv(1024).decode()
    print(response)

    player_choice = input("Escolha pedra, papel ou tesoura: ")
    client_socket.send(player_choice.encode())

    result = client_socket.recv(1024).decode()
    print(result)

    client_socket.close()

if __name__ == "__main__":
    main()