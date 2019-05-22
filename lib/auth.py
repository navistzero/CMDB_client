import hashlib
from lib.conf.config import settings


def gen_key(ctime):
    key = "{}|{}".format(settings.AUTH_KEY, ctime)

    md5 = hashlib.md5()
    md5.update(key.encode('utf-8'))

    return md5.hexdigest()