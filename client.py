#!/usr/bin/env python3
import socket

class Network:
    def __init__(self, host: str, port: int):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.addr = (self.host, self.port)
        self.id = self.connect()
        print(self.id)
    
    def connect(self):
        try:
            self.client_connected(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
    
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

class Player:
    def __init__(self, player: int):
        self.player = player
