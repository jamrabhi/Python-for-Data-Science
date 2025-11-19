def ft_tqdm(lst: range) -> None:
    '''The function must copy the function tqdm with the yield operator.'''
    total = len(lst)
    if total == 0:
        return
    for i, element in enumerate(lst, 1):
        progress = i / total
        bar = "█" * int(progress * 100) + " " * (100 - int(progress * 100))
        print(f"{progress * 100:3.0f}%|{bar}| {i}/{total}", end="\r")
        yield element
    print()
