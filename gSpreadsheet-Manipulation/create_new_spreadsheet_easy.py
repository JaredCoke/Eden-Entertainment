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
Blank Spreadsheet file
"""
sheets_file1 = service.spreadsheets().create().execute()

"""
From Python Console: dict_keys(['spreadsheetId', 'properties', 'sheets', 'spreadsheetUrl'])
"""

print(sheets_file1)
print(sheets_file1['spreadsheetUrl'])
print(len(sheets_file1['sheets'])) # acquire how many worksheets exist in this spreadsheet
print(sheets_file1['spreadsheetId'])
print(sheets_file1['properties'])