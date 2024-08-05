
def binary_search(lst, item):
    start = 0
    end = len(lst) - 1

    while start <= end:
        seredina = (start + end) // 2
        g = lst[seredina]

        if g == item:
            return g
        if g < item:
            start = seredina + 1
        else:
            end = seredina - 1
    return None

list1 = [1, 2, 5, 6, 8, 9, 0, 3]
list = sorted(list1)

result = binary_search(list, 0)
print(result)