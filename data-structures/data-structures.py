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
    return array


list_method(arr)

#tuple