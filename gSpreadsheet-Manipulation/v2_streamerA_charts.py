from Google import Create_Service

CLIENT_SECRET_FILE = 'client_file_EdenSheetsandPython_eden_jared.json' #Change me to your json key
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
spreadsheet_id = '1Wo2uJLQ6OiNXXH4yDZXDh4RsegTfbAq988x1_y3h4pk'
sheetId = '1872071561'

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
                          "endRowIndex": 32,
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
                          "endRowIndex": 32,
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
                          "endRowIndex": 32,
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
                          "endRowIndex": 32,
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
    spreadsheetId=spreadsheet_id,
    body=requests_body
).execute()








# End of Compilation
print(f'Compilation Complete; Chart(s) created successfully!')