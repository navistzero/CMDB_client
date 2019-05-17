from src.engine.base import BaseHandler

class SshHandler(BaseHandler):

    def cmd(self, command, hostname):
        import paramiko
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=hostname, port=settings.SSH_PORT, username=settings.USER, password=settings.PASSWORD)
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.read()
        # 关闭连接
        ssh.close()
        return result
