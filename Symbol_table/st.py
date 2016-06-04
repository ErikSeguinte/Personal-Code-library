import __future__
import abc

class ST(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def put(self, key, value):
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, key):
        raise NotImplementedError()
    def delete(self, key):
        self.put(key, None)
    def contains(self, key,):
        return (self.get(key) is not None)
    def isEmpty(self):
        return self.size == 0
    @abc.abstractmethod
    def size(self, node):
        raise NotImplementedError()

    @abc.abstractmethod
    def keys(self):
        raise NotImplementedError()
