import asyncio
from framework import newt as fw

async def main():
    app = fw.Newt()
    await app.start()

asyncio.run(main())