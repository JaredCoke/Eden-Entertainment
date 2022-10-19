import os
from Google import  Create_Service
import pandas as pd
from pprint import pprint

#FOLDER_PATH = r'D:\Python\GoogleSheets'
#CLIENT_SECRET_FILE = os.path.join(FOLDER_PATH, 'eden-sheets-and-python-a6e532bfaa17.json')
CLIENT_SECRET_FILE = 'client_file_EdenSheetsandPython_eden_jared.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

spreadsheets_id = '1_NRWd_Fm9MpJl2ZFcNobUNE-TnN-tEp7k9QLscjF_FM'
sheet_id = '1135960674' #gid value of worksheet w/in spreadsheet

"""
Example 1: Format the Data
"""

request_body = {
    'requests': [
        {
            'repeatCell': {
                'range': {
                    'sheetId': sheet_id,
                    'startRowIndex': 1,
                    'endRowIndex': 6, #rows 2-7
                    'startColumnIndex': 1,
                    'endRowIndex': 3
                },
                'cell': {
                    'userEnteredFormat': {
                        'numberFormat': {
                            'type': 'CURRENCY',
                            'pattern': '$#,##0',
                        },
                        'backgroundColor': {
                            'red': 25,
                            'green': 40,
                            'blue': 15
                        },
                        'textFormat': {
                            'fontSize': 14,
                            'bold': True
                        }
                    }
                },
                'fields': 'userEnteredFormat(numberFormat,backgroundColor,textFormat)'
            }
        }
    ]
}

response = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheets_id,
    body=request_body
).execute()
