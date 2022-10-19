import gspread
import pprint
import re
import pandas as pd
import numpy as np
import tweepy
from oauthlib.oauth1.rfc5849.endpoints import access_token

sa = gspread.service_account(filename="eden-sheets-and-python-a6e532bfaa17.json")
sh = sa.open("test")

#wks = sh.worksheet("testSheet")
#print('Rows: ',wks.row_count)
#print('Columns: ',wks.col_count)

#wks.update('A1','Eden test')
#wks.add_cols(2)
#The following codes affects sheet2: StreamerA
StreamerA = sh.worksheet("StreamerA")
#StreamerA.add_cols(1) #add columns

#Graph Average Viewers
worksheet_list = sh.worksheets()
print(worksheet_list)

worksheet = sh.worksheet('StreamerA')
val = worksheet.acell('D34').value
print(val)

# Acquire all values for the month here
get_Section = worksheet.get_values('D38:D67')
get_Minutes_Streamed = worksheet.get_values('N38:N67')
print(get_Section)

# Acquire all values from the date column
values_list = worksheet.col_values(1)

#Explicit Find/Search
cell = worksheet.find("Fri Dec 31 2021")
print("Found something at R%sC%s" % (cell.row, cell.col))
values_list_search = worksheet.find("Fri Dec 31 2021")
print("Found something at R%sC%s" % (values_list_search.row, values_list_search.col))

#RegEx Find/Search
#cell_re = re.findall("Fri Dec 31 2021",worksheet)
#print(cell_re)
#cell = worksheet.find('Fri Dec 31 2021')
#print(cell)
#print("Found something at R%sC%s" % (cell.row, cell.col))

# List Out the totals and averages here
## Count all values that are greater than 0 here; this lists the # of days that were streamed
#float(get_Section)
count_get_Average_Views = len(get_Section)
print(count_get_Average_Views)

#convert all strings in the list to floats
float_lst = list(np.float_(get_Section))
print(float_lst)
# Count all nonzero floats
non_zero_elements = np.count_nonzero(float_lst)
print(non_zero_elements)

#Print how many times this streamer has streamed this month
print('This streamer has streamed '+str(non_zero_elements)+' times this month')

#Write how many times this streamer has streamed this month to worksheet
worksheet.update('AK67', non_zero_elements)

"""
Average the Average Views this month
"""
#define the list set and other variables
get_Average_Views = worksheet.get_values('D38:D67')
float_get_Average_Views = list(np.float_(get_Average_Views))

count_non0_get_Average_Views = np.count_nonzero(float_get_Average_Views)

#determine which values in the list are non-zeroes

#average these non-zeroes values together
length_get_Average_Views = len(float_get_Average_Views)
print(count_non0_get_Average_Views)
sum_get_Average_Views = sum(float_get_Average_Views)
print(sum_get_Average_Views)

average_float_Views = sum_get_Average_Views / count_non0_get_Average_Views
print(average_float_Views)

#OR define this as a function
def Average(float_get_Average_Views):
    return sum(float_get_Average_Views) / count_non0_get_Average_Views #len(float_get_Average_Views)

final_average_Views = Average(float_get_Average_Views)

print("The average views for StreamerA this month are "+str(final_average_Views))
#write the averaged answer to the spreadsheet at the specified location

#get max Average Views from all streams
max_Average_Views = max(float_get_Average_Views)
print("The max average views this month from StreamerA are "+str(max_Average_Views))



"""
Average the Amount of Chat Messages Received per Stream this month
"""
#define the list set and other variables
get_Chat_Messages = worksheet.get_values('E38:E67')
float_get_Chat_Messages = list(np.float_(get_Chat_Messages))

#determine which values in the list are non-zeroes
count_non0_get_Chat_Messages = np.count_nonzero(float_get_Chat_Messages)

def chat_Average(float_get_Average_Views):
    return sum(float_get_Chat_Messages) / count_non0_get_Chat_Messages

average_Chats = chat_Average(float_get_Average_Views)
print("The average chats for StreamerA this month are "+str(average_Chats))

#get max messages sent from all streams
max_chats = max(float_get_Chat_Messages)
print("The max chat messages this month from StreamerA are "+str(max_chats))



"""
Find the Max Views from a stream this month
"""
#define the list set and other variables
get_Max_Views = worksheet.get_values('L38:L67')
float_get_Max_Views = list(np.float_(get_Max_Views))

#determine which values in the list are non-zeroes
count_non0_get_Max_Views = np.count_nonzero(float_get_Max_Views)

#determine the highest values in the list
max_views = max(float_get_Max_Views)

def max_Average(float_get_Max_Views):
    return sum(float_get_Max_Views) / count_non0_get_Max_Views

average_max = max_Average(float_get_Max_Views)

print("The max viewers from a stream for StreamerA this month are "+str(max_views))
print("The average max viewers for StreamerA this month are "+str(average_max))


"""
Average Live Views this month
"""
#define the list set and other variables
get_Live_Views = worksheet.get_values('K38:K67')
float_get_Live_Views = list(np.float_(get_Live_Views))

#determine which values in the list are non-zeroes
count_non0_get_Live_Messages = np.count_nonzero(float_get_Live_Views)

def live_Averages(float_get_Live_Messages):
    return sum(float_get_Live_Messages) / count_non0_get_Live_Messages

average_Live_Views = live_Averages(float_get_Live_Views)
print("The average live views for StreamerA this month are "+str(average_Live_Views))

#get max live views
max_live_views = max(float_get_Live_Views)
print("The max Live Views this month from StreamerA are "+str(max_live_views))


"""
Average Unique Views this month
"""
#define the list set and other variables
get_Unique_Views = worksheet.get_values('O38:O67')
float_get_Unique_Views = list(np.float_(get_Unique_Views))

#determine which values in the list are non-zeroes
count_non0_get_Unique_Views = np.count_nonzero(float_get_Unique_Views)

def unique_Averages(float_get_Unique_Views):
    return sum(float_get_Unique_Views) / count_non0_get_Unique_Views

average_unique_views = unique_Averages(float_get_Unique_Views)
print("The average unique views for StreamerA this month are "+str(average_unique_views))

#get max unique views from all streams this month
max_uniques = max(float_get_Unique_Views)
print("The max uniques this month from StreamerA are "+str(max_uniques))



"""
Count Followers
"""
# assign the values accordingly
#consumer_key = ""
#consumer_secret = ""
#access_token = ""
#access_token_secret = ""

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
#auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

# the ID of the user
id = 1134529606202118145

# fetching the user
user = api.get_user(id)

# fetching the followers_count
followers_count = user.followers_count

print("The number of followers of the user are : " + str(followers_count))

# End of Compilation
print(f'main.py Compilation Complete')