import html
import re

pua = {
    '63233': '&#3636;', # 0xf701 Sara I
    '63234': '&#3637;', # 0xf702
    '63235': '&#3638;', # 0xf703
    '63236': '&#3639;', # 0xf704
    '63237': '&#3656;', # 0xf705
    '63238': '&#3657;', # 0xf706 Mai Tho (on Po Pla)
    '63242': '&#3656;', # 0xf70a Mai Ek
    '63243': '&#3657;', # 0xf70b Mai Tho
    '63246': '&#3660;', # 0xf70e Thantakat
    '63248': '&#3633;', # 0xf710  Mai Han Akhat (on Po Pla)
    '63250': '&#3655;', # 0xf712 Mai Tai Khu (on Po Pla)
    '63251': '&#3656;', # 0xf713
    '63252': '&#3657;'  # 0xf714
}

def thaiPUA(matchobj):
    return pua[matchobj.group(1)]

p = re.compile(r'\&\#(\d{5,})\;')

outputf = open('new.html', 'w')
inputf = open('constitution-draft-20160329.html', 'r')
for line in inputf:
    text = p.sub(thaiPUA, line)
    outputf.writelines(html.unescape(text))
inputf.close()
outputf.close()
