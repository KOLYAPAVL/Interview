"""
[Собеседования 1. 06.12.23]

Дан массив точек с целочисленными координатам (x,y).

Определить, существует ли вертикальная прямая,
делящая точки на 2 симметричных, относительно этой прямой набора точек
"""

""" 
Сложность алгоритма: O(n log N), т.к. сортировка
"""


from typing import List, Optional


def is_vert_sym(lst: List[tuple[int, int]]) -> bool:
    if not lst or len(lst) == 1:
        return True
    y_points: dict[list[int]] = dict()
    for item in lst:
        x, y = item[0], item[1]
        if y not in y_points:
            y_points[y] = [x]
        else:
            y_points[y].append(x)

    sred: Optional[float] = None
    for y in y_points:
        x_items = y_points[y]
        x_items.sort()
        i: int = 0
        length: int = len(x_items)
        while i < length // 2:
            local_sred: float = (x_items[-i-1] - x_items[i]) / 2 + x_items[i]
            if sred is None:
                sred = local_sred
            elif sred != local_sred:
                return False
            i += 1
        
        if length % 2 != 0:
            central: int = x_items[length // 2]
            if sred is None:
                sred = central
            elif sred != central:
                return False

    return True

""" 
[Тест кейсы]
"""
t1: bool = is_vert_sym([(0,0), (0,0), (1,1), (2,2), (3,1), (4,0), (4,0)]) # True
t2: bool = is_vert_sym([(0,0), (0,0), (1,1), (2,2), (3,1), (4,0)]) # False
t3: bool = is_vert_sym([]) # True
t4: bool = is_vert_sym([(0,0)]) # True
t5: bool = is_vert_sym([(0,0), (10, 0)]) # True
t6: bool = is_vert_sym([(0,0), (11, 1)]) # False
t7: bool = is_vert_sym([(0,0), (1, 0), (3, 0)]) # False
t8: bool = is_vert_sym([(0,0), (1, 0), (2, 0)]) # True

print(t1,t2,t3,t4,t5,t6,t7,t8)
