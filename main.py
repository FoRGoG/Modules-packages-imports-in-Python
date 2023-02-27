from application import salary
from application.db import people
import datetime
from emoji import emojize

dt_now = datetime.datetime.now()
smile = emojize('Everything is :thumbs_up:')


if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    print('Current date and time:', dt_now)
    print(smile)

