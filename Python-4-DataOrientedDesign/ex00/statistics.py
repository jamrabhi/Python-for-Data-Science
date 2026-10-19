def get_mean(nums: list[int | float]) -> float:
    """Calculate the arithmetic mean of a list of numbers."""
    mean = sum(nums) / len(nums)
    return mean

def get_median(nums: list[int | float]) -> int:
    """Calculate the median of a sorted list of numbers."""
    if (len(nums) % 2 == 0):
        median = (nums[len(nums) // 2 - 1] +
                nums[len(nums) // 2]) / 2
    else:
        median = nums[(len(nums)) // 2]
    return median

def get_quartile(nums: list[int | float]) -> list[int | float]:
    """Calculate the 25% and 75% quartiles of a sorted list."""
    quartile = [nums[len(nums) // 4],
                nums[len(nums) * 3 // 4]]
    return quartile

def get_var(nums: list[int | float]) -> float:
    """Calculate the variance of a sorted list of numbers."""
    mean = get_mean(nums)
    variance = sum((x - mean) ** 2 for x in nums) / len(nums)
    return variance

def get_std(num : list[int | float]) -> float:
    """Calculate the standard derivation of a sorted list of numbers."""
    std = get_var(num) ** 0.5
    return std


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
            print(f"mean : {get_mean(num_sorted)}")
        elif op == "median":
            print(f"median : {get_median(num_sorted)}")
        elif op == "quartile":
            print(f"quartile : {get_quartile(num_sorted)}")
        elif op == "var":
            print(f"var : {get_var(num_sorted)}")
        elif op == "std":
            print(f"std : {get_std(num_sorted)}")
