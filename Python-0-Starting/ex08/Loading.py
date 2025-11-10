def ft_tqdm(lst: range) -> None:
    '''The function must copy the function tqdm with the yield operator.'''
    total = len(lst)
    for i, item in enumerate(lst, 0):
        percent = i / total * 100
        bar = "█" * int(i / total * 100) + "-" * (100 - int(i / total * 100))
        print(f"\r{percent:3.0f}%|{bar}|", end="")
        yield item
    print()
