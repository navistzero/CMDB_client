import os
import importlib
from . import global_settings

class Settings():
    def __init__(self):
        for i in dir(global_settings):
            if i.isupper():
                val = getattr(global_settings,i)
                setattr(self,i,val)
        config_str=os.environ["USER_SETTINGS"]
        module=importlib.import_module(config_str)
        for i in dir(module):
            if i.isupper():
                val = getattr(module,i)
                setattr(self,i,val)
        

settings=Settings()