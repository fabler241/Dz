one_day = 86400     # один день
one_hour = 3600     # один час
one_minute = 60     # одна минута
duration = int (input('Укажите продолжительность в секундах: '))
if duration<one_minute:
    print ('{} сек'.format(duration))
elif one_minute <= duration and one_hour > duration:
    my_minute=duration//one_minute
    my_second=duration%one_minute
    print ('{} мин {} сек'.format(my_minute,my_second));
elif duration >= one_hour and duration < one_day:
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} час {} мин {} сек'.format(my_hour, my_minute, my_second));