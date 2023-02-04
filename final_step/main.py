import def_locate
import def_plot
import def_stat
import time


# ВВОД ДАННЫХ ТОЛЬКО ДЛЯ ПОЛЬЗОВАТЕЛЯ
####################################
sens_from_user = int(input(f'Введите чувствительность датчика: >> '))
step_from_user = float(input(f'Введите шаг снижения чувствительности: >> '))
# уровень помех
print(f'Введите уровень помех, где уровни: \n 3: (-1...-0.8; +0.8...+1) \n 2: (-0.8...-0.3;+ 0.3...0.8) \n 1: (-0.3...+0.3) \n 0: (-1...+1)')
level = int(input(f'>> '))
# 0 - стандартный, 1 - низкий, 2 - средний, 3 - высокий уровень помех
####################################

times = int(sens_from_user / step_from_user + 1)
fp_stat = [0]*times
fp_count_miss = [0]*times
fp_prob = [0]*times

# количество итераций и графиков
kol = int(input(f'Введите количество итераций пуска ФП: >> '))
start = time.time()
for i in range(kol):
    sens = []               # для построения графика и анализа
    fp = []                 # для построения графика и анализа

    sens_inputed = sens_from_user
    # определяем чувствительность и бит нахождения ФП
    for _ in range(times):
        fp_report = def_locate.reactor(sens_inputed, level)

        # заносим данные в списки для будущего plot-инга
        sens.append(sens_inputed)
        fp.append(fp_report)

        sens_inputed -= step_from_user

    # вызов функции постройки графика для итерации
    if i == 0 or i == kol / 2 or i == kol - 1:
        graph = def_plot.to_plot(sens, fp, i)

    # вызов функции вычисления вероятности ошибки + общего графика
    main_fig = def_stat.stat(
        fp, sens, fp_stat, fp_count_miss, fp_prob, i, kol, level)


end = time.time() - start
print(f'Готово! Программа сформировала 5 графиков со статистикой эксперимента, проверьте папку с исполняемым файлом.')
print(f'Время работы программы: {round(end,3)} секунд')
input(f'Нажмите любую кнопку для выхода')
