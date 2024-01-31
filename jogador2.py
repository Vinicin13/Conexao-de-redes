import socket
host = "127.0.0.1"
port = 2002
def main():


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = client_socket.recv(1024).decode()
    print(message)

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

"""
#tentativa do chat
import socket, sys
from threading import Thread

HOST = '127.0.0.2'  # endereço IP
PORT = 2000       # Porta utilizada pelo servidor
BUFFER_SIZE = 1024  # tamanho do buffer para recepção dos dados

def conexao():
    valor = input("Digite o IP para se conectar: ")
    confirmacao = input(f"O destino é {valor}. Digite 1 para sim e 0 para nao: ")

    confirmacao = (False if int(confirmacao) == 0 else True)
    if confirmacao is False:
        print("Fechando programa")
        sys.exit()
    return iniciar_conexao(valor)
 
def verifica_ip(ip_address):
    
    if len(ip_address) == 9 and ip_address is not None:
        return True
    print("Ip errado")
    sys.exit()

def iniciar_conexao(ip_address):

    print("Tentando conexao com o servidor")
    verifica_ip(ip_address)
    tcp_conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        destino = (ip_address,PORT)
        tcp_conexao.connect(destino) 

    except ConnectionError as error:
        print("Nao aconteceu a conexao.tente novamente")

    return tcp_conexao


def fechar_conexao(tcp_conexao):
    print ("Fim da conexao")
    tcp_conexao.close()

def chat(tcp_conexao):
    print ("Bem vindo ao chat")

    while True:
        mensagem = input ("Voce: ")

        if mensagem != '':
            tcp_conexao.send(bytes(mensagem,"utf8"))
            if mensagem == 'exit':
                break
        recv_mensagem = tcp_conexao.recv(BUFFER_SIZE).decode("ascii")


        if recv_mensagem != '':
            print(f"Mensagem do servidor: {recv_mensagem}")

            if recv_mensagem =='exit':
                print("Cliente desconectou")
    
    print("Saindo")
    fechar_conexao(tcp_conexao)


if __name__ == '__main__':   
    
    print("Chat")
    conexao = conexao()
    chat(conexao)

    try: 
        conexao.close()
    except ConnectionError as err:
        print("Conexao TCP terminou") """