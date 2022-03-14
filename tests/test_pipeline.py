from python_funky.Pipeline import Pipeline
from python_funky.standalone import reduce, each


def test_pipeline_map():
    result = Pipeline([1, 2, 3]) \
        .map(lambda x: x * 2).then(list).get()
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
        .map(lambda x: x * x) \
        .filter(lambda x: x % 2 != 0) \
        .each(lambda x: intermediates.append(x)) \
        .reduce(0, lambda x, acc: x + acc) \
        .then(lambda x: range(0, x)) \
        .then(sum) \
        .get()
    assert result == 45
    assert intermediates == [1, 9]


def test_pipeline_with_kwargs():
    result = Pipeline([1, 2, 3])\
        .then(sorted, reverse=True)\
        .get()
    assert result == [3, 2, 1]
