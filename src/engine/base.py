import abc
from concurrent.futures import ThreadPoolExecutor
import json
from lib.conf.config import settings

# class BaseHandler(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def handler(self):
#         pass

class BaseHandler():

    def __init__(self):
        self.asset_api = settings.ASSET_API

    def cmd(self, command, hostname):
        raise NotImplementedError('cmd() must be Implemented')

    def handler(self):
        raise NotImplementedError('handler() must be Implemented')


class SshAndSaltHandler(BaseHandler):
    def handler(self):
        """
        SSH模式采集资产
        :return:
        """
        # 1. 通过API获取未采集资产的主机列表
        res = requests.get(url=self.asset_api)
        host_list = res.json()

        pool = ThreadPoolExecutor(20)

        # 循环主机列表  提交任务
        for hostname in host_list:
            pool.submit(self.task, hostname)

    def task(self, hostname):
        # 采集硬盘、内存、网卡
        info = get_server_info(self, hostname)

        # 发送到API
        # res = requests.post(
        #     url=self.asset_api,
        #     data=json.dumps(info).encode('utf-8')
        # )
        # print(res.text)
        print(info)