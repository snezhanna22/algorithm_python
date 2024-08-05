
#функция для хранения наименьшего значения, и наименьшего индекса
def find_small(lst):
    small_list = lst[0]
    small_list_index = 0
    for i in range(1, len(lst)):
        if lst[i] < small_list:
            small_list_index = i
    return small_list_index

#функция сортировки выбором 
def selection_sort(lst):
    new_lst = []
    for i in range(len(lst)):
        small_list = find_small(lst)
        new_lst.append(lst.pop(small_list))
    return new_lst

lst = [1, 5, 3, 6, 8, 0, 2]

result = selection_sort(lst)
print(result)