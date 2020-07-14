from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re,json,time,random,sys

puffer = dict()
i = int(sys.argv[1])
print("Start= "+sys.argv[1])
print("STOP= "+sys.argv[2])

while True:
    url = "https://knowyourmeme.com/memes/all/page/"+str(i)
    req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    res = urlopen(req)
    parser = BeautifulSoup(res, "html.parser")
    DataSet = parser.findAll( "tbody", {'class': "entry-grid-body infinite"} )
    tbody = DataSet[0]
    links = tbody.findAll("a", {'class': "photo"})
    for link in links:
        puffer[link.contents[0].attrs["title"]] = "https://knowyourmeme.com"+link.attrs["href"]
    print(i)
    i = i+1
    time.sleep(random.uniform(0.1, 2.5))
    if(i > int(sys.argv[2])):
        puffer["STOP"] = i
        puffer["STOP_COUNT"] = len(puffer)
        app_json = json.dumps(puffer)
        outputData=open(sys.argv[1]+"--"+sys.argv[2]+".json", "w", encoding="utf-8")
        outputData.write(app_json)
        break