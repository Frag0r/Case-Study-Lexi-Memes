from Data import Data

class DataFactory:
    """ Articles[ID] = Data.Object(ID,TITLE,CONTENT)"""
    Articles = dict()

    @staticmethod
    def get_Data():
        return DataFactory.Articles

    @staticmethod
    def get_Entry(id):
        return DataFactory.Articles[id]

    @staticmethod
    def add_Data(id,title,content):
        id = int(id)
        DataFactory.Articles[id] = Data(id,title,content)

    @staticmethod
    def flush_Data():
        DataFactory.Articles.clear()

    @staticmethod
    def get_Count():
        return DataFactory.Articles.__len__()