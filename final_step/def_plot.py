import numpy as np
import matplotlib.pyplot as plt


def to_plot(x, y, i):

    fig = plt.figure(dpi=250, figsize=(6.5, 6.5))
    ax = fig.add_subplot()
    ax.plot(x, y, "o-g", linewidth=0.7,  markersize='3')
    # настроим наш график
    ax.set_ylim(0, 12)
    ax.set_title(f'Шаг {i+1}', fontsize=14)
    ax.set_xlabel(f'Чувствительность фильтра')
    ax.set_ylabel(f'Номер бита обнаружения ФП')
    ax.set_xticks(np.arange(0, x[0]+x[0]-x[1], x[0]-x[1]))
    ax.set_yticks(np.arange(0, 12, 1))
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-')
    ax.grid(which='minor', linestyle=':')
    # сохраним график
    fig.savefig(f'figure №{i+1}.png')

    return True
