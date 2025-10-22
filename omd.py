# Guido van Rossum <guido@python.org>

import random

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    colors = ['красный', 'синий', 'зеленый', 'желтый', 'фиолетовый']
    umbrella_color = random.choice(colors)

    print(f'\nУтка взяла {umbrella_color} зонтик и вышла на улицу.')

    events = {
        'дождь': 'зонтик защитил утку от дождя',
        'солнце': 'зонтик защитил от палящего солнца',
        'град': 'зонтик защитил от града'
    }

    possible_weather = {'дождь', 'солнце', 'град'}
    weather = 'дождь'
    print(f'На улице пошел {weather}. {events[weather].capitalize()}!')

    bar_items = ('пиво', 'чипсы', 'орешки')
    print('В баре утка заказала: ' + ', '.join(bar_items) + '.')

    has_money = True
    is_bar_open = True

    print('Утка отлично провела вечер!')


def step2_no_umbrella():
    print('\n' + 'Утка решила не брать зонтик.'.upper())

    weather = 'ливень'
    print(f'\nНа улице начался {weather}!')

    problems = ['промокла', 'испачкалась', 'простудилась']
    first_problem = problems[0].capitalize()
    other_problems = problems[1:3]

    print(f'{first_problem}. Также она {other_problems[0]} и {other_problems[1]}.')

    feelings = ['грусть', 'разочарование', 'холод']
    print('Утка чувствует: ' + ', '.join(feelings).lower() + '.')


if __name__ == '__main__':
    step1()
