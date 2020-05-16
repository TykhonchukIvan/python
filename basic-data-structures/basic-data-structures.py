from pprint import pprint

# practise №1
print('--- practise №1')
sites = {
    'Kiev': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = dict()

kiev = sites['Kiev']
paris = sites['Paris']
london = sites['London']

kiev_paris = ((kiev[0] - paris[0]) ** 2 + (kiev[1] - paris[1]) ** 2) ** .5
kiev_london = ((kiev[0] - london[0]) ** 2 + (kiev[1] - london[1]) ** 2) ** .5
paris_london = ((paris[0] - london[0]) ** 2 + (paris[1] - london[1]) ** 2) ** .5

distances['Kiev'] = {}
distances['Kiev']['Paris'] = kiev_paris
distances['Kiev']['London'] = kiev_london
distances['London'] = {}
distances['London']['Paris'] = paris_london
distances['London']['Kiev'] = kiev_london
distances['Paris'] = {}
distances['Paris']['London'] = paris_london
distances['Paris']['Kiev'] = kiev_paris

pprint(distances)

# practise №2
print('--- practise №2')
radius = 42
point = (23, 34)
point_2 = (30, 30)


def square(r):
    area_circle = 3.1415926 * (r ** 2)
    return area_circle


square_circle = round(square(radius), 4)
print(square_circle)


def origin_point(x, y):
    op = ((x ** 2) + (y ** 2)) ** 0.5
    return op


op_1 = origin_point(point[0], point[1])
op_2 = origin_point(point_2[0], point_2[1])


def point_in_circle(a, b):
    if a < b:
        print('Точка в пределах круга')
    else:
        print('Точка не в пределах круга')


point_in_circle(op_1, radius)
point_in_circle(op_2, radius)

# practise №3
print('--- practise №3')
result = ((1 * (3 - 2)) + 4) * 5
print(result)

# practise №4
print('--- practise №4')
my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

movies = dict()

movies_1 = my_favorite_movies[0:10]
movies_2 = my_favorite_movies[-15:]
movies_3 = my_favorite_movies[12:25]
movies_4 = my_favorite_movies[35:40]

movies['Первый фильм'] = movies_1
movies['Последний фильм'] = movies_2
movies['Второй фильм'] = movies_3
movies['Второй с конца фильм'] = movies_4

pprint(movies)

# practise №5
print('--- practise №5')
my_family = ['Ivan', 'Father', 'Mather', 'GirlFriendIrina']

my_family_height = [
    ['Ivan', 190],
    ['Father', 185],
    ['Mather', 170],
    ['GirlFriendIrina', 175]
]

father = 'height father - ' + str(my_family_height[1][1]) + ' centimeters'

height_family = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1]
my_family_growth = 'The overall growth of my family - ' + str(height_family) + ' centimeters'

print(father)
print(my_family_growth)

# practise №6
print('--- practise №6')
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
print(zoo)
birds = ['rooster', 'ostrich', 'lark']
zoo.insert(1, 'bear')
zoo.append(birds[0])
zoo.append(birds[1])
zoo.append(birds[2])
print(zoo)
zoo.pop(3)
print(zoo)
pprint(str(zoo.count('lion')) + ' and ' + str(zoo.count('lark')))


def search_list(ar, el, el_1):
    i = ar.index(el)
    i_2 = ar.index(el_1)
    print(str(i) + ' ' + str(i_2))


search_list(zoo, 'lion', 'lark')

# practise №7
print('--- practise №7')
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
songs_time_1 = violator_songs_list[3][1] + violator_songs_list[5][1] + violator_songs_list[8][1]
print(songs_time_1)
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
songs_time_2 = violator_songs_dict['Sweetest Perfection'] + violator_songs_dict['Policy of Truth'] + violator_songs_dict['Blue Dress']
print(songs_time_2)

# practise №8
print('--- practise №8')
secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
mes_1 = secret_message[3][7:13]
mes_2 = secret_message[4][16:21]
secret_message = secret_message[0][3] + secret_message[1][10:13] + secret_message[2][5:14:2] + mes_1[::-1] + mes_2[::-1]
print(secret_message)

# practise №9
print('--- practise №9')
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')
garden_set = set(garden)
meadow_set = set(meadow)
print(garden_set)
print(meadow_set)
print(meadow_set.union(garden_set))
print(meadow_set.difference(garden_set))
print(garden_set.difference(meadow_set))

# practise №10
print('--- practise №10')

sweets = {
    'печенье': [
        {'ашан': 'название магазина', 'price': 10.99},
        {'пятерочка': 'название магазина', 'price': 9.99},
        {'магнит': 'название магазина', 'price': 11.99},
    ],
    'конфеты': [
        {'ашан': 'название магазина', 'price': 34.99},
        {'пятерочка': 'название магазина', 'price': 32.99},
        {'магнит': 'название магазина', 'price': 30.99},
    ],
    'карамель': [
        {'ашан': 'название магазина', 'price': 45.99},
        {'пятерочка': 'название магазина', 'price': 46.99},
        {'магнит': 'название магазина', 'price': 41.99},
    ],
    'пирожное': [
        {'ашан': 'название магазина', 'price': 67.99},
        {'пятерочка': 'название магазина', 'price': 59.99},
        {'магнит': 'название магазина', 'price': 62.99},
    ],
}

pprint(sweets)

# practise №11
print('--- practise №11')

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

print(store['12345'][0]['price'])

cost_12345 = store['12345'][0]['price'] * store['12345'][0]['quantity']
cost_23456 = (store['23456'][0]['price'] * store['23456'][0]['quantity']) \
             * (store['23456'][1]['price'] * store['23456'][1]['quantity'])
cost_34567 = (store['34567'][0]['price'] * store['34567'][0]['quantity'])\
             * (store['34567'][1]['price'] * store['34567'][1]['quantity'])
cost_45678 = (store['45678'][0]['price'] * store['45678'][0]['quantity'])\
             * (store['45678'][1]['price'] * store['45678'][1]['quantity']) \
             * (store['45678'][2]['price'] * store['45678'][2]['quantity'])

quantity_12345 = store['12345'][0]['quantity']
quantity_23456 = store['23456'][0]['quantity'] + store['23456'][1]['quantity']
quantity_34567 = store['34567'][0]['quantity'] + store['34567'][1]['quantity']
quantity_45678 = store['45678'][0]['quantity'] + store['45678'][1]['quantity'] + store['45678'][2]['quantity']


stock = dict()

stock['Склад'] = {}
stock['Склад']['Количество всех ламп'] = quantity_12345
stock['Склад']['Количество всех столов'] = quantity_23456
stock['Склад']['Количество всех стулей'] = quantity_45678
stock['Склад']['Количество всех диванов'] = quantity_34567

stock['Склад']['Ценна всех ламп'] = cost_12345
stock['Склад']['Ценна всех столов'] = cost_23456
stock['Склад']['Ценна всех стулей'] = cost_34567
stock['Склад']['Ценна всех диванов'] = cost_45678

pprint(stock)
