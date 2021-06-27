import numpy as np
number=np.random.randint(1,101) #загадали число
print("загадано число от 1 до 100")
predict=int(input("введите число")) #предполагаемое число
def Binary_Search(number): #функция бинарного поиска
    predict = list(range(1, 101)) #диапазон чисел
    first = 1 #первое
    last = 100 #последние
    index = 0
    count = 1# счетчик
    while (first <= last) and (index == 0):#условие перебора
        count += 1   #плюс попытка
        mid = (first + last) // 2 #медианное значение данного интервала
        if predict[mid] == number:
            index = mid
        else:
            if number < predict[mid]:
                last = mid - 1 #движемся левее значения
            else:
                first = mid + 1 #движемся правее значения
    return count #выход из цикла
def score_game(game_core): #Запускаем игру 1000 раз
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000)) #1000 повторений
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score) #выход из цикла
score_game(Binary_Search) #вызов функции (запуск)