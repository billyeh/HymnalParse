def run(directory):
    """ Takes a JSON object of the format
    
    {"[TAG]": "Song words
    Song words
    Song words",
    "[TAG]": "Song words
    Song words
    Song words",
    ...}
    
    and turns it into a JSON array of the format
    
    ["[TAG]: Song words
    Song words
    Song words",
    "[TAG]: Song words
    Song words
    Song words",
    ...]
    
    """
    TAGS = ['non', 'cho', 'not', 'cop', ', "']
    import util
    files = util.get_files_in_directory(directory)
    for f in files:
        song_text = open(directory + f, 'r').read()
        song_text = song_text.replace('": "', ' ').replace('{', '[').replace('}', ']').replace('\n', '\\n').replace('",\\n"', '", "')
        new_file = open(directory + f, 'w')
        for i in range(len(song_text)):
            if (song_text[i] == '"' and song_text[i + 1: i + 4] not in TAGS and
                not util.is_numeric(song_text[i + 1]) and song_text[i + 1] != ']'):
                new_file.write('\\"')
            else:
                try:
                    new_file.write(song_text[i])
                except:
                    pass # in this case, you've already finished the file and there is nothing left to do