class _partial_op(object):
    def __init__(self, arg, name, func):
        self.arg = arg
        self.func = func
        self.name = name

    def __or__(self, other):
        arg = self.arg
        if hasattr(arg, "__%s__" % self.name):
            func = getattr(arg, "__%s__" % self.name)
            return func(other)
        elif hasattr(other, "__r%s__" % self.name):
            func = getattr(other, "__r%s__" % self.name)
            return func(arg)
        else:
            func = self.func
            return func(arg, other)

    def __repr__(self):
        raise Exception("Don't quit evaluation of the |%s| operator halfway. It's a bad idea" % self.name)

    def __str__(self):
        return str(self)

class MiniOperator(object):
    def __init__(self, name, func=None):
        if func == None:
            if callable(name):
                name, func = name.__name__, name
            else:
                func = lambda *args, **kwargs: raise NotImplementedError("|%s| not implemented in general" % name)
        self.__name__ = self.name = name
        self.func = func

    def __ror__(self, other):
        return _partial_op(other, self.name, self.func)

    def __repr__(self):
        return "<operator |%s|>" % self.name

    def __str__(self):
        return repr(self)

if __name__ == "__main__":
    def compose(f, g):
        return lambda *args, **kwargs: f(g(*args, **kwargs))

    compose = MiniOperator(compose)
    concatmap = (lambda l: sum(l, [])) |compose| map
    assert concatmap(lambda x: [x, x + 1], range(0, 10, 2)) == range(0, 10), "`concatmap` better work!"

    class T(object):
        def __compose__(self, other): return "left-composed"
        def __rcompose__(self, other): return "right-composed"
    T = T()

    assert T |compose| map == "left-composed", "__<name>__ should overload <name>"
    assert map |compose| T == "right-composed", "__r<name>__ should overload <name>"
