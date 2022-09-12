from __future__ import print_function

import datetime
import os.path
from datetime import date, timedelta

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/calendar']


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        calendar = {
            'summary': input("Type in Calendar Name: "),
            'timeZone': 'America/Mexico_City'
        }

        created_calendar = service.calendars().insert(body=calendar).execute()
        print(created_calendar['id'])

        classes = []
        for i in range(1, 9):
            classes.append(input(f"P{i}"))

        start_date = date(2022, 8, 29)
        end_date = date(2023, 6, 22)

        odd_or_even = 1

        no_schools = {date(2022, 9, 5), date(2022, 9, 16)}.union(set(daterange(date(2022, 11, 21), date(2022, 11, 26)))).union(set(daterange(date(2022, 12, 22), date(2023, 1, 7)))).union({date(2023, 2, 6), date(2022, 3, 20)}).union(daterange(date(2023, 4, 3), date(2023, 4, 15))).union({date(2023, 5, 1), date(2023, 5, 5)})

        for single_date in daterange(start_date, end_date):
            # Skip the for loop if there's no school
            if (single_date in no_schools) or single_date.strftime("%a") == 'Sun' or single_date.strftime(
                    "%a") == 'Sat':
                continue




            # Create Weekday/Friday schedule
            weekday_schedule = {
                1: {
                    'start': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T08:30:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                    'end': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T09:45:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                },
                2: {
                    'start': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T10:25:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                    'end': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T11:40:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                },
                3: {
                    'start': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T11:45:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                    'end': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T13:00:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                },
                4: {
                    'start': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T13:35:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                    'end': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T14:50:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                },
            }
            friday_schedule = {
                1: {
                    'start': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T08:30:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                    'end': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T09:50:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                },
                2: {
                    'start': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T09:55:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                    'end': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T11:15:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                },
                3: {
                    'start': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T11:35:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                    'end': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T12:55:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                },
                4: {
                    'start': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T13:20:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                    'end': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T14:40:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                },
            }
            if single_date.strftime("%a") == 'Fri':
                if odd_or_even:
                    period_counter = 1
                    for period in friday_schedule.values():
                        event = period
                        event["summary"] = classes[period_counter - 1]
                        print("Odd Friday Success")
                        event = service.events().insert(calendarId=created_calendar['id'],
                                                        body=period).execute()
                        period_counter += 2
                else:
                    period_counter = 2
                    for period in friday_schedule.values():
                        event = period
                        event["summary"] = classes[period_counter - 1]
                        print("Even Friday Success")
                        event = service.events().insert(calendarId=created_calendar['id'],
                                                        body=period).execute()
                        period_counter += 2
                lunch = {
                    'start': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T13:00:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                    'end': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T13:30:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                }
                event = service.events().insert(calendarId=created_calendar['id'], body=lunch).execute
            else:
                if odd_or_even:
                    period_counter = 1
                    for period in weekday_schedule.values():
                        event = period
                        event["summary"] = classes[period_counter - 1]
                        print("Odd Weekday Success")
                        event = service.events().insert(calendarId=created_calendar['id'],
                                                        body=period).execute()
                        period_counter += 2
                else:
                    period_counter = 2
                    for period in weekday_schedule.values():
                        event = period
                        event["summary"] = classes[period_counter - 1]
                        print("Even Weekday Success")
                        event = service.events().insert(calendarId=created_calendar['id'], body=period).execute()
                        period_counter += 2
                MAAPS = {
                    'summary': 'MAAPS',
                    'start': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T09:50:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                    'end': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T10:15:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                }
                event = service.events().insert(calendarId=created_calendar['id'], body=MAAPS).execute()
                print("MAAPS Successful")
                lunch = {
                    'summary': 'Lunch',
                    'start': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T13:00:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                    'end': {
                        'dateTime': f'{single_date.strftime("%Y-%m-%d")}T13:30:00-05:00',
                        'timeZone': 'America/Mexico_City',
                    },
                }
                event = service.events().insert(calendarId=created_calendar['id'], body=lunch).execute()
                print("Lunch Successful")

            odd_or_even = not odd_or_even

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()