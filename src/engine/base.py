import abc

# class BaseHandler(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def handler(self):
#         pass

class BaseHandler():

    def cmd(self, command, hostname):
        raise NotImplementedError('cmd() must be Implemented')

    def handler(self):
        raise NotImplementedError('handler() must be Implemented')