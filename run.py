import site1, parse
import os

dirList = os.listdir('./hymns')
directories = []
for d in dirList:
    directories.append(d)

def run(song_type, start_song, end_song):
    parser = site1.HymnHTMLParser(False, ['li', 'p', 'a'], ['div', 'id', 'lyrics'])
    url = 'http://www.hymnal.net/hymn.php/ns/'
    filename = 'hymns/hymn'
    while start_song <= end_song:
        # open the correct website and file
        url += str(start_song)
        filename += str(start_song) + '.txt'
        filename = os.path.abspath(filename)
    
        # open file and replace symbols
        if filename not in directories:
            parse.parse(url, filename, parser)
        
        # reset the values
        url = 'http://www.hymnal.net/hymn.php/ns/'
        filename = 'hymns/hymn'
        start_song += 1
run('ns', 1, 384)