from bs4 import BeautifulSoup
from urllib.request import urlopen
from string import punctuation
import util
#import sys

def parse_url(url):
    soup = BeautifulSoup(urlopen(url).read().decode('utf-8'))
    def filt(tag):
        if tag.name == 'font':
            if tag.has_key('class'):
                if tag.parent.parent.parent.name == 'table':
                    if tag.parent.parent.parent.has_key('width'):
                        if tag.parent.parent.parent['width'] in ['400', '500']:
                            return True
                        elif tag.parent.parent.parent['width'] == '760':
                            return tag['class'] == ['text2']
        
    soup = BeautifulSoup(str(soup.find_all(filt)))
    return util.replace_unicode(soup.text)

def parse_html(line, file):
    song = parse_url(line.split()[0][:len(line.split()[0]) - 1])[2:]
    song_string = ''
    for i in range(len(song)):
        if ((song[i] not in ['[', ']']) and 
            not (song[i] in punctuation and song[i - 1] in punctuation) and 
            not (util.is_numeric(song[i - 1]) and song[i] == ",")):
            song_string += song[i]
        elif util.is_numeric(song[i - 1]) and song[i] == ",":
            song_string += ':'
    file.write(util.jsonify(song_string.rstrip()))
#sys.stdout.buffer.write(str(h).encode('utf-8'))
#parse('http://www.witness-lee-hymns.org/hymns/H0013.html')