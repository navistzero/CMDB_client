# 硬盘  采集硬盘 解析数据
# from lib.conf.config import settings
#
#
# def get_disk(handler, hostname=None):
#     # 采集信息
#     # 命令一样 执行命令的方式不一样
#     ret = handler.cmd('dir', hostname)
#     print(ret)

class Disk():
    def process(self, handler, hostname=None):
        # 执行命令
        ret = handler.cmd('dir', hostname)
        return ret[10:20]