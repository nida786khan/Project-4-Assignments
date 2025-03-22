# server.py
import socket
import threading

def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"[{addr}] {message}")
            client_socket.send("Message received!".encode())
        except:
            break
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen()
    print("[SERVER] Waiting for connections...")
    while True:
        client_socket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()

# client.py
import socket
import streamlit as st

def client_app():
    st.title("Multiplayer Game Client")
    host = st.text_input("Enter Server IP", "127.0.0.1")
    port = 5555
    message = st.text_input("Enter Message")
    if st.button("Send Message"):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))
            client.send(message.encode())
            response = client.recv(1024).decode()
            st.write("Server Response: ", response)
        except Exception as e:
            st.write("Error: ", e)
        finally:
            client.close()

if __name__ == "__main__":
    client_app()
