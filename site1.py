import logging
from html.parser import HTMLParser

class HymnHTMLParser(HTMLParser):
    logging.basicConfig(filename='htmlparsing.log', level=logging.INFO)
    def __init__(self, tagging, want_tag, start_on=None):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = []
        self.want_tag, self.tagging, self.start_on = want_tag, tagging, start_on
        
    def handle_starttag(self, tag, attribute):
        if self.start_on:
            if tag == self.start_on[0]:
                for name, value in attribute:
                    if name == self.start_on[1] and value == self.start_on[2]:
                        self.tagging = True
        if self.tagging:
            if tag in self.want_tag:
                for name, value in attribute:
                    self.data.append(str(value) + ': ')
                self.recording += 1
            
    def handle_endtag(self, tag):
        if self.tagging:
            if (tag in self.want_tag) and self.recording:
                self.data.append(str('\n'))
                self.recording -= 1
            if self.start_on:
                if tag == self.start_on[0]:
                    self.tagging = False
            if tag == 'br':
                self.data.append(str('\n'))
                
    def handle_entityref(self, name):
        if self.tagging:
            if name == 'mdash':
                self.data.append(str('-'))
            elif name != 'nbsp':
                logging.info(name)

    def handle_charref(self, name):
        if self.tagging and name != 'nbsp':
            logging.info(name)
            
    def handle_data(self, data):
        if self.recording:
            self.data.append(data)
