breed = input('Собака короткошерстной породы? ')
height = input('Рост собаки менее 50 см? ')
if breed.lower() == 'да' and height.lower() == 'да':
    tail = input('У собаки короткий хвост? ')
    if tail.lower() == 'да':
        print('английский бульдог')
    else:
        ears = input('У собаки длинные уши? ')
        if ears.lower() == 'да':
            print('гончая')
        else:
            body = input('У собаки короткое тело? ')
            if body.lower() == 'да':
                print('мопс')
            else:
                print('чихуахуа')
elif breed.lower() == 'да' and height.lower() == 'нет':
    weight = input('Собака весит более 50 кг? ')
    if weight.lower() == 'да':
        print('датский дог')
    else:
        print('фоксхаунд')
elif breed.lower() == 'нет' and height.lower() == 'да':
    personality = input('У собаки доброжелательный характер? ')
    if personality.lower() == 'да':
        print('кокер-спаниэль')
    else:
        print('ирландский сеттер')
else:
    height_2 = input('У собаки рост менее 70 см? ')
    if height_2.lower() == 'да':
        ears_2 = input('У собаки длинные уши? ')
        if ears_2.lower() == 'да':
            print('большой вандейский грифон')
        else:
            print('колли')
    else:
        color = input('Окрас рыжий с белыми отметинами? ')
        if color.lower() == 'да':
            print('сенбернар')
        else:
            color_2 = input('Белоснежный окрас? ')
            if color_2.lower() == 'да':
                print('ирландский волкодав')
            else:
                print('ньюфаундленд')