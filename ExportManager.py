from pathlib import Path
import re,json

class ExportManager:

    def __init__(self,data):
        my_file = Path("data/output.html")
        if my_file.is_file():
            # file exists
            outputData=open("data/output.html", "a", encoding="utf-8")
        else:
            outputData=open("data/output.html", "w", encoding="utf-8")
            outputData.write("###knowyourmeme.com extract by Marcel Leschnik###\n")
            outputData.close()
            outputData=open("data/output.html", "a")

        for x in data:
            outputData.write("<article id=\""+str(x)+"\" title=\""+data[x].get_Title()+"\" >\n")
            outputData.write(data[x].get_Content())
            outputData.write(" \n</article>\n")

        outputData.close()