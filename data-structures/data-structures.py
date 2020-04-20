from pprint import pprint

# list
print('---list')
arr = []
print(arr)


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
    print(list_select_numb)
    print(len(list_select_numb))
    return list_select_numb


arr = list_method(arr)
print(arr)

# tuple
print('---tuple')


def tuple_method_dif(ar):
    tpl = tuple(ar)
    print(len(tpl))
    print(tpl)
    print(type(tpl))
    lst = list(tpl)
    print(len(lst))
    print(lst)
    print(type(lst))


tuple_method_dif(arr)

# dict
print('---dict')

dct = {}


def dict_method(dc):
    dc['bmw'] = {}
    dc['ford'] = {}
    dc['porsche'] = {}
    dc['mercedes'] = {}
    dc['volkswagen'] = {}

    dc['bmw'][1] = 'i8'
    dc['bmw'][2] = 'Z4 Roadster'
    dc['bmw'][3] = '6-series Gran Turismo'

    dc['ford'][1] = 'Focus'
    dc['ford'][2] = 'Fiesta'
    dc['ford'][3] = 'Mondeo'

    dc['porsche'][1] = 'Cayman'
    dc['porsche'][2] = 'Boxster'
    dc['porsche'][3] = '911'

    dc['mercedes'][1] = 'A-Clas'
    dc['mercedes'][2] = 'AMG GT'
    dc['mercedes'][3] = 'AMG GT Roadster'

    dc['volkswagen'][1] = 'Polo'
    dc['volkswagen'][2] = 'Golf'
    dc['volkswagen'][3] = 'Passat'

    pprint(dc)

    dc_keys = dc.keys()
    dc_values = dc.values()

    def keys_output(dc_):
        ar_car = []
        for el in dc_:
            ar_car.append(el)
        return ar_car

    print(keys_output(dc_keys))

    def values_output(dc_):
        ar_car = []
        ar_bmw = []
        ar_ford = []
        ar_porsche = []
        ar_mercedes = []
        ar_volkswagen = []

        for el in dc_:
            ar_car.append(el)
        for key in ar_car[0]:
            ar_bmw.append(ar_car[0][key])
        print(ar_bmw)
        for key in ar_car[1]:
            ar_ford.append(ar_car[1][key])
        print(ar_ford)
        for key in ar_car[2]:
            ar_porsche.append(ar_car[2][key])
        print(ar_porsche)
        for key in ar_car[3]:
            ar_mercedes.append(ar_car[3][key])
        print(ar_mercedes)
        for key in ar_car[4]:
            ar_volkswagen.append(ar_car[4][key])
        print(ar_volkswagen)

        ar_model = ar_bmw + ar_ford + ar_porsche + ar_mercedes + ar_volkswagen
        return ar_model

    ar_model_car = values_output(dc_values)
    print(ar_model_car)


dict_method(dct)


# sequence
print('---sequence')


# set
print('---set')
