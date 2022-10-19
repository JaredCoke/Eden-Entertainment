from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from google.oauth2 import service_account

#import service as service
from Google import Create_Service
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#from pprint import pprint
from googleapiclient import discovery


#from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#sa = gspread.service_account(filename="eden-sheets-and-python-a6e532bfaa17.json")
#sh = sa.open("test")

#code from oauth service account
SERVICE_ACCOUNT_FILE = 'eden-sheets-and-python-a6e532bfaa17.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] #change access to scopes to be sheets
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#end of code from oauth

scope = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('eden-sheets-and-python-a6e532bfaa17.json',scope)
client = gspread.authorize(creds)

spreadsheet_id = '1Wo2uJLQ6OiNXXH4yDZXDh4RsegTfbAq988x1_y3h4pk'
sheetId = '1872071561'

python_test = client.open("test").worksheet("StreamerA")

#service2 = discovery.build('test', sheetId, credentials=creds)


#wks = sh.worksheet("testSheet")
#print('Rows: ',wks.row_count)
#print('Columns: ',wks.col_count)

#wks.update('A1','Eden test')
#wks.add_cols(2)
#The following codes affects sheet2: StreamerA
#StreamerA = sh.worksheet("StreamerA")
service = Create_Service('eden-sheets-and-python-a6e532bfaa17.json', #CLIENT_SECRET_FILE
                         'sheets', #API_NAME
                         'v4', #API_VERSION
                         scope) #SCOPES



#StreamerA.add_cols(1) #add columns

#Graph Average Viewers



#Here's the sample/defualt code
requests_body = {
  "requests": [
    {
      "addChart": {
        "chart": {
          "spec": {
            "title": "Model Q1 Sales",
            "basicChart": {
              "chartType": "COLUMN",
              "legendPosition": "BOTTOM_LEGEND",
              "axis": [
                {
                  "position": "BOTTOM_AXIS",
                  "title": "Model Numbers"
                },
                {
                  "position": "LEFT_AXIS",
                  "title": "Sales"
                }
              ],
              "domains": [
                {
                  "domain": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": sheetId,
                          "startRowIndex": 0,
                          "endRowIndex": 7,
                          "startColumnIndex": 0,
                          "endColumnIndex": 1
                        }
                      ]
                    }
                  }
                }
              ],
              "series": [
                {
                  "series": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": sheetId,
                          "startRowIndex": 0,
                          "endRowIndex": 7,
                          "startColumnIndex": 1,
                          "endColumnIndex": 2
                        }
                      ]
                    }
                  },
                  "targetAxis": "LEFT_AXIS"
                },
                {
                  "series": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": sheetId,
                          "startRowIndex": 0,
                          "endRowIndex": 7,
                          "startColumnIndex": 2,
                          "endColumnIndex": 3
                        }
                      ]
                    }
                  },
                  "targetAxis": "LEFT_AXIS"
                },
                {
                  "series": {
                    "sourceRange": {
                      "sources": [
                        {
                          "sheetId": sheetId,
                          "startRowIndex": 0,
                          "endRowIndex": 7,
                          "startColumnIndex": 3,
                          "endColumnIndex": 4
                        }
                      ]
                    }
                  },
                  "targetAxis": "LEFT_AXIS"
                }
              ],
              "headerCount": 1
            }
          },
          "position": {
            "newSheet": True
          }
        }
      }
    }
  ]
}

response = service.spreadsheets().batchUpdate(
    spreadsheetId=python_test,
    body=requests_body
).execute()

#response = request.execute()






# End of Compilation
print(f'Compilation Complete')