import site1, parse
import os

dirList = os.listdir('./hymns')
directories = []
for d in dirList:
    directories.append(d)

parser = site1.HymnHTMLParser(False, ['li', 'p', 'a'], ['div', 'id', 'lyrics'])
counter = 1131
url = 'http://www.hymnal.net/hymn.php/h/'
filename = 'hymns/hymn'
hyphen_found= False

while counter <= 1360:
    # open the correct website and file
    url += str(counter)
    filename += str(counter)
    filename += '.txt'
    filename = os.path.abspath(filename)
    
    # open file and replace symbols
    if filename not in directories:
        parse.parse(url, filename, parser)
        
    # reset the values
    url = 'http://www.hymnal.net/hymn.php/h/'
    filename = 'hymns/hymn'
    counter += 1
