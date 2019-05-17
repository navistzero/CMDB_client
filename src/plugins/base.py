from lib.conf.config import settings

class BasePlugin:

    def __init__(self):
        self.debug = settings.DEBUG
        self.base_dir = settings.BASE_DIR

    def get_os(self,handler,hostname):
        # 执行命令获取操作系统
        # os = handler.cmd('uname',hostname)
        # if os.capitalize() == 'Linux':
        #     return os
        # else:
        #     return 'win'
        return 'linux'

    def process(self, handler, hostname=None):
        os = self.get_os(handler,hostname)
        if os == 'win':
            return self.win(handler, hostname)
        else:
            return self.linux(handler, hostname)

    def win(self, command, hostname):
        raise NotImplementedError('win() must be Implemented')

    def linux(self, command, hostname):
        raise NotImplementedError('win() must be Implemented')