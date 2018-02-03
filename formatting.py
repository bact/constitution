import re
from xml.dom import minidom

p1 = re.compile(r'<p>(.+?)</p>', re.DOTALL)
p2 = re.compile(r'[^\n]+(\n[^\n]+)(\n\s*\n)*')

def paragraph(matchobj):
    #print('--')
    #print(matchobj.group(1))
    #print('--')
    return p2.sub(subparagraph, matchobj.group(1))

def subparagraph(matchobj):
    para = matchobj.group(0)
    print('<p>')
    print(para)
    print('</p>')
    return '<p>' + para + '</p>'

inputf = open('new2.html', 'r')
text = inputf.read()
inputf.close()

text = p1.sub(paragraph, text)

outputf = open('new3.html', 'w')
outputf.write(text)
outputf.close()
