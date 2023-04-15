import asyncio

class Plugin:
    _registry = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.register()

    def __init__(self):
        pass

    def run(self, app):
        raise NotImplementedError

    @classmethod
    def register(cls):
        cls._registry.append(cls)

    @classmethod
    def run_all(cls, app):
        for plugin_cls in cls._registry:
            plugin = plugin_cls()
            plugin.run(app)


class AsyncPlugin:
    _registry = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.register()

    def __init__(self):
        pass

    async def run(self, app):
        raise NotImplementedError

    @classmethod
    def register(cls):
        cls._registry.append(cls)

    @classmethod
    async def run_all(cls, app):
        tasks = [asyncio.create_task(plugin_cls().run(app)) for plugin_cls in cls._registry]
        await asyncio.gather(*tasks)