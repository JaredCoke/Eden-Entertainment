import os
from Google import  Create_Service

#FOLDER_PATH = r'D:\Python\GoogleSheets'
#CLIENT_SECRET_FILE = os.path.join(FOLDER_PATH, 'eden-sheets-and-python-a6e532bfaa17.json')
CLIENT_SECRET_FILE = 'client_file_EdenSheetsandPython_eden_jared.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

"""
Blank Spreadsheet file, Advanced Method
"""


"""
To specify Google Sheets file basic settings and as well as configure default worksheets
"""

spreadsheet = {
    'properties': {
        'title': "My First Google Sheets File Made by Python",
        "locale": "en_US",
        "autoRecalc": "HOUR",
        "timeZone": "America/New_York"
    }
}
spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                            fields='spreadsheetId').execute()
print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))

"""

"""

