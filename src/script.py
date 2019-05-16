from .engine import agent
from .engine import ssh
from .engine import salt
from lib.conf.config import settings
import importlib

def run():
    engin_path=settings.ENGINE_DICT[settings.ENGINE]
    module_str,engine_str=engin_path.rsplit(".",maxsplit=1)
    module=importlib.import_module(module_str)
    cls=getattr(module,engine_str)
    obj=cls()
    obj.handler()