import requests
import re
# from collections import defaultdict

url = "https://raw.githubusercontent.com/elastic/beats/master/filebeat/module/nginx/access/test/access.log"
log = requests.get(url)
# events_metrics = defaultdict(int)
events_metrics = {}
#events_metrics['a'] += 1
#print events_metrics


with open("access.log", "w") as f:
    f.write(log.text)

with open("access.log", "r") as f:
    file_ = f.read()
    print file_
    print "*" * 100
    x = re.findall('\d{2}/[A-Z][a-z]{2}/\d{4}:\d{2}:\d{2}:\d', file_)

print x
for event in x:
    if event in events_metrics.keys():
        events_metrics[event] += 1
    else:
        events_metrics[event] = 1

print events_metrics

for key, val in sorted(events_metrics.items()):
    print key, val