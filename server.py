import socket
import sys


def send_commands(conn):
    while True:
        print("enter the commands below\n")
        cmd = input()
        if cmd == 'quit':
            conn.close()
            server.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(4096), "utf-8")  # Size of data-in buffer
            print(client_response, end="\n")


bind_ip = ''
bind_port = 555
serv_add = (bind_ip, bind_port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(serv_add)
server.listen(5)
print("Listening on {}:{}".format(bind_ip, bind_port))
conn, addr = server.accept()  # server.accept returns pair, conn and address.
print('Accepted connection from {} and port {}'.format(addr[0], addr[1]))
send_commands(conn)
conn.close()
