import os


def ft_tqdm(lst: range) -> None:
    '''The function must copy the function tqdm with the yield operator.'''
    total = len(lst)
    if total == 0:
        return

    try:
        term_cols = os.get_terminal_size().columns
    except OSError:
        term_cols = 40
    term_width = max(40, term_cols - (34 + 2 * len(str(total))))

    for i, element in enumerate(lst, 1):
        progress = i / total
        filled = progress * term_width
        bar = "█" * int(filled) + " " * (term_width - int(filled))
        print(f"\r{progress * 100:3.0f}%|{bar}| {i}/{total}", end="")
        yield element
    print()
