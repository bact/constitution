# constitution

แปลงรัฐธรรมนูญ (ร่างต้นปี 2559) จาก PDF เป็น HTML
ดูคำอธิบายได้ในสไลด์ https://www.slideshare.net/arthit/pdf-plain-text และโน๊ต https://www.facebook.com/notes/10154493302702646 
 

Convert Thai constitution draft (early 2016) from PDF to plaintext and correct encoding glitches. It is crafted to work with a specific set of PDF. Mainly one from https://www.parliament.go.th/ewtcommittee/ewt/draftconstitution2/download/article/article_20160129132217.pdf and following versions. Cannot be guarantted to work with other PDFs. This is like web scraping, you have to tailor it to a particular website. 

- Use [Apache PDFBox](https://pdfbox.apache.org/) for PDF to HTML
  - ```java -jar pdfbox-app.jar ExtractText -html file.pdf file.html```
  - Cannot convert directly to plaintext, as there are Thai characters in the PDF that use codepoints in Private User Area (PUA) -- all the PUAs will be discarded for conversion to plaintext
- Convert Thai characters that encoded as HTML entities to UTF-8. The same process will also convert PUAs to valid codepoints.
  ```python
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
   ```
- Correct wrong order of Thai characters, like tonemark + vowel --> vowel + tonemark
- Basic reformatting

More explanation (in Thai): [slides](https://www.slideshare.net/arthit/pdf-plain-text), [notes](https://www.facebook.com/notes/10154493302702646)

Ideally, there should be no need for a script like this. All laws should be available in search friendly and machine-readable format.
