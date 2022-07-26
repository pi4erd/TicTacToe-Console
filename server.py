#!/usr/bin/env python3
import asyncio
from _thread import *
import sys
import socket

def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""

    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received:", reply)
                print("Sendind:", reply)
            
            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost connection")
    conn.close()

if __name__ == "__main__":
    host = "localhost"
    port = 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((host, port))
    except socket.error as e:
        print(repr(e))


    server.listen(2)
    print(f"Waiting for a connection, listening at {host}:{port}")

    while True:
        conn, addr = server.accept()
        print("Connected to:", addr)

        start_new_thread(threaded_client, (conn,))
