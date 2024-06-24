
import netpack as npk
import time
PORT=9999
client_ip="172.0.0.1"
server_ip=client_ip
ADDR=(server_ip, PORT)
client_socket=npk.create_tcp_timeoutsocket()
npk.connect_to_tcp_server(client_socket, ADDR)
print('[CONNECTING] Server with IP : {} & PORT : {}'.format(ADDR[0], ADDR[1]))
T1=time.time()
data=None
while True:
    try:
        data=npk.read_data_from_tcp_server(client_socket)        
        if data=='close':
            break
        print('[=] Message from server : {}'.format(data))
    except:
        if (time.time()-T1 > 5) and (data==None): # wait 5 sec for server to connect & data is none
            print("[=] Server is not accepting connection")
            break
npk.close_socket_connection(client_socket)
