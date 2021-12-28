_builtin_map = map
_builtin_filter = filter


def reduce(iterable, acc, fun):
    for x in iterable:
        acc = fun(x, acc)
    return acc


def map(iterable, fun):
    return _builtin_map(fun, iterable)


def filter(iterable, fun):
    return _builtin_filter(fun, iterable)


def each(iterable, fun):
    iterable = [x for x in iterable]
    [fun(x) for x in iterable]
    return iterable
