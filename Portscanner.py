import socket

target_ip = input("Enter target")

for port in range (1,1024) :
     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     s.settimeout(5)
     
     result = s.connect_ex((target_ip,port))
     
     if result == 0 :
         print("Port {port}: Got connected !")
     
     s.close()
