class Memory():
    def process(self, handler, hostname=None):
        # 执行命令
        ret = handler.cmd('wmic memorychip', hostname)

        return ret[10:20]