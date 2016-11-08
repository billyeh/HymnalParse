import requests
import json
import sqlite3
import unicodedata

from bs4 import BeautifulSoup

def parse_text(text):
  text = text.replace("<br/>", "\n")
  soup = BeautifulSoup(text, 'html.parser')
  try:
    lyrics = soup.find_all(class_="lyrics")[0]
  except:
    print('*** unknown song ***')
    return []
  lyrics_array = []
  tds = lyrics.find_all("td")
  song = []
  for i in range(0, len(tds), 2):
    marker = tds[i]
    if 'class' in marker.attrs:
      song.append(marker['class'][0] + ' ' + marker.get_text().strip())
      tds.insert(i, '')
      continue
    content = tds[i + 1]
    if marker.get_text().strip() == '':
      tag = 'nonum'
    elif 'class' in content.attrs:
      tag = content['class'][0]
    else:
      tag = marker.get_text().strip()
    song.append(tag + ' ' + content.get_text())

  return song

if __name__ == '__main__':
  conn = sqlite3.connect('songdb.db')
  c = conn.cursor()
  songs = []
  for line in open('update'):
    category, start, end = line.split()
    for i in range(int(start), int(end)):
      song = category + '/' + str(i)
      print(song)
      song_text = requests.get("http://www.hymnal.net/en/hymn/" + song).text
      song_array = parse_text(song_text)
      if song_array:
        songs.append((song.replace('/', ''), unicodedata.normalize("NFKD", json.dumps(song_array, ensure_ascii=False))))
  c.executemany('insert into songdb(_id, url, song) values(NULL, ?, ?)', songs)
  conn.commit()
