""" 
Собеседование 2 (13.12.23)

Даны даты заезда и отъезда каждого гостя. 
Для каждого гостя дата заезда строго раньше даты отъезда (то есть каждый гость останавливается хотя бы на одну ночь). 
В пределах одного дня считается, что сначала старые гости выезжают, а затем въезжают новые. Найти максимальное число постояльцев, 
которые одновременно проживали в гостинице (считаем, что измерение количества постояльцев происходит в конце дня).

Сложность: O(n log n)
"""

from typing import List

def max_num_guests(guests: List[tuple]) -> int:
    d1: dict = dict()
    d2: dict = dict()
    for guest in guests:
        start: int = guest[0]
        end: int = guest[1]
        if start not in d1:
            d1[start] = 1
        else:
            d1[start] += 1
        
        if end not in d2:
            d2[end] = 1
        else:
            d2[end] += 1

    days: set[int] = set(list(d1.keys()) + list(d2.keys()))
    count: int = 0
    max_count: int = 0
    for day in sorted(days):
        profit: int = d1.get(day, 0) - d2.get(day, 0)
        count += profit
        if count > max_count:
            max_count = count
    
    return max_count

""" 
Тест кейсы
"""
t1: bool = max_num_guests([(1, 2), (1, 3), (2, 4), (2, 3)])
print(t1)
