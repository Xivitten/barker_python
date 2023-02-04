import numpy as np
import matplotlib.pyplot as plt


def stat(fp, sens, fp_stat, fp_count_miss, fp_prob, i, kol, level):
    for (index_stat, value_stat) in enumerate(fp):
        fp_stat[index_stat] += value_stat       # для усредненного графика

        if value_stat != 11:
            # для вероятности ошибки на sens
            fp_count_miss[index_stat] += 1

    # подсчет вероятностей и средних точек, построение графиков
    if i == kol - 1:
        for (index_prob, value_prob) in enumerate(fp_count_miss):
            fp_prob[index_prob] = (value_prob / kol) * 100
            fp_stat[index_prob] = fp_stat[index_prob] / kol

        print(f'\nsensiv  = {sens}')
        print(f'fp_prob = {fp_prob}')
        print(f'fp_stat = {fp_stat}\n')

        fig1 = plt.figure(dpi=250, figsize=(6.5, 6.5))
        ax1 = fig1.add_subplot()
        ax1.plot(sens, fp_stat, "o-g", linewidth=0.7, markersize='3')
        # настроим наш график
        ax1.set_ylim(0, 12)
        ax1.set_title(f'Средняя принятая ФП из {i+1} значений', fontsize=14)
        ax1.set_xlabel(f'Чувствительность фильтра')
        ax1.set_ylabel(f'Номер бита обнаружения ФП')
        ax1.set_xticks(np.arange(0, sens[0]+sens[0]-sens[1], sens[0]-sens[1]))
        ax1.set_yticks(np.arange(0, 12, 1))
        ax1.minorticks_on()
        ax1.grid(which='major', linestyle='-')
        ax1.grid(which='minor', linestyle=':')
        # сохраним график
        fig1.savefig(f'Средняя точка ФП - {level} ур.png')

        fig2 = plt.figure(dpi=250, figsize=(6.5, 6.5))
        ax2 = fig2.add_subplot()
        ax2.plot(sens, fp_prob, "o-r", linewidth=0.7, markersize='3')
        # настроим наш график
        ax2.set_ylim(0, 12)
        ax2.set_title(f'Вероятность ошибки из {i+1} значений', fontsize=14)
        ax2.set_xlabel(f'Чувствительность фильтра')
        ax2.set_ylabel(f'Вероятность ошибки в %')
        ax2.set_xticks(np.arange(0, sens[0]+sens[0]-sens[1], sens[0]-sens[1]))
        ax2.set_yticks(np.arange(0, 104, 5))
        ax2.minorticks_on()
        ax2.grid(which='major', linestyle='-')
        ax2.grid(which='minor', linestyle=':')
        # сохраним график
        fig2.savefig(f'Вероятность ошибки - {level} ур.png')

    return True
