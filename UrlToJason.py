from bs4 import BeautifulSoup
import sys
import json
filename="./template.html"
try:
    filename=sys.argv[1]
except:
    pass
header='''
[wpcode id="5382"]
<div id="player"></div>
<div class="table"></div>
<script>
'''
footer='''
loadSeminarYT(data.ytID,data.startTimes)
</script>
'''
with open(filename) as x: f = x.read()
soup = BeautifulSoup(f,features="html.parser")
mydivs = soup.find_all("iframe")
thumbs= soup.find_all("img")
descriptions=[]
timecodes=[]
thumbnails=[]
descriptions2=[]
for t in soup.select('a[href*=link]'):
    descriptions2.append(t.contents[0])


for thumb in thumbs:
    thumbnails.append(thumb["src"])


for view in mydivs:
    description=""
    try:
        description="".join([str(x)for x in view.parent.find_previous_sibling("div").contents]) 
        # description="".join([str(x)for x in view.find_next_sibling("p").contents]) 
    except:
        pass
    timecode=""
    ytID=""
    try:
        ytID=view["src"].split("?start=")[0].split("/")[-1]
        timecode=view["src"].split("start=")[1].split("&")[0]
    except:
        pass
    descriptions.append(description)
    timecodes.append(timecode)
    # first_child = next(view.children, None)
    # if first_child is not None:
    #     print(f'curl {first_child["href"]} --insecure -o "files/{first_child["aria-label"]}" ')
startimes=[]
for i,v in enumerate(timecodes):
    time = timecodes[i] or ""
    desc= descriptions[i]  or ""
    desc2=descriptions2[i] or ""
    thumb= thumbnails[i] or ""
    startimes.append({'start':time,'description':f"{desc} {desc2}",'thumbnail':thumb})
data={'ytID':ytID,'startTimes':startimes}
print (header)
print ('data='+json.dumps(data, indent=4))
print (footer)