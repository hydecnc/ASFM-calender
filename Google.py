from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/calendar']


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
        # page_token = None
        # while True:
        #     calendar_list = service.calendarList().list(pageToken=page_token).execute()
        #     for calendar_list_entry in calendar_list['items']:
        #         print(calendar_list_entry, calendar_list_entry['summary'])
        #     page_token = calendar_list.get('nextPageToken')
        #     if not page_token:
        #         break
        calendar = {
            'summary': 'calendarSummary',
            'timeZone': 'America/Los_Angeles'
        }

        created_calendar = service.calendars().insert(body=calendar).execute()
        event = {
            'summary': 'Test',
            'start': {
                'dateTime': '2022-08-29',
                'timeZone': 'America/Los_Angeles'
            },
            'end': {
                'dateTime': '2022-08-29',
                'timeZone': 'America/Los_Angeles'
            },
        }
        event = service.events().insert(calendarId=created_calendar['id'], body=event).execute()
        # event = service.events().insert(calendarId='primary', body=event).execute()


    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()