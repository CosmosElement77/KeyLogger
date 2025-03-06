import socket

# Define host and port
host = socket.gethostname()
port = 10000

# Create Socket object and bind to hostname
sock = socket.socket() 
sock.bind((host, port))

# Establishing Connection
sock.listen(5)
print(f'Server listening on {host}:{port}')

# Wait for a connection
print("Waiting for a connection...")
conn, addr = sock.accept()  # Accept connection when client connects
print(f"Connected by {addr[0]}:{addr[1]}")

# Print Client Data
# try:
while True:
    data = conn.recv(1024)  # Receive client data
    if data:
        print(data.decode('utf-8'))
#         else:
#             print("No data received. Closing connection.")
#             break
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     conn.close()
#     sock.close()
#     print("Connection closed.")
