import os
import sys

os.environ['USER_SETTINGS']='config.settings'
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.conf.config import settings
 
from src.script import run

if __name__=="__main__":
    run()