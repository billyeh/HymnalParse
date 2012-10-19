from urllib.request import urlopen
import logging, site2, util

logging.basicConfig(filename='parse.log', level=logging.INFO)
parsed = False

def parse(url, filename, parser):
    global parsed
    web_page = urlopen(url)
    file = open(filename, 'w')
    parser.feed(web_page.read().decode('utf-8'))
    count = 0
    song_str = ''
    while count < len(parser.data):
        line = str(parser.data[count])
        if line[:4] == 'http':
            logging.info(line.split()[0][:len(line.split()[0]) - 1])
            site2.parse_html(line, file)
            parsed = True
        if not parsed:
            if line != 'info: ':
                for i in range(len(line)):
                    song_str += line[i]
        count += 1
    if not parsed:
        file.write(util.jsonify(song_str.rstrip()))
    parsed = False
    del parser.data[:]