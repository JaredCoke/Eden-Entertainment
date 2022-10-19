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

#spreadsheet_id = '1Wo2uJLQ6OiNXXH4yDZXDh4RsegTfbAq988x1_y3h4pk' THIS IS THE SHARED CLOUD FILE
#sheet_id = '1872071561' THIS IS THE SHARED CLOUD FILE
spreadsheet_id = '1_NRWd_Fm9MpJl2ZFcNobUNE-TnN-tEp7k9QLscjF_FM'
sheet_id = '1433888156' #gid value of worksheet w/in spreadsheet

"""
Example 1: Create a Single Bar Chart
"""

requests_body = {
    'requests': [
        {
            'addChart': {
                'chart': {
                    'spec': {
                        'title': 'StreamerB Analytics',
                        'basicChart': { #here's where you define bar, line, pie, etc chart type
                            'chartType': 'COLUMN',
                            'legendPosition': 'BOTTOM_LEGEND',
                            'axis': [
                                #X-Axis
                                {
                                    'position': "BOTTOM_AXIS",
                                    'title': 'Analytics'
                                },
                                #Y-Axis
                                {
                                    'position': "LEFT_AXIS",
                                    'title': 'Metrics'
                                }
                            ],
                            #Chart Labels
                            'domains': [ #create a dictionary of data
                                {
                                    'domain': {
                                        'sourceRange': { #create another dictionary
                                            'sources': [ #create a list
                                                {
                                                    'sheetId': sheet_id,
                                                    'startRowIndex': 37,
                                                    'endRowIndex': 61,
                                                    'startColumnIndex': 0, #was 1
                                                    'endColumnIndex': 1 #was 2
                                                }
                                            ]
                                        }
                                    }

                                }
                            ],
                            #Source Chart Data
                            'series': [
                                {
                                    'series': { #create a dictionary of data
                                        'sourceRange': {
                                            'sources': [ #create a list
                                                {
                                                    'sheetId': sheet_id,
                                                    'startRowIndex': 37, # Row 38 #was 36
                                                    'endRowIndex': 61, # Row 66 #was 61
                                                    'startColumnIndex': 3, # Column 4
                                                    'endColumnIndex': 4 #Column 5; doesn't show data in this column
                                                }
                                            ]
                                        }
                                    },
                                    'targetAxis': 'LEFT_AXIS'
                                }
                            ]
                        }
                    },
                    'position': {
                        "newSheet": True
                    #    "overlayPosition": {
                    #      "sheetId": sheet_id,
                    #      "rowIndex": 34,
                    #      "columnIndex": 34
                    #    }
                    }
                }
            }
        }
    ]
}

response = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body=requests_body
).execute()

print('chart added to sheet')