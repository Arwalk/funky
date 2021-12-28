from .standalone import reduce, map, filter, _builtin_map, _builtin_filter


class Pipeline:
    _auto_transform = {
        _builtin_map: map,
        _builtin_filter: filter,
    }

    def __init__(self, start) -> None:
        self._start_value = start
        self._operations = []

    def then(self, fun, *args) -> 'Pipeline':
        fun = self._auto_transform.get(fun, fun)
        self._operations.append(lambda x: fun(x, *args))
        return self

    def map(self, fun) -> 'Pipeline':
        return self.then(map, fun)

    def filter(self, fun) -> 'Pipeline':
        return self.then(filter, fun)

    def reduce(self, acc, fun) -> 'Pipeline':
        return self.then(reduce, acc, fun)

    def get(self):
        val = reduce(self._operations, self._start_value, lambda op, acc: op(acc))
        try:
            return [x for x in val]
        except:
            return val
