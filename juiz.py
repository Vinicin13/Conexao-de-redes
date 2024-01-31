import socket
import threading

players = {}

def determine_winner(player_choice, opponent_choice):
    if player_choice == opponent_choice:
        return "Empate"
    elif (player_choice == "pedra" and opponent_choice == "tesoura") or \
         (player_choice == "tesoura" and opponent_choice == "papel") or \
         (player_choice == "papel" and opponent_choice == "pedra"):
        return "Você venceu!"
    else:
        return "Você perdeu!"


def main():
    host = "127.0.0.1"
    port = 2002

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)  # Aumentado o número de conexões na fila

    print("Servidor em execução, aguardando jogadores...")


    #while True:
    player_conn, player_addr = server_socket.accept()
    print("Novo jogador conectado:", player_addr)

    player_conn.send("Bem-vindo! Insira seu apelido:".encode())
    nickname = player_conn.recv(1024).decode()

    players[nickname] = player_conn
    print("Jogador", nickname, "inscrito.")
    player_conn.send("Inscrição bem-sucedida.".encode())

    



    player2_conn, player_addr2 = server_socket.accept()
    print("Novo jogador conectado:", player_addr2)

    player2_conn.send("Bem-vindo! Insira seu apelido:".encode())
    nickname = player2_conn.recv(1024).decode()
    players[nickname] = player2_conn

    print("Jogador", nickname, "inscrito.")
    player2_conn.send("Inscrição bem-sucedida.".encode())

    



    player_choice = player_conn.recv(1024).decode().lower()
    player2_choice = player2_conn.recv(1024).decode().lower()

    result1 = determine_winner(player_choice, player2_choice)
    result2 = determine_winner(player2_choice, player_choice)

    player_conn.send(result1.encode())
    player2_conn.send(result2.encode())

    player_conn.close()
    player2_conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()



"""
tentativa do chat
import socket

def determine_winner(player_choice, opponent_choice):
    if player_choice == opponent_choice:
        return "Empate"
    elif (player_choice == "pedra" and opponent_choice == "tesoura") or \
         (player_choice == "tesoura" and opponent_choice == "papel") or \
         (player_choice == "papel" and opponent_choice == "pedra"):
        return "Você venceu!"
    else:
        return "Você perdeu!"

def main():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)

    print("Aguardando jogadores...")
    player1_conn, player1_addr = server_socket.accept()
    print("Jogador 1 conectado:", player1_addr)
    player1_conn.send("Você é o jogador 1. Aguarde o jogador 2.".encode())

    player2_conn, player2_addr = server_socket.accept()
    print("Jogador 2 conectado:", player2_addr)
    player2_conn.send("Você é o jogador 2. Agora você pode jogar.".encode())
    
    player1_choice = player1_conn.recv(1024).decode().lower()
    player2_choice = player2_conn.recv(1024).decode().lower()

    result1 = determine_winner(player1_choice, player2_choice)
    result2 = determine_winner(player2_choice, player1_choice)

    player1_conn.send(result1.encode())
    player2_conn.send(result2.encode())

    player1_conn.close()
    player2_conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()"""