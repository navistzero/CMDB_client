from lib.conf.config import settings
from lib.import_string import get_class


def get_server_info(handler, hostname=None):
    # 根据配置获取相应的硬件的信息
    info = {}
    for name, path in settings.PLUGINS_DICT.items():
        cls = get_class(path)
        obj = cls()
        info[name] = obj.process(handler, hostname)
    return info
