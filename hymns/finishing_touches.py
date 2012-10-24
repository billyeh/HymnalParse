import os, logging
dirList = os.listdir('./')
files = []
for d in dirList:
    files.append(d)
logging.basicConfig(filename='finshing.txt', level=logging.INFO)
log = ''
for f in files:
    file = open(f, 'r')
    song_text = file.read()
    if song_text == '{""}':
        logging.info(f)
    new_file = open(f, 'w')
    for i in range(len(song_text)):
        if (song_text[i] == ':' and song_text[i - 5: i] == 'nonum' or
            song_text[i - 1] == '\n' and song_text[i: i + 6] == 'nonum"'):
            new_file.write('"')
        if  (song_text[i - 1] == '\n' and song_text[i: i + 5] == 'note":' or
            song_text[i] == ':' and song_text[i - 4: i] == 'note'):
            new_file.write('"')
        if i + 1 < len(song_text):
            if song_text[i] == '\n' and song_text[i + 1] == '"' and song_text[i - 2: i] != '",':
                new_file.write('",')
        if (song_text[i] == ':' and song_text[i - 9: i] == 'copyright' or
            song_text[i] == 'c' and song_text[i: i + 9] == 'copyright'):
            new_file.write('"')
        new_file.write(song_text[i])