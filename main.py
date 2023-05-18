import socket
from loguru import logger

logger.debug("Python Simple Server Application starting...")

# Create a socket and bind it to a specific address and port
HOST = '10.0.8.138'  # <-- Change to IP of the system this script is running on.
PORT = 8080
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(1)
    logger.debug(f"Server listening on {HOST}:{PORT}")

    while True:
        # Accept a client connection
        conn, addr = sock.accept()
        logger.debug(f"Accepting client connection from: {addr}")

        # Handle client requests
        while True:
            # Receive data from the client
            data = conn.recv(1024)
            if not data:
                break

            logger.debug(f"Received data: {data.decode()}")

            # Send a response back to the client
            response = b"Message Received"
            conn.sendall(response)

        # Close the connection
        conn.close()
