""" 
Собеседование 2 (13.12.23)

Даны 2 слова, необходимо вернуть True если можно сделать слова одинаковыми, одним из действий:
1. Изменить один символ
2. Добавить один символ
3. Удалить один символ

Сложность алгоритма: O(n) - линейная
"""
def can_sym(word1: str, word2: str) -> bool:
    len1: int = len(word1)
    len2: int = len(word2)
    if len1 == len2:
        """Если длины строк равны, то в данном случае мы предпологаем, что надо заменить одну строку"""
        i: int = 0
        fall: int = 0
        while i < len2:
            if word1[i] != word2[i]:
                fall += 1
            if fall > 1:
                return False
            i += 1
        return True
    elif len2 - len1 == 1:
        """Если второе слово длинее первого, то предпологаем, что надо удалить один символ от туда"""
        i: int = 0
        j: int = 0
        while j < len1:
            if word1[i] == word2[j]:
                i += 1
            j += 1
            if j - i > 1:
                return False
        return True
    elif len1 - len2 == 1:
        """Если первое слово длинее второго, то предпологаем, что надо добавить один символ во второе слово"""
        i: int = 0
        j: int = 0
        while i < len2:
            if word1[i] == word2[j]:
                j += 1
            i += 1
            if i - j > 1:
                return False
        return True
    
    return False

"""
[Тест-кейсы]
"""
t1: bool = can_sym("tea", "tet") # True
t2: bool = can_sym("tea", "eae") # False
t3: bool = can_sym("tea", "teat") # True
t4: bool = can_sym("tea", "teta") # True
t5: bool = can_sym("tea", "teatt") # False
t6: bool = can_sym("tea", "te") # True
t7: bool = can_sym("tea", "ta") # True
t8: bool = can_sym("tea", "t") # False

print(t1, t2, t3, t4, t5, t6, t7, t8)
