# def sum_odd_index(lst):
#     s = 0
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             s += lst[i]
#     print(f"Сумма равна: {s}")


# lst = [2, 3, 5, 9, 3]
# sum_odd_index(lst)
# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# sum_odd_index(lst)


# def mult_lst(lst):
#     l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
#     new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
#     print(new_lst)


# lst = [2, 3, 4, 5, 6]
# mult_lst(lst)
# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# mult_lst(lst)


# lst = list(map(float, input("Введите числа через пробел:\n").split()))
# new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
# print(max(new_lst) - min(new_lst))

# s = ""
# n = int(input(
#     "Введите число для преобразовывания десятичного числа в двоичное:\n"))
# while n != 0:
#     s = str(n % 2) + s
#     n //= 2
# print(s)


# k = int(input('Введите целое число:'))
# otr_f = []
# f = []
# result_f = []
# fib_0 = 0
# f.append(fib_0)
# fib_1 = 1
# f.append(fib_1)
# fib = 0
# for i in range(k):
#     fib = f[i] + f[i + 1]
#     f.append(fib)
#     fib *= -1
#     otr_f.append(fib)
# # print(f)
# otr_f.reverse()
# # print(otr_f)
# result_f = otr_f + f
# print(f'Для k = {k} => {result_f}')