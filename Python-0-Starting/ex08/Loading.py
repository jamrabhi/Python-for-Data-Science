import os


def ft_tqdm(lst: range) -> None:
    '''The function must copy the function tqdm with the yield operator.'''
    total = len(lst)
    if total == 0:
        return
    try:
        len_term = max(60, os.get_terminal_size().columns - (34 + 2 * len(str(total))))
    except OSError:
        len_term = 60
    for i, element in enumerate(lst, 1):
        progress = i / total
        bar = "█" * int(progress * len_term) + " " * (len_term -
                                                      int(progress * len_term))
        print(f"\r{progress * 100:3.0f}%|{bar}| {i}/{total}", end="")
        yield element
    print()
