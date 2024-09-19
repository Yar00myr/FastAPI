import asyncio
from fastapi import FastAPI
from uvicorn import Server, Config


app = FastAPI()

config = Config(app=app, host="localhost", port=8080)

from . import routes


def main() -> None:
    server = Server(config)
    asyncio.run(server.serve())

if __name__ == "__main__":
    main()
    