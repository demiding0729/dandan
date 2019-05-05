import csv
import codecs
import datetime

#Src = r'C:\Users\rost2\Desktop\RESEARCH\2018_Election_Tweets\Ny_District_19.json'   #file with raw data
Src = r'C:\Users\DingYue\Dropbox\19SPRING\3SYSTEM ENGINEERING AND SOCIAL MEDIA\Project\AV_TWEETS\AV_TWEETS2\textdata\negative.csv'
Trg = r'C:\Users\DingYue\Dropbox\19SPRING\3SYSTEM ENGINEERING AND SOCIAL MEDIA\Project\AV_TWEETS\AV_TWEETS2\textdata\negatives2.csv'

In_File = open(Src, 'r')    #open as Unicode text
Out_File = open(Trg, 'w')
lines = In_File.read().split("\n")

for line in lines:        #read the file line by line
    Words = line.strip().lower().split(' ')
    Out_Str = str(Words)+ '\n'
    Out_File.write(Out_Str)

In_File.close()
Out_File.close()
