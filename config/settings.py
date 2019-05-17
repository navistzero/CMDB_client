import os

ENGINE_DICT = {
	'agent': 'src.engine.agent.AgentHandler',
	'ssh': 'src.engine.ssh.SshHandler',
	'salt': 'src.engine.salt.SaltHandler',
}
PLUGINS_DICT = {
    'disk': 'src.plugins.disk.Disk',
    'memory': 'src.plugins.memory.Memory',
    'NIC': 'src.plugins.nic.NIC',
}
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME="lijun"
AGE="18"
ENGINE="agent"
DEBUG = True
ASSET_API = 'http://127.0.0.1:8000/asset/'