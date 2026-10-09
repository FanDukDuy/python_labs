### Лабораторная работа 2

#### Задание 1
  

```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
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



def unique_sorted(nums):
    unique = []
    for x in nums:
        if x not in unique:
            unique.append(x)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if unique[j] < unique[i]:
                unique[i], unique[j] = unique[j], unique[i]
    return unique



def flatten(mat):
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError
        for x in row:
            result.append(x)
    return result

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3,4,5)]))
print(flatten([[1], [], [2,3]]))
print(flatten([[1, 2], 'ab']))
```

![](../../images/lab02/01.png/012.png/013.png)
