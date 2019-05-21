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
import traceback
from lib.response import BaseResponse
from lib.logger import logger

class CPU(BasePlugin):
    def win(self,handler, hostname):
        ret = handler.cmd('dir', hostname)
        return ret[10:20]

    def linux(self,handler, hostname):
        # linux 执行命令
        result = BaseResponse()
        try:
            if self.debug:
                # 读取文件信息
                with open(os.path.join(self.base_dir,'files','cpuinfo.out')) as f:
                    ret = f.read()
            else:
                ret = handler.cmd('cat /proc/cpuinfo',hostname)
            result.data = self.parse(ret)
        except Exception as e:
            result.status=False
            result.error=traceback.format_exc()
            logger.error(result.error)
        return result.dict

    @staticmethod
    def parse(content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        response = {'cpu_count': 0, 'cpu_physical_count': 0, 'cpu_model': ''}

        cpu_physical_set = set()
        content = content.strip()
        for item in content.split('\n\n'):
            for row_line in item.split('\n'):
                key, value = row_line.split(':')
                key = key.strip()
                if key == 'processor':
                    response['cpu_count'] += 1
                elif key == 'physical id':
                    cpu_physical_set.add(value)
                elif key == 'model name':
                    if not response['cpu_model']:
                        response['cpu_model'] = value
        response['cpu_physical_count'] = len(cpu_physical_set)

        return response
    # def parse(self, content):
    #     """
    #     解析shell命令返回结果
    #     :param content: shell 命令结果
    #     :return:解析后的结果
    #     """
    #     response = {}
    #     result = []
    #     for row_line in content.split("\n\n"):
    #         result.append(row_line)
    #     for item in result:
    #         temp_dict = {}
    #         for row in item.split('\n'):
    #             if not row.strip():
    #                 continue
    #             if len(row.split(':')) != 2:
    #                 continue
    #             key, value = row.split(':')
    #             name = key
    #             if name:
    #                 if key.startswith('flags'):
    #                     temp_dict[name.strip()] = value[:15]
    #                 else:
    #                     temp_dict[name.strip()] = value.strip()
    #         if temp_dict:               
    #             response[temp_dict['processor']] = temp_dict
    #     return response
