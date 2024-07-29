import re
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
with open(filename) as x: f = x.readlines()
timecodes=[]
descriptions=[]
for line in f: 
    matches = re.findall(r'start=([^\&]*)', line)
    if len(matches)>0:
        timecodes.append(matches[0])
    matches = re.findall(r'<[^\]]*\](.*)', line)
    if len(matches)>0:
        descriptions.append(matches[0])
startimes=[]
for i,v in enumerate(descriptions):
    startimes.append({'start':timecodes[i],'description':descriptions[i],'thumbnail':"paste"})
# for m in matches:
print (header)
print (json.dumps(startimes))
print (footer)