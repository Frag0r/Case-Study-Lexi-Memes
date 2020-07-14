from ScraperFactory import ScraperFactory
from DataFactory import DataFactory
from ExportManager import ExportManager
import json,time,random,sys

class main:

    """
    LogManager hinzufügen und sowas wie ein Debug-Mode
    """

    def __init__(self,arguments):
        logFile = open("log.txt", "w", encoding="utf-8")
        json_file = open(arguments,"r", encoding='utf-8')
        Links_JSON = json.load(json_file)
        first = Links_JSON["3"]
        for x in first:
            title = x
            url = first[x]
            print(title+" -> "+url+"\n")
            ScraperFactory.create_Thread([title,url])
            time.sleep(random.uniform(0.5,2.0))
            if(DataFactory.get_Count() == 25):
                ExportManager(DataFactory.get_Data())
                DataFactory.flush_Data()
                logFile.write("SUCESS FOR 25\n")
                time.sleep(random.randint(20,30))
        logFile.write("SUCESS FOR "+sys.argv[1])
        logFile.close()

app = main("links.json")