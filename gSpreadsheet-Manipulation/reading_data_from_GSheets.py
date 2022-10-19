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
mySpreadsheets = service.spreadsheets().get(spreadsheetId=spreadsheets_id).execute()

"""
Example 1: Get method (single cell range of values)
"""

response = service.spreadsheets().values().get(
    spreadsheetId =spreadsheets_id,
    majorDimension = 'ROWS',
    range='StreamerB!A34:AG155'
).execute()

print('Printing response: ')
print(response)
print('Printing response.keys(): ')
print(response.keys())
print('Printing range: ')
print(response['range'])
print('Printing majorDimension: ')
print(response['majorDimension'])
print('Printing values: ')
print(response['values'])

columns = response['values'][0]
data = response['values'][1:]
df = pd.DataFrame(data, columns=columns)
print('Printing df:')
print(df)

df2 = df.set_index('Date')
print('Printing df2:')
print(df2)


"""
Example 2: Get Method
"""
print('')

response2 = service.spreadsheets().values().get(
    spreadsheetId =spreadsheets_id,
    majorDimension = 'ROWS',
    range='StreamerB'
).execute()

print('Printing response2: ')
print(response2)
print('Printing length of response2:')
print(len(response2))
print('Printing response2[values]: ')
print(response2['values'])
print('Printing length of response2[values]:')
print(len(response2['values']))


columns = response2['values'][33][0:] #- working!
#insert smarter way to start at the Date column marked as column 34 (zero index 33)
print('Printing columns:')
print(columns)
print('Printing length of columns:')
print(len(columns))

#data = [item[0:] for item in response2['values'][1:]]
data = response2['values'][34:]
#insert smarter way to start at the Date column marked as column 35 (zero index 34)
print('Printing data:')
print(data)
print('Printing length of data:')
print(len(data))

df3 = pd.DataFrame(data, columns=columns)
#df3 = pd.DataFrame.from_dict(data, orient='index')
#df3 = df.transpose()
print('Printing df3:')
#print(df3)
#df3 = df.set_index('Date')
#print(df3)

#adjust pandas max rows and columns displayed to comsole
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
print(df3)


"""
Example 4: BatchGet Method
"""
print('')

valueRanges_body = [
    'StreamerA', 'StreamerB', 'StreamerD'
]

response3 = service.spreadsheets().values().batchGet(
    spreadsheetId = spreadsheets_id,
    majorDimension = 'ROWS',
    ranges=valueRanges_body
).execute()

print('Printing response3: ')
print(response3)
print('Printing length of response3:')
print(len(response3))
print('Printing response3.keys:')
print(response3.keys())
print('Printing response3[valueRanges]: ')
print(response3['valueRanges'])
print('Printing length of response3[valueRanges]:')
print(len(response3['valueRanges']))

#create a dictionary dataset from all three spreadsheet data values
dataset = {}
for item in response3['valueRanges']:
    dataset[item['range']] = item['values']

print('Printing dataset: ')
print(dataset)
print('Printing length of dataset:')
print(len(dataset))
print('Printing dataset.keys:')
print(dataset.keys())

#From the entire dataset pull out the different spreadsheet values
print("Printing StreamerA dataset from entire python stored dataset dictionary")
print(dataset['StreamerA!A1:Z1000']) #for now this is hardcoded, but find a way to auto pull this range out!
print("Printing length of StreamerA dataset from entire python stored dataset dictionary")
print(len(dataset['StreamerA!A1:Z1000']))
print("Printing StreamerB dataset from entire python stored dataset dictionary")
print(dataset['StreamerB!A1:AT1009']) #for now this is hardcoded, but find a way to auto pull this range out!
print("Printing length of StreamerB dataset from entire python stored dataset dictionary")
print(len(dataset['StreamerB!A1:AT1009']))
print("Printing StreamerD dataset from entire python stored dataset dictionary")
print(dataset['StreamerD!A1:AT1009']) #for now this is hardcoded, but find a way to auto pull this range out!
print("Printing length of StreamerD dataset from entire python stored dataset dictionary")
print(len(dataset['StreamerD!A1:AT1009']))

#Remove empty leading datasets
x = []
while x in dataset['StreamerB!A1:AT1009']:
    dataset['StreamerB!A1:AT1009'].remove([])
print('Printing modified dataset[StreamerB!A1:AT1009] values')
print(dataset['StreamerB!A1:AT1009'])
print('Printing length of the modified dataset[StreamerB!A1:AT1009] values')
print(len(dataset['StreamerB!A1:AT1009']))

#Remove empty leading datasets
x = []
while x in dataset['StreamerB!A1:AT1009']:
    dataset['StreamerB!A1:AT1009'].remove([])
print('Printing modified dataset[StreamerB!A1:AT1009] values')
print(dataset['StreamerB!A1:AT1009'])
print('Printing length of the modified dataset[StreamerB!A1:AT1009] values')
print(len(dataset['StreamerB!A1:AT1009']))

#Convert tables to dataframes
# TO DO: need to implement same logic as in Example 3 here for starting and etc
df4 = {} #create a dictionary
for indx, k in enumerate(dataset): #use enumerate method to return a key from an indexed value
    columns4 = dataset[k][0]
    data4 = dataset[k][1:]
    df4[indx] = pd.DataFrame(data, columns=columns4)