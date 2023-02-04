from random import randint


def reactor(sens, level):

    n = 11
    d = 8

    # помехи
    match level:

        case 0:
            mush = [0]*(n*d)
            for i in range(n*d):
                mush[i] = float(randint(-100, 100))/100

        case 1:
            mush = [0]*(n*d)
            for i in range(n*d):
                mush[i] = float(randint(-30, +30))/100

        case 2:
            mush = [0]*(n*d)
            for i in range(n*d):
                f = randint(1, 100)
                if f % 2 == 0:
                    mush[i] = float(randint(-80, -30))/100
                elif f % 2 == 1:
                    mush[i] = float(randint(30, 80))/100

        case 3:
            mush = [0]*(n*d)
            for i in range(n*d):
                f = randint(1, 100)
                if f % 2 == 1:
                    mush[i] = float(randint(-100, -80))/100

                elif f % 2 == 0:
                    mush[i] = float(randint(80, 100))/100

        case _:
            return False

    bark_forward = [+1, +1, +1, -1, -1, -1, +1, -1, -1, +1, -1]  # локатор ФП
    bark_reverse = [-1, +1, -1, -1, +1, -1, -1, -1, +1, +1, +1]  # ФП

    # разбиваем каждый бит ФП (посылаемой в ЛЗ) на d отсчетов
    fp_d = []
    for (_, value) in enumerate(bark_reverse):
        for _ in range(d):
            fp_d.append(value)

    # разбиваем каждый бит ФП (стационарный локатор АКФ) на d отсчетов
    fp_d_locate = []
    for (_, value) in enumerate(bark_forward):
        for _ in range(d):
            fp_d_locate.append(value)

    # на каждый отсчет каждого бита воздействуется "уникальная" помеха уровнем от -1 до +1 (вероятность крайних значений крайне мала)
    for (m_index, m_value) in enumerate(mush):
        fp_d[m_index] += m_value
        fp_d[m_index] = round(fp_d[m_index], 2)

    # задаем lz (пустая) и значение АКФ (пока ноль)
    lz = []
    akf = 0
    k = 1

    for (index, value) in enumerate(fp_d):
        # вставляем по очереди биты (8 отсчетов) на 0-ую позицию, при этом остальное сдвигается вправо (как на схеме в документе)
        for x in range(d):
            lz.insert(0, fp_d[d*k - x - 1])
        k += 1

        # считаем АКФ между передачей ФП и стационарным локатором ФП
        for (index_akf, _) in enumerate(lz):
            akf += lz[index_akf] * fp_d_locate[index_akf]
        akf = akf / 8
        akf = round(akf, 2)
        # print(f'АКФ на шаге {index+1} = {akf}')

        # ищем точку всплеска АКФ
        if akf > sens:  # чувствительность ФП
            # print(f'Бит обнаружения ФП: {index+1}')
            report = index + 1
            break

        akf = 0
    return report
