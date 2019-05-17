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
import re

class Disk(BasePlugin):
    # def __init__(self):
    #     super().__init__()
    def win(self,handler, hostname):
        ret = handler.cmd('dir', hostname)
        return ret[10:20]

    def linux(self,handler, hostname):
        # linux 执行命令
        if self.debug:
            # 读取文件信息
            with open(os.path.join(self.base_dir,'files','disk.out')) as f:
                ret = f.read()
        else:
            ret = handler.cmd('sudo MegaCli  -PDList -aALL',hostname)
        return self.parse(ret)

    def parse(self, content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        response = {}
        result = []
        for row_line in content.split("\n\n\n\n"):
            result.append(row_line)
        for item in result:
            temp_dict = {}
            for row in item.split('\n'):
                if not row.strip():
                    continue
                if len(row.split(':')) != 2:
                    continue
                key, value = row.split(':')
                name = self.mega_patter_match(key)
                if name:
                    if key == 'Raw Size':
                        raw_size = re.search('(\d+\.\d+)', value.strip())
                        if raw_size:
                            temp_dict[name] = raw_size.group()
                        else:
                            raw_size = '0'
                    else:
                        temp_dict[name] = value.strip()
            if temp_dict:
                response[temp_dict['slot']] = temp_dict
        return response

    @staticmethod
    def mega_patter_match(needle):
        grep_pattern = {'Slot': 'slot', 'Raw Size': 'capacity', 'Inquiry': 'model', 'PD Type': 'pd_type'}
        for key, value in grep_pattern.items():
            if needle.startswith(key):
                return value
        return False