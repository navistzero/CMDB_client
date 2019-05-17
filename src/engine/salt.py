
from src.engine.base import BaseHandler

class SaltHandler(BaseHandler):

    def cmd(self, command, hostname):
        import salt.client
        local = salt.client.LocalClient()
        result = local.cmd(hostname, 'cmd.run', [command])
        return result[hostname]

    def handler(self):
        """
        salt模式采集资产
        :return:
        """
        pass