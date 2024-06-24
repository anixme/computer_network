
#Tcp_server
import netpack as npk
import random
PORT = 9999
server_ip = "172.20.55.31"
ADDR = (server_ip, PORT)
server_socket = npk.create_tcp_socket()
npk.start_tcp_server(server_socket, ADDR)
print("[WAIT] Server waits for client")
(client_socket, addr) = npk.accept_tcp_client(server_socket)
print('[CONNECTED] Client with IP : {} & PORT : {}'.format(addr[0], addr[1]))
while True:
    val = random.randint(0,100)
    npk.send_data_to_tcp_client(client_socket, val)
    print("[SEND] Data {}".format(val))
    data = npk.read_data_from_tcp_client(client_socket)
    if data == "close":
        npk.close_socket_connection(client_socket)
        print("[=] TCP Client requesting to close connection")
        break
    else:
        print("[RECEV] {}".format(data))
npk.close_socket_connection(server_socket)
