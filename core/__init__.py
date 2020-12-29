import datetime

# A class to return system info.


class SystemInfo:
    def __init__(self):
        pass
    
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'The time now is {} {}'.format(now.hour, now.minute)
        return answer

    @staticmethod
    def get_date():
        now = datetime.datetime.now()

        answer = 'Today is {} {} of {}'.format(now.strftime('%B'), now.day, now.year)

        return answer


    @staticmethod
    def get_year():
        now = datetime.datetime.now()
        answer = 'The date is day {} month {} and year {}'.format(now.month, now.day, now.year)
        return answer


print(SystemInfo.get_date())