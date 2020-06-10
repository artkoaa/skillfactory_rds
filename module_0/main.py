def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    import numpy as np
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    n1 = 1
    n2 = 100
    random_array = np.random.randint(n1,n2+1, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return(score)


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict1 = 50
    n1 = 1
    n2 = 100

    while number != predict1:
        count += 1
        if number > predict1 and predict1+1 < n2:
            n1 = predict1
            predict1 = (n2 - predict1) // 2  + predict1
        elif number < predict1 and predict1 > n1 and predict1 > 2:
            predict1 = predict1 - (predict1 - n1) // 2
        elif predict1 + 1  == n2:
            predict1 = n2
        else: predict1 = n1

    return(count) # выход из цикла, если угадали

# Проверяем
score_game(game_core_v2)
