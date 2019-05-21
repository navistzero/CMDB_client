import os
from config.settings import BASE_DIR

EMAIL = 'SS@qq.com'
SSH_PORT = 22

LOG_NAME = 'cmdb'
LOG_FILE_PATH = os.path.join(BASE_DIR, 'log', 'cmdb.log')