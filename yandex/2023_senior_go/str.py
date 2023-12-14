"""
Собеседование 1 (06.12.23)

Дана произвольная строка состоящая из символо 0 1 и O

Надо найти максимальное расстояние между 0, 1

Сложность: O(n) - линейная
"""

SYMBOLS: list = ["0", "1"]
def max_size(items: str) -> int:
    if len(items) < 2:
        return 0
    size: int = 0
    last_symbol: str = ""
    max_size: int = 0
    for item in items:
        if item in SYMBOLS:
            if last_symbol and last_symbol != item:
                if size > max_size:
                    max_size = size
            last_symbol = item
            size = 1
        else:
            size += 1

    return max_size

""" 
[Тест кейсы]
"""
t1: bool = max_size("") # 0
t2: bool = max_size("0") # 0
t3: bool = max_size("1") # 0
t4: bool = max_size("01") # 1
t5: bool = max_size("0OOOO1") # 5
t6: bool = max_size("1OO0OOOO1") # 5
print(t1,t2,t3,t4,t5,t6)
