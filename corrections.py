import re
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

digits = {
    '๐': '0',
    '๑': '1',
    '๒': '2',
    '๓': '3',
    '๔': '4',
    '๕': '5',
    '๖': '6',
    '๗': '7',
    '๘': '8',
    '๙': '9'
}

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def thaiDigits(matchobj):
    return digits[matchobj.group(0)]

def tonemarkPos(matchobj):
    return matchobj.group(2) + matchobj.group(1)

def tonemarkSpace(matchobj):
    return matchobj.group(1) + matchobj.group(2)

def article(matchobj):
    num = matchobj.group(1)
    return '\nมาตรา ' + num + matchobj.group(2)

p1 = re.compile(r'[๐๑๒๓๔๕๖๗๘๙]') # thai digits -> arabic digits
p2 = re.compile(r'([่้๊๋])([ัุูิีึื])') # <tonemark><vowel> -> <vowel><tonemark>
p3 = re.compile(r'([ัุูิีึื])\s+([่้๊๋])') # <vowel><space><tonemark> -> <vowel><tonemark>
p4 = re.compile(r'[ ]+$', re.MULTILINE) # <space>+ -> <space>
p5 = re.compile(r'[0-9]+\n+คณะกรรมการร่างรัฐธรรมนูญ 29 มีนาคม 2559\n+') # remove page number and header
p6 = re.compile(r'^\s+มาตรา\s+([0-9]+)(.*?)(?=(\n\s+มาตรา\s+[0-9]+))', re.DOTALL|re.MULTILINE) # just formatting
p7 = re.compile(r'\s+(?=[ัุูิีึื])') # <space><vowel> -> <vowel>

inputf = open('new.html', 'r')
text = inputf.read()
inputf.close()

text = strip_tags(text) # strip html tags
text = p1.sub(thaiDigits, text)
text = p2.sub(tonemarkPos, text)
text = p3.sub(tonemarkSpace, text)
text = p4.sub('', text)
text = p5.sub('', text)
text = p6.sub(article, text)
text = p7.sub('', text)

outputf = open('new.txt', 'w')
outputf.write(text)
outputf.close()
