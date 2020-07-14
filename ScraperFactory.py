from ScraperThread import ScraperThread

class ScraperFactory:

""" TODO: Add Multi-Threading """

    ScraperList =  []

    @staticmethod
    def get_Scraper(pos):
        return ScraperFactory.ScraperList[pos]

    @staticmethod
    def create_Thread(article):
        ScraperFactory.ScraperList.append(ScraperThread(article))