name = input('Здравствуйте! Как Вас зовут? ')
print('Очень приятно, ', name, '! ', 'Меня зовут Марк.', sep='')
age = int(input('Сколько Вам лет? '))
if age > 78:
    print('Да, ', name, ', Вы старше меня на ', age - 78, ' лет.', sep='')
elif age < 78:
    print('Да, ', name, ', я старше Вас на ', 78 - age, ' лет.', sep='')
else:
    print('Да, ', name, ', Вам столько же лет, сколько и мне. ', sep='')
program = input('Вам нравится программировать? ')
if program.lower() == 'да':
    print('Превосходно! Уверен, у Вас получится написать множество '
          'полезных и хороших программ.')
else:
    print('Жаль. Я думал, Вы сможете написать интересную программу для меня.')