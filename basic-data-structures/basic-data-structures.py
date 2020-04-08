from pprint import pprint

# practise №1
sites = {
    'Kiev': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = dict()

kiev = sites['Kiev']
paris = sites['Paris']
london = sites['London']

kiev_paris = ((kiev[0]-paris[0])**2+(kiev[1]-paris[1])**2) ** .5
kiev_london = ((kiev[0]-london[0])**2+(kiev[1]-london[1])**2) ** .5
paris_london = ((paris[0]-london[0])**2+(paris[1]-london[1])**2) ** .5

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
radius = 42
point = (23, 34)
point_2 = (30, 30)


def square(r):
    area_circle = 3.1415926 * (r**2)
    return area_circle


square_circle = round(square(radius), 4)
print(square_circle)


def origin_point(x, y):
    op = ((x**2)+(y**2))**0.5
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
result = ((1*(3-2))+4)*5
print(result)

# practise №4

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




