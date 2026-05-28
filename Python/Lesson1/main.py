# a = 3
# b = 2
# summa = a + b
# raznost = a - b
# proizvedenie = a * b
# castnoe = a / b
# print('summa = ', summa)
# print('raznost = ', raznost)
# print('proizvedenie = ', proizvedenie)
# print('castnoe = ', castnoe)


# name = input('Введите имя: ')
# vozrast = input('Введите возраст: ')

# print('Привет, ', name, '. Через год вам будет ' , int(vozrast) + 1, ' лет')

# dlina = input('Введите длину прямоугольника: ')
# shirina = input('Введите ширину прямоугольника: ')

# print ('Площадь прямоугольника равна: ', int(dlina) * int(shirina))

# slovo = input('Vvedite slovo:')
# cislo = input('Vvedite kolichestvo povtorenii:')
# print(slovo * int(cislo))

# a = int(input('Vvedite pervoe celoe cislo:'))
# b = int(input('Vvedite vtoroe celoe cislo:'))
# c = int(input('Vvedite trete celoe cislo:'))
# result = (a + b) * c - (a % b)
# print('(a + b) * c - (a % b) = ', result)

# radius = float(input('Vvedite radius kruga:'))
# pi = 3.14
# plosad = pi * radius ** 2
# print(plosad)

# x = 10
# y = 5
# print('Summa = ', x + y)
# print('Raznost = ', x - y)
# print('Proizvedenie = ', x * y)
# print('Castnoe = ', x / y)
# print('Celoe ot delenija = ', x // y)
# print('Ostatok ot delenija = ', x % y)
# print('Stepen = ', x ** y)


# name = input('Vvedite svoe imja:')
# print('Привет, ' + name + '!', 'Добро пожаловать в мир Python!')

# cislo1 = float(input('Vvedite pervoe cislo:'))
# cislo2 = float(input('Vvedite vtoroe cislo:'))
# cislo3 = float(input('Vvedite trete cislo:'))

# result = (cislo1 + cislo2 + cislo3) / 3

# print('Srednee arifmeticheskoe:', result)


# celcii =float(input('Vvedite temperaturu v gradusah celcija:'))
# farengeit = celcii  * 9/5 + 32
# print('Temperatura v gradusah po Farengeitu', farengeit)

# minuta = int(input('Vvedite kolichestvo minut:'))
# chas = minuta // 60
# ostatok = minuta % 60

# print('Eto', chas, 'chasov i', ostatok, 'minut')

# radius = float(input('Vvedite radius:'))
# pi = 3.14
# dlina = 2 * pi * radius
# print('Dlina okruzhnosti ravna', dlina)

cislo = int(input('Vvedite trechznachnoe cislo'))
sotni = cislo // 100
print(sotni)
desjatki = (cislo - sotni * 100) // 10
print(desjatki)
edinici = cislo - sotni * 100 - desjatki * 10
resultat = sotni + desjatki + edinici
print('Summa cifr', resultat)






