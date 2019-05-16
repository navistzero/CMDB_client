from src.engine.base import BaseHandler

class SshHandler(BaseHandler):

    def handler(self):
        """
        Agent模式采集资产
        :return:
        """
        print('ssh')