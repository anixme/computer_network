
#Tcp_client
import netpack as npk
PORT = 9999
client_ip = "172.20.55.31"
server_ip = client_ip
ADDR = (server_ip, PORT)
client_socket = npk.create_tcp_socket()
npk.connect_to_tcp_server(client_socket, ADDR)
print('[CONNECTED] Server with IP : {} & PORT : {}'.format(ADDR[0], ADDR[1]))
while True:
    data = npk.read_data_from_tcp_server(client_socket)
    print('[=] Message from server : {}'.format(data))
    flag = input('Close connection y/n : ')
    if flag == 'y' or flag == 'Y':
        npk.send_data_to_tcp_server(client_socket, "close")
        npk.close_socket_connection(client_socket)
        print("[=] Requested for closing connection")
        break
    else:
        npk.send_data_to_tcp_server(client_socket, "+ACK")
