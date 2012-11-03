import site1, parse, util, os

directories = util.get_files_in_directory('./hymns')

def run(song_type, start_song, end_song):
    parser = site1.HymnHTMLParser(False, ['li', 'p', 'a'], ['div', 'id', 'lyrics'])
    url = 'http://www.hymnal.net/hymn.php/' + song_type + '/'
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
        url = 'http://www.hymnal.net/hymn.php/' + song_type + '/'
        filename = 'hymns/hymn'
        start_song += 1
for s in list(range(1, 26)) + [41, 42, 51, 52, 61, 71, 81, 91, 92, 93, 94, 102, 103, 111, 112, 113, 114, 115, 116, 121, 131, 132, 141, 151, 152, 161, 162, 163, 164]:
    run('c', s, s)