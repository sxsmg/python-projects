import socket

target_host = 'google.com'
target_port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b'GET / HTTP/1.1\r\nHOST:google.com\r\n\r\n')

response = client.recv(4096)

print(response)