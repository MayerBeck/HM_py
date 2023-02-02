# x0 = int(120)
# step = 0
# p = int(input(f'Если игру начинает PELAYER_1, то введите цифру: 1\nЕсли игру начинает PELAYER_2, то введите цифру: 2\n '))
# if p == 1:
#     print('Игру начинает PELAYER_1')
# if p == 2:
#     print('Игру начинает PELAYER_2')
# else:
#     print(f'Вы нажали {p}\nНачните сначала. Введите номер игрока 1 или 2, который делает первый ход')
#     exit()    
# while x0 > 0:
#     step = int(input(f'Введите количество конфет от 1 до 28, которое хотите забрать за один ход: - '))
#     print()    
#     if step < 1 or step > 28:
#         print(f'Вы нажали {step}, играете не по правилам\nВведите число от 1 до 28')
#         continue
#     else:
#         x0 -= step
#         if p == 1:
#             if x0 > 0: p = 2
#             print(f'PELAYER_1 забрал {step} конфет, осталось {x0} \n\nХод  PELAYER_2\n')            
#         else:
#             if x0 > 0: p = 1
#             print(f'PELAYER_2 забрал {step} конфет, осталось {x0} \n\nХод  PELAYER_1\n')               
# if p == 1:
#     print(f'Конфет не осталось - PELAYER_1 ПОБЕДИЛ!')    
# if p == 2:
#     print(f'Конфет не осталось - PELAYER_2 ПОБЕДИЛ!')
# exit()        

# from random import randint
# x0 = int(60)
# step = 0
# p = randint(1, 2)
# if p == 1:
#     print('Игру начинает ЧЕЛОВЕК')
# if p == 2:
#     print('Игру начинает КОМПЬЮТЕР')

# while x0 > 0:        
#         if p == 1 and x0 > 0:        
#             p = 2
#             step = int(input(f'Введите количество конфет от 1 до 28, которое хотите забрать за один ход: - '))
#             if step < 1 or step > 28:
#                 print(f'Вы нажали {step}, жульничаете!\nВводите числа по правилам  от 1 до 28')
#                 break
#             x0 -= step
#             print(f'ЧЕЛОВЕК забрал {step} конфет, осталось {x0} \n\nХод  КОМПЬЮТЕРА\n')            
#         else:
#             if x0 > 0: 
#                 p = 1
#                 step = randint(1, 28)
#                 x0 -= step
#                 print(f'КОМПЬЮТЕР забрал {step} конфет, осталось {x0} \n\nХод  ЧЕЛОВЕКА\n')                   
# if p == 2:
#     print(f'Конфет не осталось - ЧЕЛОВЕК ПОБЕДИЛ!')    
# if p == 1:
#     print(f'Конфет не осталось - КОМПЬЮТЕР ПОБЕДИЛ!')
# exit()    


# def matrix(mtr): # Отрисовка таблицы

#     print('\n')
#     print('\t    |    |    ')
#     print('\t  {} |  {} |  {} '.format(mtr[0], mtr[1], mtr[2]))
#     print('\t____|____|____')

#     print('\t    |    |    ')
#     print('\t  {} |  {} |  {}  '.format(mtr[3], mtr[4], mtr[5]))
#     print('\t____|____|____')

#     print('\t    |    |    ')
#     print('\t  {} |  {} |  {}  '.format(mtr[6], mtr[7], mtr[8]))
#     print('\t    |    |    ')
# print('\n')

# mtr = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Список ячеек
# step_count = 0                    # Счетчик ходов
# win_status = False                # Статус выгирыша
# win_lst = '123_456_789_147_258_369_159_357'  # Строка выигрышных комбинаций
# p = int(input(f'Если игру начинает X, то введите цифру: 1\nЕсли игру начинает O, то введите цифру: 0\n '))
# while not win_status:  # Пока никто не выграл
#     matrix(mtr)        #  Отрисовка таблицы
#     if p == 1: p = 0   #  Переход хода
#     else:
#         p = 1
#     if step_count == 9:  # Все ячейки заняты, но никто не выиграл
#         print('НИЧЬЯ')
#         break
#     step_count += 1      # Счетчик ходов + ход
#     if p == 0:
#         point = int(input(f'Ход игрока X - выбирете номер ячейки \n '))    
#         if point not in mtr:  # Если в списке нет номера ячейки - воврат к выбру
#             print(f'Место занято - выбирете свободный номер \n ') #
#             continue
#         win_lst = win_lst.replace(str(point), 'X') # Иначе заменяем в строке выигрышных комбинаций число на символ игрока      
#         for x in range(9):  # В списке ячеек меняем номер ячейки на символ игрока (выбрать его будет невозможно)
#             if mtr[x] == point: mtr[x] = 'X'
#         if 'XXX' in win_lst:  # Если в строке выигрышных комбинаций есть ХХХ, то называем победителя и прерываем выполнение программы  
#             print('ИГРОК X ВЫИГРАЛ!')
#             break

#     if p == 1:  # Те же операции для втрого игрока 
#         point = int(input(f'Ход игрока 0 - выбирете номер ячейки \n '))
#         if point not in mtr:
#             print(f'Место занято - выбирете свободный номер \n ')
#             continue
#         win_lst = win_lst.replace(str(point), '0')
#         for x in range(9): 
#             if mtr[x] == point: mtr[x] = '0'
#         if '000' in win_lst:
#             print('ИГРОК 0 ВЫИГРАЛ!')
#             break
# exit() #


# def encode(cod_str):
#     out_str = ""
#     count = 1
#     char = cod_str[0]
#     for i in range(1, len(cod_str)):  # Цикл по индексам строки
#         if cod_str[i] == char:        # Считаем к-во одинаковых символов
#             count += 1
#         else:
#             out_str += str(count) + char  # Если символ изменился, дбваляем его строковое к-во повторений
#             char = cod_str[i]
#             count = 1
#     else:    
#         out_str += str(count) + char  # Если символ не повторился, дбваляем его с 1
#     return out_str
# 	#  RLE Декодер
# def decode(out_str):  
#     str = ''
#     count = ''
#     for i in out_str:  # Для каждого элемента в строке 
#         if i.isdigit():  # Если символ число - добавляем в строку числового значения 
#             count += i              
#         else:
#             str = str + int(count)*i  # Если символ, умножаем на коэфф. приведенный к числу
#             count = '' # Облуляем строку числового коэффициента 
#     return str
# print('Чтобы выполнить кодирование нажмите клавишу c') # Выбор действия, чтение изапись файлов
# print('Чтобы выполнить кодирование нажмите клавишу d')
# state = input()
# if state == "c":
#     with open('origin_file.TXT', 'r') as f:
#         cod_str = f.read()
#     with open('coded_file.txt', 'w') as f:
#         out_str = encode(cod_str)
#         f.write(out_str)
#     print('Исходные данные:    ' + cod_str)
#     print('Сжатые данные:    ' + out_str)
# elif state == 'd':
#     with open('coded_file.txt', 'r') as f:
#         cod_str = f.read()
#     with open('decoded_file.txt', 'w') as f:
#         out_str = decode(cod_str)
#         f.write(out_str)
#     print('Сжатые данные:         ' + cod_str)
#     print('Раскодированные данные:  ' + out_str)    
# else:
#     print('Нажмите клавишу c или d')        
