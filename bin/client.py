import os
import sys

os.environ['USER_SETTINGS']='config.settings'
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.conf.config import settings
print(settings.NAME)