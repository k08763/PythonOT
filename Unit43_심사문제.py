import re
p = re.compile('^(http?://)[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-_/.?=]*')
print(p.match(input()) != None)