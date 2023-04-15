from framework.plugins import AsyncPlugin

class MyAsyncPlugin(AsyncPlugin):
    async def run(self, app):
        print("Running async plugin aio_plugin.MyAsyncPlugin...")