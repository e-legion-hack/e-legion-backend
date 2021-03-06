from enum import Enum


class City(Enum):
    moscow = 'Moсква'
    spb = 'Санкт-Петербург'
    kazan = 'Казань'
    ufa = 'Уфа'
    kalinin = 'Калининград'


class Department(Enum):
    android = 'Андройд разработка'
    ios = 'iOS разработка'
    frontend = 'Frontend разработка'
    backend = 'Backend разработка'
    manager = 'Управление'
    analytics = 'Аналитика'
    design = 'Дизайн'
    marketing = 'Маркетинг'
    test = 'Тестирование'
    back = 'Бэкофис'
    hr = 'HR'


class EmployeeStatus(Enum):
    working = 'работает'
    on_vacation = 'в отпуске'
    on_sick = 'на больничном'
    on_time_off = 'в отгуле'


class RomeStatus(Enum):
    tubicen = 'Тубицен'  # стажер
    evocatus = 'Эвокат'  # junior
    duplicarius = 'Дупликарий'  # middle
    praefectus_castrorum = 'Префект лагеря'  # руководитель группы
    laticlavius = 'Латиклавий'  # руководитель проектов
    legatus = 'Легат'  # CEO


class TaskStatus(Enum):
    created = 'создана'
    in_progress = 'в исполнении'
    canceled = 'отменена'
    executed = 'выполнена'


class ActivityType(Enum):
    lunch = 'обед'
    sport = 'спорт'
    party = 'вечеринка'
    board_games = 'настольные игры'
    nature = 'природа'
