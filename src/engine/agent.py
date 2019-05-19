from src.engine.base import BaseHandler
from ..plugins import get_server_info
import requests
import json

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
        info = get_server_info(self)
        res = requests.post(
            url=self.asset_api,
            data=json.dumps(info).encode('utf-8'),
            headers={'Content-Type':'application/json'}
        )
        print(res.text)