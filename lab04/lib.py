def count_common_elements(*lists):
    if not lists:
        return 0

    # Преобразуем каждый список в множество для удаления дубликатов
    sets = [set(lst) for lst in lists]

    # Найдем пересечение всех множеств
    common_elements = sets[0]
    for s in sets[1:]:
        common_elements = common_elements.intersection(s)

    # Возвращаем количество общих элементов
    return len(common_elements)
