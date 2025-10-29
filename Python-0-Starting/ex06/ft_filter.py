"""filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""


def ft_filter(func, iterable):
    if func is None:
        temp_list = [item for item in iterable if item]
    else:
        temp_list = [item for item in iterable if func(item)]
    return iter(temp_list)
