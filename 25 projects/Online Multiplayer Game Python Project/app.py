import streamlit as st
import pygame
import socket
import threading
import ast
import time

# Setup Server
HOST = '0.0.0.0'
PORT = 5555
players = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)
st.write(f"Server started on {HOST}:{PORT}")

def handle_client(conn, addr, player_id):
    players[player_id] = [50, 50]
    conn.send(f"{player_id}".encode())
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            players[player_id] = ast.literal_eval(data)
            conn.send(str(players).encode())
        except:
            break
    del players[player_id]
    conn.close()

def start_server():
    player_id = 0
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr, player_id)).start()
        player_id += 1

threading.Thread(target=start_server, daemon=True).start()

# Pygame Setup
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

SERVER_IP = "127.0.0.1"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))
player_id = int(client.recv(1024).decode())
positions = {player_id: [50, 50]}

running = True
while running:
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        positions[player_id][0] -= 5
    if keys[pygame.K_RIGHT]:
        positions[player_id][0] += 5
    if keys[pygame.K_UP]:
        positions[player_id][1] -= 5
    if keys[pygame.K_DOWN]:
        positions[player_id][1] += 5

    client.send(str(positions[player_id]).encode())
    data = client.recv(1024).decode()
    positions = ast.literal_eval(data)
    
    for p_id, pos in positions.items():
        color = (255, 0, 0) if p_id == player_id else (0, 255, 0)
        pygame.draw.rect(screen, color, (*pos, 20, 20))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
client.close()
