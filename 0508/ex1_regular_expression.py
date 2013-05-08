import re

#reResult = re.search(r'\w+\s\(\d{4}\s', "Between (2012 and 2015)")
#reResult = re.search(r'\(\d+\s\w+', "Between (2012 and 2015)")
reResult = re.search(r'\w+.(jpg)',"/Library/WebServer/Documents/testa.jpg").group(1)

print reResult