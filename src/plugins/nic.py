class NIC():
    def process(self, handler, hostname=None):
        # 执行命令
        ret = handler.cmd('ipconfig', hostname)

        return ret[10:20]