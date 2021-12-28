from python_funky.Pipeline import Pipeline
from python_funky.standalone import reduce, each


def test_pipeline_map():
    result = Pipeline([1, 2, 3]) \
        .map(lambda x: x * 2).get()
    assert result == [2, 4, 6]


def test_map_filter_reduce():
    result = Pipeline([1, 2, 3]) \
        .map(lambda x: x * x) \
        .filter(lambda x: x % 2 != 0) \
        .reduce(0, lambda x, acc: x + acc) \
        .get()
    assert result == 10


def test_pipeline_full():
    intermediates = []
    result = Pipeline([1, 2, 3]) \
        .then(map, lambda x: x * x) \
        .then(filter, lambda x: x % 2 != 0) \
        .then(each, lambda x: intermediates.append(x)) \
        .then(reduce, 0, lambda x, acc: x + acc) \
        .then(lambda x: range(0, x)) \
        .then(sum) \
        .get()
    assert result == 45
    assert intermediates == [1, 9]
