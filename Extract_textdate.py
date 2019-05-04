import json
import csv
import codecs
import datetime

#Src = r'C:\Users\rost2\Desktop\RESEARCH\2018_Election_Tweets\Ny_District_19.json'   #file with raw data
Src = r'C:\Users\DingYue\Dropbox\....\tweets.json'
Trg = r'C:\Users\DingYue\Dropbox\....\textdatetweet.json'

Users = {}   #this will be the database of our users
User_count = 0    #we will be counting users here
Tweet_count = 0    #we will be counting tweets here
Word_Counts = {}

In_File = codecs.open(Src, 'r', 'UTF-8')    #open as Unicode text
Out_File = codecs.open(Trg, 'w', 'UTF-8')


for line in In_File:        #read the file line by line
    Curr_Tweet = json.loads(line)   #this reads JSON into a Python dictionary
    Words = Curr_Tweet["text"]
    Date = Curr_Tweet["created_at"]
    Out_Str = str(Date)+','+str(Words)+ '\n'
    Out_File.write(Out_Str)

In_File.close()
Out_File.close()
