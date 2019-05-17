from .engine import agent
from .engine import ssh
from .engine import salt
from lib.conf.config import settings
import importlib
from lib.import_string import get_class

def run():
    engin_path=settings.ENGINE_DICT[settings.ENGINE]
    cls=get_class(engin_path)
    obj=cls()
    obj.handler()