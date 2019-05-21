# 硬盘  采集硬盘 解析数据
# from lib.conf.config import settings
#
#
# def get_disk(handler, hostname=None):
#     # 采集信息
#     # 命令一样 执行命令的方式不一样
#     ret = handler.cmd('dir', hostname)
#     print(ret)
# from src.plugins.whichsystem import SystemType
from .base import BasePlugin
import os
import traceback
from lib.response import BaseResponse
from lib.logger import logger

class BOARD(BasePlugin):
    def win(self,handler, hostname):
        ret = handler.cmd('dir', hostname)
        return ret[10:20]

    def linux(self,handler, hostname):
        # linux 执行命令
        # result = {'status': True, 'error': None, 'data': None}
        result = BaseResponse()
        try:
            if self.debug:
                # 读取文件信息
                with open(os.path.join(self.base_dir,'files','board.out')) as f:
                    ret = f.read()
            else:
                ret = handler.cmd('sudo dmidecode -t1',hostname)
            result.data = self.parse(ret)
        except Exception as e:
            result.status=False
            result.error=traceback.format_exc()
            logger.error(result.error)
        return result.dict
    def parse(self, content):
        
        result = {}
        key_map = {
            'Manufacturer': 'manufacturer',
            'Product Name': 'model',
            'Serial Number': 'sn',
        }
        
        for item in content.split('\n'):
            row_data = item.strip().split(':')
            if len(row_data) == 2:
                if row_data[0] in key_map:
                    result[key_map[row_data[0]]] = row_data[1].strip()
        
        return result