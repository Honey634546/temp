import os
import csv
from urlManage import urlManage

def readCSV(fileName):
    path = os.getcwd()
    try:
        os.mkdir("url")
    except Exception:
        pass
    CSVFile = open(fileName, 'r')
    reader = csv.reader(CSVFile)
    urlmanage = urlManage()
    for line in reader:
        name = line[0]
        lat = line[1]
        lon = line[2]
        print(line)
        newFile=os.path.join(path+'\\url\\',name+'.txt')
        urlmanage.getUrl(lat,lon,output_file=newFile)



readCSV("test.csv")