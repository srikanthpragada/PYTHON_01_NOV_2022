def count_upper(st: str) -> int:
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count


print(count_upper("Hello"), count_upper("AbCdE"))
