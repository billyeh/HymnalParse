import util
files = util.get_files_in_directory('./')
for f in files:
    song_text = open(f, 'r').read()
    song_text = song_text.replace('": "', ' ').replace('{', '[').replace('}', ']').replace('\n', '\\n').replace('",\\n"', '", "')
    new_file = open(f, 'w')
    for i in range(len(song_text)):
        if song_text[i] == '"' and song_text[i + 1: i + 4] not in ['non', 'cho', 'not', 'cop', ', "'] and not util.is_numeric(song_text[i + 1]) and song_text[i + 1] != ']':
            new_file.write('\\"')
        else:
            try:
                new_file.write(song_text[i])
            except:
                pass
