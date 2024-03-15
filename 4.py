answer = input('Вы поедете на бал?\nОтвет: ')
if 'да' not in answer.lower() and 'нет' not in answer.lower() :
    print('Верно')
else:
    print('Неверно')