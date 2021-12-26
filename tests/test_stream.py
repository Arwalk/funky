from funky.Stream import Stream


def test_map():
    result = Stream([1, 2, 3]) \
        .map(lambda x: x * 2) \
        .as_list()
    assert result == [2, 4, 6]


def test_map_filter_reduce():
    result = Stream([1, 2, 3]) \
        .map(lambda x: x * x) \
        .filter(lambda x: x % 2 != 0) \
        .reduce(0, lambda x, acc: x + acc)

    assert result == 10
