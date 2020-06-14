# Указываем диапазон чисел в интервале от n1 до n2

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    import numpy as np
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!

    # Указываем диапазон чисел в интервале от n1 до n2,
    # чтобы решение было более гибкое
    n1 = 1
    n2 = 100
    random_array = np.random.randint(n1,n2+1, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return(score)


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или
       увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''

     # Указываем диапазон чисел в интервале от n1 до n2,
     # чтобы решение было более гибкое при условии, что n2>n1
    n1 = 1
    n2 = 100

    predict = (n2-n1+1) // 2 #Первое предполошаемое значение между n1 и n2
    count = 1

    while number != predict:
        count += 1
        if number > predict and predict+1 < n2:
            n1 = predict
            predict = (n2 - predict) // 2  + predict
        elif number < predict and predict > n1 and predict > 2:
            predict = predict - (predict - n1) // 2
        elif predict + 1  == n2:
            predict = n2
        else: predict = n1

    return(count) # выход из цикла, если угадали

# Проверяем
score_game(game_core_v2)
