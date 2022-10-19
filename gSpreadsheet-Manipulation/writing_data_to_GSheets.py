import os
from Google import  Create_Service

#FOLDER_PATH = r'D:\Python\GoogleSheets'
#CLIENT_SECRET_FILE = os.path.join(FOLDER_PATH, 'eden-sheets-and-python-a6e532bfaa17.json')
CLIENT_SECRET_FILE = 'client_file_EdenSheetsandPython_eden_jared.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

spreadsheets_id = '1_NRWd_Fm9MpJl2ZFcNobUNE-TnN-tEp7k9QLscjF_FM'
mySpreadsheets = service.spreadsheets().get(spreadsheetId=spreadsheets_id).execute()

"""
Use the 'Update' method
"""
worksheet_name = 'StreamerA!'
cell_range_insert = 'B2'

values = [
    ('Col A','Col B','Col C'),
    ('Average Viewers', 'Unique Viewers', 'Average Comments')
]
value_range_body = {
    "majorDimension": "COLUMNS",
    "values": values
}

service.spreadsheets().values().update(
    spreadsheetId=spreadsheets_id,
    valueInputOption='USER_ENTERED',
    range=worksheet_name + cell_range_insert,
    body=value_range_body
).execute()

#clear the worksheet from data
#service.spreadsheets().values().clear(
#    spreadsheetId=spreadsheets_id,
#    range='StreamerA'#you can define either a specific area or entire worksheet here
#).execute()


"""
Use the 'Append' method
"""
worksheet_name = 'StreamerA!'
cell_range_insert = 'B2'

values = [
    ('Col D','Col E','Col F'),
    ('Average Max Views', 'Moar Unique Viewers', 'Moar Average Comments')
]
value_range_body = {
    "majorDimension": "COLUMNS",
    "values": values
}

service.spreadsheets().values().append(
    spreadsheetId=spreadsheets_id,
    valueInputOption='USER_ENTERED',
    range=worksheet_name + cell_range_insert,
    body=value_range_body
).execute()

#clear the worksheet from data
#service.spreadsheets().values().clear(
#    spreadsheetId=spreadsheets_id,
#    range='StreamerA'#you can define either a specific area or entire worksheet here
#).execute()

