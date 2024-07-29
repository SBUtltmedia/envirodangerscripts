from bs4 import BeautifulSoup
import sys
import json
filename="./template.html"
try:
    filename=sys.argv[1]
except:
    pass

with open(filename) as x: f = x.read()
soup = BeautifulSoup(f)
mydivs = soup.find_all("span", {"class": "view"})
for view in mydivs:
    first_child = next(view.children, None)
    if first_child is not None:
        print(f'curl {first_child["href"]} --insecure -o "files/{first_child["aria-label"]}" ')
