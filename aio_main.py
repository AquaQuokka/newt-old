import asyncio
import importlib
from framework import newt as fw
from framework import plugins

async def main():
    app = fw.Newt()
    plugin = importlib.import_module("aio_plugin")
    await plugins.AsyncPlugin.run_all(app)
    await app.run_coroutine()

asyncio.run(main())