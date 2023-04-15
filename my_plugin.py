from framework.plugins import Plugin

class MyPlugin(Plugin):
    def run(self, app):
        print("Running plugin my_plugin.MyPlugin...")
