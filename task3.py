"""
    Home Work 2
    Pavel Shvarchov - 319270583
"""

def make_mydate(day=1, month=1, year=2017):

    def generate_max_days_of_month():
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
            max_days = 31
        elif (month == 4 or month == 6 or month == 9 or month == 11):
            max_days = 30
        elif (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
            max_days = 29
        else:
            max_days = 28
        return max_days

    def possible_date(day, month, year):
        if month < 1 or 12 < month or year < 0:
            return False
        max_days = generate_max_days_of_month()
        if day < 1 or max_days < day:
            return False
        return True

    if not possible_date(day, month, year):
        return "bad date"

    def next_date():
        nonlocal day,month,year
        max_days=generate_max_days_of_month()
        if day==max_days:
            day=1
            if month==12:
                month=1
                year+=1
            else:
                month+=1
        else:
            day+=1

    def days_between_dates(d2):
        if month!=d2('get')('month') or year!=d2('get')('year'):
            return 'different months or years not allowed'
        result=day-d2('get')('day')
        if result<0: result=-result
        return result

    def set_day(value):
        nonlocal day
        max_days = generate_max_days_of_month()
        if value < 1 or max_days < value:
            return 'bad value for day'
        else:
            day = value
            return 'day changed to {}'.format(day)

    def set_month(value):
        nonlocal day, month
        if value < 1 or 12 < value:
            return 'bad value for month'
        month=value
        max_days = generate_max_days_of_month()
        addon=''
        if day > max_days:
            day = max_days
            addon='+ day was out of limit for the month, was changed to {}, ie the max day for the month'.format(day)
        return 'month changed to {} '.format(month) + addon

    def set_year(value):
        nonlocal year
        if value < 0:
            return 'bad value for year'
        year = value
        return 'year changed to {}'.format(year)

    def set(parameter, value):
        if parameter == 'day':
            return set_day(value)
        elif parameter == 'month':
            return set_month(value)
        elif parameter == 'year':
            return set_year(value)
        else:
            return "bad parameter"

    def get(parameter):
        if parameter == 'day':
            return day
        elif parameter == 'month':
            return month
        elif parameter == 'year':
            return year
        else:
            return 'bad parameter'


    def view(type='dmy'):
        if type == 'dmy':
            return "{:02d}/{:02d}/{:04d}".format(day, month, year)
        elif type == 'mdy':
            return "{:02d}/{:02d}/{:04d}".format(month, day, year)
        elif type == 'ymd':
            return "{:04d}/{:02d}/{:02d}".format(year, month, day)
        else:
            return 'format error'

    def dispatch(msg):
        if msg == 'view':
            return view
        elif msg == 'set':
            return set
        elif msg == 'get':
            return get
        elif msg=='next date':
            return next_date
        elif msg=='days between dates':
            return days_between_dates

    return dispatch


########test#######
def example():
    d1 = make_mydate()
    print(d1('view')('mdy'))
    print(d1('set')('day', 31))
    print(d1('set')('month', 12))
    print(d1('view')('ydm'))
    print(d1('view')('ymd'))
    print(d1('next date')())
    print(d1('view')('mdy'))
    d2 = make_mydate(23, 1, 2018)
    print(d2('view')())
    print(d1('days between dates')(d2))

if __name__=="__main__":
    example()
