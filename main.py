from framework import newt as fw
from framework import plugins
import importlib

app = fw.Newt()

plugin = importlib.import_module("plugin")

plugins.Plugin.run_all(app)
app.run()
