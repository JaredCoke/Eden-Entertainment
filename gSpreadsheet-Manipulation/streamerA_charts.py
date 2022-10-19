import gspread
sa = gspread.service_account(filename="eden-sheets-and-python-a6e532bfaa17.json")
sh = sa.open("test")

wks = sh.worksheet("testSheet")
#print('Rows: ',wks.row_count)
#print('Columns: ',wks.col_count)

wks.update('A1','Eden test')
wks.add_cols(2)
#The following codes affects sheet2: StreamerA
StreamerA = sh.worksheet("StreamerA")
sheetId = StreamerA
#StreamerA.add_cols(1) #add columns

#Graph Average Viewers



#Here's the sample/defualt code

requests_body = {
    'requests': [
        {
            'addChart':{
                'chart':{
                    'spec':{
                        'title': 'Streamer A Average Viewers'
                        'basicChart': {
                            'chartType':'COLUMN',
                            'legendPosition': 'BOTTOM_LEGEND',
                            'axis': [
                                # X-Axis
                                {
                                    'position': 'BOTTOM_AXIS',
                                    'title':"Average Viewers"
                                }
                                # Y-Axis
                                {
                                    'position': 'LEFT_AXIS',
                                    'title':"Total"
                                }
                            ]
                            'series': [
                                {
                                    'series': {
                                        'sourceRange': {
                                            'sources': [
                                                {
                                                    'sheetId': sheetId,
                                                    'startRowIndex': 27,
                                                    'endRowIndex': 55,
                                                    'startColumn': 3, #Column D
                                                    'endColumn': 3
                                                }
                                            ]
                                        }
                                    },
                                        'targetaxis': 'LEFT_AXIS'
                                }
                            ]
}
                    }
                }
            }
        }
    ]
}

response = service.spreadsheets().batchUpdate()








# End of Compilation
print(f'Compilation Complete')