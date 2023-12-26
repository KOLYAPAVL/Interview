"""" 
Задача: Дан список чисел a, отсортированный. Дан индекс элемента (index) из списка. 
Так же дано число k.
Цель: вернуть k чисел, из списка a, ближайших к a[index]
"""

from typing import List, Optional

def find_nums(a: List, index: int, k: int) -> List[int]:
    if not a or k <= 0:
        return []

    length: int = len(a)
    left: int = index - 1 # Левый указатель
    right: int = index + 1 # Правый указатель
    target = a[index]
    numbers: List[int] = [target]
    
    while len(numbers) < k and (left >= 0 or right < length):
        l_value: Optional[int] = a[left] if left >= 0 else None
        r_value: Optional[int] = a[right] if right < length else None
        
        if l_value is None:
            numbers.append(r_value)
            right += 1
            continue
        if r_value is None:
            numbers.append(l_value)
            left += 1
            continue
        
        razn_1: int = target - l_value
        razn_2: int = r_value - target
        
        if razn_1 < razn_2:
            numbers.append(l_value)
            left += 1
        else:
            numbers.append(r_value)
            right += 1

    return numbers

""" 
Тест кейсы
"""

print(find_nums([5,8,9,15,22,40], index=4, k=2)) # [22, 15]
print(find_nums([5,8,9,15,22,40], index=2, k=5)) # [9, 8, 9, 15, 22]
