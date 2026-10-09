def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    Находит минимальное и максимальное число в списке.
    Если список пустой, вызывает ValueError.
    """
    if len(nums) == 0:
        raise ValueError
    min = nums[0]
    max = nums[0]
    for x in nums:
        if x < min:
            min = x
        if x > max:
            max = x
    return min, max



def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    Убирает повторяющиеся числа и сортирует их по возрастанию.
    """
    unique = []
    for x in nums:
        if x not in unique:
            unique.append(x)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if unique[j] < unique[i]:
                unique[i], unique[j] = unique[j], unique[i]
    return unique



def flatten(mat: list[list | tuple]) -> list:
    """
    Объединяет списки и кортежи в один список.
    Если элемент не список и не кортеж, вызывает TypeError.
    """
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError
        for x in row:
            result.append(x)
    return result

""" print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([])) """
""" 
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0])) """

 
""" print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))   """


