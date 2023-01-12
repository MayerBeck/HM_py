# n = int(input("Введите точность определения числа ПИ (количество знаков после запятой): "))
# k = 1
# s = 0
# for i in range (100000):
#     if i % 2 == 0 :
#         s += 4 / k
#         k += 2
#     else :
#         s -= 4 / k
#         k += 2
# print(f"%.{n}f" % s)

# num = int(input("Введите число: "))
# i = 2 # первое простое число
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")

# lst = []
# lst_2 = []

# num = int(input("Введите сколько цифр хотите внести в список: "))
# for i in range(num):
#     ind = int(input(f"Введите {i+1} число: "))
#     lst.append(ind)

# for j in lst:
#     if j not in lst_2:
#         lst_2.append(j)
# print(f"Список введённый пользователем равен: {lst}")
# print(f"Список без повторяющихся знаков равен: {lst_2}")

# from random import randint
# import itertools

# k = randint(2, 7)

# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10) 
#     return ratios

# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)

# with open('33_Polynomial.txt', 'w') as data:
#     data.write(polynom1)
