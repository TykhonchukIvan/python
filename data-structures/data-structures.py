from pprint import pprint

# list
print('---list')
arr = []


def list_method(array):
    array.append('el')
    print(array)
    array.append([])
    print(array)
    array.append({})
    print(array)
    arr_1 = [1, 2, 3]
    array.extend(arr_1)
    print(array)
    array.reverse()
    print(array)
    arr_2 = array.copy()
    print(arr_2)
    arr_2.clear()
    array.extend(array)
    print(array)
    el_1 = array.count(3)
    print(el_1)
    arr_3 = ['a', 'b', 'c', 'd', 'e']
    array.extend(arr_3)
    print(array)
    array.reverse()
    print(array)

    def number_selection(ar):
        ar_number = [1, 2, 10, 45, 4, 5, 9, 8, 2, 4, 7, 1]
        list_select = []
        list_select.extend(ar_number)
        for el in ar:
            if type(el) == int:
                list_select.append(el)
            else:
                ar.remove(el)
        return list_select

    list_select_numb = number_selection(array)
    print(list_select_numb)
    list_select_numb.sort()
    list_select_numb.reverse()
    pprint(list_select_numb)
    return list_select_numb


list_method(arr)

# tuple

# def tuple_method(tuple):
