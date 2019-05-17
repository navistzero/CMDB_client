from src.engine.base import BaseHandler
from ..plugins import get_server_info

class AgentHandler(BaseHandler):

    def cmd(self, command, hostname):
        import subprocess
        ret = subprocess.getoutput(command)
        return ret

    def handler(self):
        """
        Agent模式采集资产
        :return:
        """
        # 采集硬盘、内存、网卡
        ret = get_server_info(self)
        print(ret)