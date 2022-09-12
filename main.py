from datetime import date, datetime, timedelta


class DateManager():
    def __init__(self, start_date, end_date, classes):
        self.classes = classes
        self.start_date = start_date
        self.end_date = end_date
        self.odd_or_even = 1

        self.weekday_schedule = {
            1: {
                'start': {
                    'dateTime': '2022-08-29T08:30:00-05:00',
                    'timeZone': 'America/Mexico_City',
                },
                'end': {
                    'dateTime': '2022-08-29T09:45:00-05:00',
                    'timeZone': 'America/Mexico_City',
                },
            },
            2: {
                'start': {
                    'dateTime': '2022-08-29T10:25:00-05:00',
                    'timeZone': 'America/Mexico_City',
                },
                'end': {
                    'dateTime': '2022-08-29T11:40:00-05:00',
                    'timeZone': 'America/Mexico_City',
                },
            },
            3: {
                'start': {
                    'dateTime': '2022-08-29T11:45:00-05:00',
                    'timeZone': 'America/Mexico_City',
                },
                'end': {
                    'dateTime': '2022-08-29T13:00:00-05:00',
                    'timeZone': 'America/Mexico_City',
                },
            },
            4: {
                'start': {
                    'dateTime': '2022-08-29T13:35:00-05:00',
                    'timeZone': 'America/Mexico_City',
                },
                'end': {
                    'dateTime': '2022-08-29T14:50:00-05:00',
                    'timeZone': 'America/Mexico_City',
                },
            },
        }
        self.friday_odd_schedule = {
            1: {
                'start': {
                    'dateTime': '2022-08-29T08:30:00-05:00',
                    'timeZone': 'America/Mexico_City',
                },
                'end': {
                    'dateTime': '2022-08-29T09:50:00-05:00',
                    'timeZone': 'America/Mexico_City',
                },
            },
            2: {
                'start': {
                    'dateTime': '2022-08-29T09:55:00-05:00',
                    'timeZone': 'America/Mexico_City',
                },
                'end': {
                    'dateTime': '2022-08-29T11:15:00-05:00',
                    'timeZone': 'America/Mexico_City',
                },
            },
            3: {
                'start': {
                    'dateTime': '2022-08-29T11:35:00-05:00',
                    'timeZone': 'America/Mexico_City',
                },
                'end': {
                    'dateTime': '2022-08-29T12:55:00-05:00',
                    'timeZone': 'America/Mexico_City',
                },
            },
            4: {
                'start': {
                    'dateTime': '2022-08-29T13:20:00-05:00',
                    'timeZone': 'America/Mexico_City',
                },
                'end': {
                    'dateTime': '2022-08-29T14:40:00-05:00',
                    'timeZone': 'America/Mexico_City',
                },
            },
        }

    def get_day_schedule(self, day, is_friday):
        if is_friday:
            if odd_or_even:
                self.friday_odd_schedule
            else:
        else:
            if odd_or_even:

            else:


        return

    def daterange(self, start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)




odd_schedule = {

}

with open("no_schools.txt", 'r') as no_school_file:
    no_schools = set(no_school_file.read())

# Generate set of all the days without school
# no_schools = {date(2022, 9, 16)}.union(set(daterange(date(2022, 11, 21), date(2022, 11, 26)))).union(set(daterange(date(2022, 12, 22), date(2023, 1, 7)))).union({date(2023, 2, 6), date(2022, 3, 20)}).union(daterange(date(2023, 4, 3), date(2023, 4, 15))).union({date(2023, 5, 1), date(2023, 5, 5)})

for single_date in daterange(start_date, end_date):
    if (single_date in no_schools) or single_date.strftime("%a") == 'Sun' or single_date.strftime("%a") == 'Sat':
        continue


    odd_or_even = not odd_or_even
    # if single_date.strftime("%a") == 'Fri':
    #     print((single_date.strftime("FRIDAY %Y-%m-%d, %a")))
    # else:
    #     print((single_date.strftime("WEEKDAY %Y-%m-%d, %a")))
    print(single_date.strftime())

