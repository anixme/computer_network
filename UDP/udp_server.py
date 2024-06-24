
import netpack as npk
import time
PORT=9999
server_ip="172.0.0.1"
ADDR=(server_ip, PORT)
max_client_connection = 2
server_socket=npk.create_tcp_timeoutsocket()
npk.start_tcp_server(server_socket, ADDR)
print("[WAIT] Multithreaded Server waits for maximum {} clients".format(max_client_connection))
client_list = []
while True:
    try:
        if len(client_list) < max_client_connection:
            (client_socket, addr)=npk.accept_tcp_client(server_socket)
            print('[CONNECTED] Client with IP : {} & PORT : {}'.format(addr[0], addr[1]))
            C=npk.ConnectClient_thread(client_socket, addr,20)
            C.start()
            client_list.append(C)
            if len(client_list)== max_client_connection:
                print('[=] Server has reached to maximum connections {}'.format(max_client_connection))
    except KeyboardInterrupt:
        break
    except:
        pass    
for i in range(len(client_list)):
    if client_list[i].check_thread_status():
        client_list[i].close_connection()
npk.close_socket_connection(server_socket)
