#!/usr/bin/env python3
import asyncio
import websockets

async def test():
    async with websockets.connect("ws://localhost:8080/") as websocket:
        await websocket.send("Hello!")
        response = await websocket.recv()
        print(response)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(test())
