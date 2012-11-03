def get_files_in_directory(directory):
    import os
    dirList = os.listdir(directory)
    files = []
    for d in dirList:
        if d[len(d) - 3: len(d)] == 'txt':
            files.append(d)
    return files

def is_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def replace_unicode(s):
    unicode_chars = {'\xa0': " ", 
                      '\x91': "'", 
                      '\x92': "'", 
                      '\x20\x20': "\\n", 
                      '\x20': " ", 
                      '\x93': '\"', 
                      '\x94': '\"', 
                      ",,": "", 
                      '\n, ': '\\n', 
                      ' Chorus\n,\n,': 'chorus:'}
    for char in unicode_chars:
        s = s.replace(char, unicode_chars[char])
    return s

def jsonify(s):
    global count
    """ Takes a string of the format
    
    #: Song words
    Song words
    Song words
    chorus: Song words
    Song words
    Song words
    
    and turns it into a json object.
    """
    song_s = '{"'
    for i in range(len(s)):
        for word in ['chorus', 'nonum', 'note', 'copyright']:
            if (s[i - 1] == '\n' and s[i: i + len(word) + 1] == word + ':' or
                s[i] == ':' and s[i - len(word): i] == word):
                song_s += '"'
        if (s[i - 1] == '\n' and is_numeric(s[i]) or
            s[i] == ':' and is_numeric(s[i - 1]) or 
            s[i - 1] == ' ' and s[i - 2] == ':'):
            song_s += '"'
        elif  s[i] == '\n' and (is_numeric(s[i + 1]) or s[i + 1] == 'c' or s[i + 1] == 'n'):
            song_s += '",'
        if not (i == len(s) - 2 and s[i] == '\n'):
            song_s += s[i]
    return song_s + '"}'
