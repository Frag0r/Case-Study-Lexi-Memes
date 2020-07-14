from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

class Data:
    """ Alle möglichen Daten erfassen """

    def __init__(self,id,title,content):
        self.ID = id
        self.title = title
        self.content = content

    def get_ID(self):
        return self.ID

    def get_Title(self):
        return self.title

    def get_Content(self):
        puffer = ""
        for entry in self.content:
            i = 0
            while i < len(entry):
                if(i == 0):
                    if(type(entry[0]) is NavigableString):
                        puffer+="<h1>"+entry[0]+"</h1>\n"
                    if(type(entry[0]) is Tag):
                        puffer+="<h1>"+str(entry[0])+"</h1>\n"
                else:
                    if(type(entry[i]) is NavigableString):
                        puffer+=entry[i]+"\n"
                    if(type(entry[i]) is Tag):
                        puffer+=str(entry[i])+"\n"
                i = i+1

        return puffer
