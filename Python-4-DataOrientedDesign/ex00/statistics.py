def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Makes statistics about the given arguments and keyword arguments."""
    valid_stats = ("mean", "median", "quartile", "std", "var")

    if not all(isinstance(arg, (int, float)) for arg in args):
        print("ERROR")
        return None

    num_sorted = sorted(args)
    for op in kwargs.values():
        if not args :
            print("ERROR")
        elif op == "mean":
            mean = sum(num_sorted) / len(num_sorted)
            print(mean)
        elif op == "median":
            if (len(num_sorted) % 2 == 0):
                median = (num_sorted[len(num_sorted) // 2 - 1] +
                        num_sorted[len(num_sorted) // 2]) / 2
            else:
                median = num_sorted[(len(num_sorted)) // 2]
            print(median)
        elif op == "quartile":
            quartile = [num_sorted[len(num_sorted) // 4], num_sorted[len(num_sorted) * 3 // 4]]
            print(quartile)

    