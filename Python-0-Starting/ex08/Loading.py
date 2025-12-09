def ft_tqdm(lst: range) -> None:
    '''The function must copy the function tqdm with the yield operator.'''
    total = len(lst)
    if total == 0:
        return
    for i, element in enumerate(lst, 1):
        progress = i / total
        bar = "█" * int(progress * 60) + " " * (60 - int(progress * 60))
        print(f"\r{progress * 100:3.0f}%|{bar}| {i}/{total}", end="")
        yield element
    print()
