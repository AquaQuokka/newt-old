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
