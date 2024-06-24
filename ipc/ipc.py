import netpack as npk 


import IPC_methods as ipc  

Q=npk.create_queue() 

val_list=list(range(10)) 

flag=1 

if flag==1: 

    P1=npk.create_process(ipc.write_to,[Q,val_list]) 

    P2=npk.create_process(ipc.read_from,[Q]) 

    npk.start_process(P1) 

    npk.start_process(P2) 

    npk.join_process(P1) 

    npk.join_process(P2) 

    print ("Main ends") 

elif flag==2: 

      P3=npk.create_process(ipc,write_read,[Q,val_list]) 

      P4=npk.create_process(ipc,read_write,[Q]) 

      npk.start_process(P3) 

      npk.start_process(P4) 

      npk.join_process(P3) 

      npk.join_process(P4) 

      print ("Main ends")