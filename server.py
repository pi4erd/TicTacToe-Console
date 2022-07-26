#!/usr/bin/env python3
import asyncio
from _thread import *
import sys
import socket
import json
import tictactoe
from game import *
import pickle

if __name__ == "__main__":
    host = "localhost"
    port = 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((host, port))
    except socket.error as e:
        print(e)

    server.listen(2)
    print("Waiting for connection, {}:{}".format(host, port))    

    board = [[0]*3 for _ in range(3)]
    connected = set()
    games: dict[int, Game] = {}
    idCount = 0

    def threaded_client(conn: socket.socket, p, gameId):
        conn.send(str.encode(str(p)))

        reply = ""
        while True:
            try:
                data = conn.recv(4096).decode()
                if gameId in games:
                    game = games[gameId]

                    if not data:
                        break
                    else:
                        if data == "reset":
                            game.reset()
                        elif data != "get":
                            game.play(p, data)
                                
                    conn.sendall(pickle.dumps(game))
                else:
                    break
            except:
                break
    try:
        while True:
            conn, addr = server.accept()
            print("Connected to:", addr)

            idCount += 1
            p = 0
            gameId = (idCount - 1) // 2
            if idCount % 2 == 1:
                games[gameId] = Game(gameId)
                print("Creating new game")
            else:
                games[gameId].ready = True
                p = 1
            
            start_new_thread(threaded_client, (conn, p, gameId))
    except KeyboardInterrupt:
        server.close()
