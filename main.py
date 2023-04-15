from framework import newt as fw
from framework import plugins
import importlib

app = fw.Newt()

plugin = importlib.import_module("my_plugin")

plugins.Plugin.run_all(app)
app.run()