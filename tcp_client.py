import socket
import sys

HOST = ''

if len(sys.argv) != 2:
    raise SystemExit('Error: missing args\nUsage: python3 tcp_server.py <PORT>')
    exit()

PORT = int(sys.argv[1])


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))


    msg_to_send = input(">>Type a msg\n")
    while msg_to_send != 'disconnect':
        s.sendall(bytes(msg_to_send, 'utf-8'))
        #print('I sent my msg~!')
        #msg = s.recv(1024)


        if msg_to_send == 'close server':
            print("server disconnected.")
            exit(1)

        #print(f"I echoed: {msg}")

        text = s.recv(1024)
        print(f"Response: {''.join(text.decode('utf-8'))}")

        msg_to_send = input(">>Type a msg\n")



    s.sendall(b'disconnect')