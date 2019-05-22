from src.engine.base import BaseHandler
from ..plugins import get_server_info
import requests
import json
from lib.conf.config import settings
import os
import time
from lib.auth import gen_key

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
        cert_path = settings.CERT_PATH
        if not os.path.exists(cert_path):
            # 没有文件 当前是新增主机
            info['type'] = 'create'
        else:
            # 修改
            with open(cert_path, 'r', encoding='utf-8') as f:
                cert = f.read()  # 原主机名

            hostname = info['basic']['data']['hostname']
            if cert == hostname:
                # 更新资产
                info['type'] = 'update'
            else:
                # 更改主机名 +  更新资产
                info['type'] = 'host_update'
                info['hostname'] = cert

        # ctime = time.time()
        ctime = 1
        key = gen_key(ctime)

        res = requests.post(
            url=self.asset_api,
            params={'key': key, 'ctime': ctime},
            data=json.dumps(info).encode('utf-8'),
            headers={'Content-Type':'application/json'}
        )
        response = res.json()
        print(response.get("msg"))
        # if response.get('status'):
        #     # 把主机名写入到文件中
        #     with open(cert_path, 'w', encoding='utf-8') as f:
        #         f.write(response.get('hostname'))
        # print(res.text)