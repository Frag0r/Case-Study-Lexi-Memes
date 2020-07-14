import json,time,random,sys,re
from bs4 import BeautifulSoup
from bs4.element import NavigableString


DataSet_File = open("data/DataSet.html","r", encoding='utf-8')
soup = BeautifulSoup(DataSet_File)
articles = soup.findAll("article")

output = open("articles.html","w",encoding="utf-8")

for entry in articles:
    content = "<article>"+"<title>"+entry.attrs["title"]+"</title>"
    p = entry.findAll("p")
    content+="<content>"
    for el in p:
        for x in el.children:
            if(x.string != None):
                content+= x.string
    content+="</content></article>"
    output.write(content)

output.close()

data = open("articles.html","r",encoding="utf-8")
soup = BeautifulSoup(data)
workingData = soup.findAll("article")

is_A = dict()

regExContentRef = re.compile(r".*refers to.*")
regExContent = re.compile(r".*is a.*")

for art in workingData:
    title = art.find("title").string
    content = art.find("content").string
    if(type(content) is NavigableString):
        content = str(content.encode('utf-8'))
        if(regExContent.match(content)):
            is_A[title] = content

resultFile = open("results.json","w",encoding="utf-8")
resultFile.write(json.dumps(is_A))
resultFile.close()

print("AMOUNT : "+str(len(is_A)))

div = soup.findAll("div", {"class":"references"})

NullSource = 0
MaxSourceCount = 0
MinSource = 0
MaxSource = 0
sourceCount = 0
refCount = 0
for entry in div:
    aliste=entry.findAll("a", {"class": "external-link"})
    srcCount = len(aliste)
    if(srcCount > MaxSource):
        MaxSource = srcCount
    if(srcCount < MinSource):
        MinSource = srcCount
    if(srcCount == 0):
        NullSource=NullSource+1
    if(srcCount == 30):
        MaxSourceCount=MaxSourceCount+1
    sourceCount+=len(aliste)
    refCount=refCount+1

print("Quellen : "+str(sourceCount))
print("Artikel :"+str(refCount))
print("MinSource : "+str(MinSource))
print("MaxSource :"+str(MaxSource))
print("NullSourceCount :"+str(NullSource))
print("MaxSourceCount :"+str(MaxSourceCount))

DataSet = dict()

for x in articles:
    div = x.findAll("div", {"class":"references"})
    print(str(div))