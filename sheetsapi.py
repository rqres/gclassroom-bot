from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from pprint import pprint

from googleapiclient import discovery

creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = discovery.build('sheets', 'v4', credentials=creds)

# The spreadsheet to request.
spreadsheet_id = '1jJm0z68CML8WaNEyv0TeXbplH-bFjV2tgZtv6xOkZ5w'

# The ranges to retrieve from the spreadsheet.
ranges = 'B24:X24'

request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=ranges)
response = request.execute()

code_values = response['values'][0]

print(code_values)
