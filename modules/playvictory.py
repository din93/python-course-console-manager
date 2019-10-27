import random

def play_victory():
    print('Game Victory v0.1')
    print('Ведущий: Добро пожаловать в игру! Правила таковы: я задаю вам вопросы, а вы на них отвечаете. Поехали!')
    birthdate_list = [
        ('Владимира Маяковского', '19.06.1893', 'третье июня 1893-го'),
        ('Михаила Ломоносова', '19.11.1711', 'девятнадцатое ноября 1711-го'),
        ('Уильяма Шекспира', '01.04.1564', 'первое мая 1564-го'),
        ('Сэра Йэна Маккелена', '25.05.1939', 'двадцать пятое мая 1939-го'),
        ('Илона Маска', '28.06.1971', 'двадцать восьмое июня 1971-го'),
        ('Юлии Липницкой', '05.06.1998', 'пятое июня 1998-го'),
        ('Хидео Кодзимы', '24.08.1963', 'двадцать четвертое августа 1963-го'),
        ('Сергея Есенина', '03.10.1895', 'третье октября 1895-го'),
        ('Дэниэла Рэдклиффа', '23.07.1989', 'двадцать третье июля 1989-го'),
        ('Хеди Ламарр', '09.11.1914', 'девятое ноября 1914-го')
    ]
    selection_size = 5

    wanna_play = 'да'
    while wanna_play.lower() == 'да':
        birthdate_list_selection = random.sample(birthdate_list, selection_size)
        mistakes_count = 0
        for name, birthdate_nums, birthdate_words in birthdate_list_selection:
            answer = input(f'Ведущий: Напишите дату рождения {name} в формате "dd.mm.yyyy"\nВы: ')
            if answer != birthdate_nums:
                print(f'Неверно, дата рождения {name} - {birthdate_words}!')
                mistakes_count += 1
            else:
                print(f'Верно! {birthdate_words.capitalize()}.')
        print(f'Ведущий: Итак, правильных ответов - {selection_size - mistakes_count}, неправильных - {mistakes_count}')
        wanna_play = input("Ведущий: Начнем сначала? (да или нет)\nВы: ")
        if wanna_play != 'да':
            print('Ведущий: Тогда до свидания!')