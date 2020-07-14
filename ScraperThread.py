from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from ExportManager import ExportManager
from DataFactory import DataFactory

class ScraperThread:

    HEADER = {'User-Agent': 'Mozilla/5.0'}

    def __init__(self,article):
        self.set_URL(article[1])
        self.set_REQUEST()
        self.set_RESPONSE()
        self.set_SOUP_PARSER_PARAM("html.parser")
        self.set_PARSER()
        self.title = article[0]
        self.get_Data_by_ID("article","^entry_.+")

    def set_URL(self,url):
        self.URL = url

    def get_URL(self):
        return self.URL

    def get_REQUEST(self):
        return self.REQUEST

    def set_REQUEST(self):
        self.REQUEST = Request(self.get_URL(),headers=self.HEADER)

    def set_RESPONSE(self):
        self.RESPONSE = urlopen(self.get_REQUEST())

    def get_RESPONSE(self):
        return self.RESPONSE

    def get_SOUP_PARSER_PARAM(self):
        return self.SOUP_PARSER_PARAM

    def set_SOUP_PARSER_PARAM(self,parser):
        self.SOUP_PARSER_PARAM = parser

    def get_PARSER(self):
        return self.SOUP_PARSER

    def set_PARSER(self):
        self.SOUP_PARSER = BeautifulSoup(self.get_RESPONSE(), self.get_SOUP_PARSER_PARAM())

    def set_Entry_ID(self):
        self.ENTRY_ID = ""

    def get_Entry_ID(self):
        return self.ENTRY_ID


    def get_Data_by_ID(self,tagname, id_Regex=None):
        DataSet = self.get_PARSER().findAll( tagname, {'id': re.compile(id_Regex)} )
        article = DataSet[0]
        id = DataSet[0].attrs["id"][6:]

        data = []

        h2 = article.findAll("h2")
        for el in h2:
            puffer = []
            while True:
                if(el.name == "h2"):
                    puffer.append(el.contents[0])
                else:
                    puffer.append(el)

                el = el.find_next_sibling()
                if(el == None or el.name == "h2"):
                    data.append(puffer)
                    break
            if(el == None):
                break
        DataFactory.add_Data(id,self.title,data)
        """ x = ExportManager(text) """
