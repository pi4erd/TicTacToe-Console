#!/usr/bin/env python3
import asyncio
import websockets

async def handler(websocket, path):
    data = await websocket.recv()
    reply = f"Data recieved as: {data}"
    await websocket.send(reply)

if __name__ == "__main__":
    start_server = websockets.serve(handler, "localhost", 8080)
    try:
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        exit(0)
