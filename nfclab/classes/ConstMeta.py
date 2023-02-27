class ConstMeta(type):
    class ConstError(TypeError):
        pass

    def __init__(self, name, bases, dict):
        super(ConstMeta, self).__init__(name, bases, dict)
        import sys
        sys.modules[name] = self()

    def __setattr__(self, name, value):
        if name in self.__dict__.keys():
            raise self.ConstError('No rebind')
        super(ConstMeta, self).__setattr__(name, value)
