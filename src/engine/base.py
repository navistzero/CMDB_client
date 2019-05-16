import abc

# class BaseHandler(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def handler(self):
#         pass

class BaseHandler():

    def handler(self):
        raise NotImplementedError('handler() must be Implemented')