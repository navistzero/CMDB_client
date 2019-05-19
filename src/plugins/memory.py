from .base import BasePlugin
import os
from lib import convert
from lib.response import BaseResponse
import traceback

class Memory(BasePlugin):
    # def process(self, handler, hostname=None):
    #     # 执行命令
    #     ret = handler.cmd('wmic memorychip', hostname)
    #
    #     return ret[10:20]

    def win(self,handler, hostname):
        ret = handler.cmd('wmic memorychip', hostname)
        return ret[10:20]

    def linux(self,handler, hostname):
        # linux 执行命令
        result = BaseResponse()
        try:
            if self.debug:
                # 读取文件信息
                with open(os.path.join(self.base_dir,'files','memory.out')) as f:
                    ret = f.read()
            else:
                ret = handler.cmd('sudo dmidecode  -q -t 17 2>/dev/null', hostname)[:60]
            result.data = self.parse(ret)
        except Exception as e:
            # result['status'] = False
            # result['error'] = traceback.format_exc()
            result.status=False
            result.error=traceback.format_exc()
        return result.dict

    def parse(self, content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        ram_dict = {}
        key_map = {
            'Size': 'capacity',
            'Locator': 'slot',
            'Type': 'model',
            'Speed': 'speed',
            'Manufacturer': 'manufacturer',
            'Serial Number': 'sn',

        }
        devices = content.split('Memory Device')
        for item in devices:
            item = item.strip()
            if not item:
                continue
            if item.startswith('#'):
                continue
            segment = {}
            lines = item.split('\n\t')
            for line in lines:
                if len(line.split(':')) > 1:
                    key, value = line.split(':')
                else:
                    key = line.split(':')[0]
                    value = ""
                if key in key_map:
                    if key == 'Size':
                        segment[key_map['Size']] = convert.convert_mb_to_gb(value, 0)
                    else:
                        segment[key_map[key.strip()]] = value.strip()
            ram_dict[segment['slot']] = segment

        return ram_dict